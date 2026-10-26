#!/usr/bin/env python3
"""Verify prepared release files using Python 3 standard library only.

Usage: python3 scripts/verify_release.py [release_directory]
       python3 scripts/verify_release.py [release_directory] --genomes path/to/Genomes_889.tar.gz
The optional genome check reads every archived assembly and checks its digest.
This utility was written for deposit preparation. It is not the original analysis pipeline.
"""
import argparse, collections, csv, hashlib, json, re, tarfile
from pathlib import Path

def digest(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
 return h.hexdigest()

def fasta(path):
 records={};name=None
 with path.open() as f:
  for line in f:
   if line.startswith('>'):
    name=line[1:].split()[0]
    if name in records:raise ValueError('Duplicate FASTA ID: '+name)
    records[name]=''
   elif line.strip():
    if name is None:raise ValueError('Sequence precedes header: '+str(path))
    records[name]+=line.strip()
 if not records or not all(records.values()):raise ValueError('Empty FASTA: '+str(path))
 return records

def tips(path):
 # Supports the unquoted or single-quoted leaf labels used by these Newick files.
 s=path.read_text().strip()
 if not s.endswith(';') or s.count('(')!=s.count(')'):raise ValueError('Malformed Newick: '+str(path))
 labels=[a.replace("''", "'") if a else b.strip() for a,b in re.findall(r"[\(,]\s*(?:'((?:[^']|'')*)'|([^\s\(\),:;][^\(\),:;]*))(?=\s*[:),;])",s)]
 if len(labels)!=len(set(labels)):raise ValueError('Duplicate Newick tips')
 return set(labels)

def subsequence(s,raw):
 it=iter(raw)
 return all(any(x==c for x in it) for c in s.replace('-',''))

def verify(root,genomes=None):
 manifest=root/'SHA256SUMS.txt'
 for line in manifest.read_text().splitlines():
  expected,name=line.split('  ',1);p=root/name
  if not p.is_file() or digest(p)!=expected:raise ValueError('Checksum mismatch: '+name)
 results={}
 for name,n,cols in [('broad_889',889,2644),('focused_40',40,1286)]:
  d=root/'alignments'/name
  a=fasta(d/'NifHDK_aligned.faa');u=fasta(d/'NifHDK_unaligned.faa');t=tips(next((root/'trees'/name).glob('*.nwk')))
  assert len(a)==n and set(a)==set(u)==t,(name,'IDs/count')
  assert {len(x) for x in a.values()}=={cols},(name,'length')
  assert all(subsequence(a[k],u[k]) for k in a),(name,'alignment not subsequence')
  results[name]={'sequences':n,'alignment_columns':cols,'IDs_and_trimmed_sequences':'PASS'}
 broad=fasta(root/'alignments/broad_889/NifHDK_unaligned.faa');small=fasta(root/'alignments/focused_40/NifHDK_unaligned.faa')
 assert all(broad.get(k)==v for k,v in small.items())
 proteins=[fasta(root/'proteins'/('Nif'+g+'_889.faa')) for g in 'HDK']
 assert all(set(p)==set(broad) for p in proteins)
 assert all(broad[k]==''.join(p[k] for p in proteins) for k in broad)
 if genomes:
  rows=list(csv.DictReader((root/'metadata/genome_sequence_manifest.tsv').open(),delimiter='\t'))
  expected={x['genome_archive_path']:x['genome_sha256'] for x in rows};seen=set()
  with tarfile.open(genomes,'r|gz') as tar:
   for member in tar:
    if not member.isfile():continue
    assert member.name in expected,member.name
    h=hashlib.sha256();f=tar.extractfile(member)
    for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
    assert h.hexdigest()==expected[member.name],member.name
    seen.add(member.name)
  assert seen==set(expected)
  results['genomes']={'assemblies':len(seen),'archived_bytes':'PASS'}
 return results

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('root',nargs='?',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--genomes',type=Path);a=p.parse_args()
 print(json.dumps(verify(a.root.resolve(),a.genomes),indent=2))
