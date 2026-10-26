# Genome assemblies and NifHDK phylogenetic data for Synechocystis sp. LKSZ1

This repository contains final NifHDK sequence alignments, displayed phylogenetic trees, iTOL annotation files, and genome metadata associated with the study of nitrogen fixation in Synechocystis sp. LKSZ1.

The release was prepared from supplied files on 26 October 2026. Sequence characters, FASTA identifiers, Newick trees, and iTOL annotations were retained without modification. Descriptive names were assigned to copies of the alignment files. Original tree filenames were retained.

## Contents

| Path | Contents |
| --- | --- |
| `alignments/broad_889/` | Aligned and unaligned concatenated NifHDK sequences for 889 representatives, corresponding to S3 Fig. The alignment has 2,644 columns. |
| `alignments/focused_40/` | Aligned and unaligned concatenated NifHDK sequences for the 40-sequence LKSZ1-related dataset, corresponding to Fig 7. The alignment has 1,286 columns. |
| `proteins/` | Individual NifH, NifD, and NifK sequence collections, each containing 889 records. |
| `trees/` | The supplied broad 889-tip tree and focused 40-tip tree in Newick format. |
| `itol/` | Supplied iTOL annotations, retained as provided. |
| `previews/` | Supplied PDF tree views for reference. The Newick files contain the machine-readable trees. |
| `metadata/` | Genome-to-sequence mapping, supplied biological metadata, initial screening inventory, and validation results. |
| `partitions/` | Gene boundaries reconstructed from the manuscript Methods. These are newly prepared tables, not original inference partition files. |
| `METHODS_AND_LIMITATIONS.md` | Reported analysis settings and the scope of the archived data. |
| `DATA_DICTIONARY.md` | File and metadata definitions. |
| `scripts/verify_release.py` | An offline release verification utility written during deposit preparation. |

## Genome assemblies

The matching Figshare deposit contains `Genomes_889.tar.gz`, with 889 genome FASTA files, and `NifHDK_individual_proteins.tar.gz`, with per-genome protein FASTA files and the aggregate protein collections. A corresponding analysis archive preserves this repository's data and documentation. The reserved Figshare DOI is https://doi.org/10.6084/m9.figshare.34788258. It becomes active when the dataset is published. The repository is https://github.com/leoken422/LKSZ1-NifHDK-data. The version-specific dataset DOI and repository release will be recorded when finalized.

The assemblies are the exact supplied analysis copies. Their original contig identifiers have not been independently verified against source assemblies. File identifiers and sequence hashes allow these copies to be distinguished from subsequently downloaded or updated records.

## Verify this release

Python 3 is sufficient. No third-party packages or network connection are required.

```bash
python3 scripts/verify_release.py .
```

This checks SHA256 digests, FASTA record uniqueness, matching tree-tip and alignment IDs, alignment lengths, agreement between the 40-sequence and 889-sequence raw sets, and compatibility of trimmed alignments with the unaligned sequences. To also verify every archived genome against the manifest, provide the downloaded genome archive.

```bash
python3 scripts/verify_release.py . --genomes /path/to/Genomes_889.tar.gz
```

## Scope of reproducibility

The deposit freezes the supplied 889 genome assemblies and the available NifHDK sequence and tree outputs. The broad analysis included an additional 1,129 reference sequences during inference. Those sequences, the complete broad inference alignment, the unpruned inference tree, original execution logs, and original screening or assembly scripts were unavailable for this deposit. The archived broad tree and alignment contain the 889 displayed representatives.

The verification utility checks file integrity and internal sequence consistency. It does not repeat the original screening, assembly, or phylogenetic inference. The initial-screen inventory contains metadata for 19,243 screened genomes. It does not include assemblies for all 19,243 genomes.

## Citation and reuse

Use the version-specific Figshare DOI for the data used in the paper and identify the GitHub release and commit for this repository. Consult `CITATION.md` and `LICENSING.md`. Original source accessions are preserved where supplied. Unresolved source fields remain explicitly identified in the metadata.
