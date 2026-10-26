# Reported methods and available materials

These settings were transcribed from the accompanying manuscript. The historical commands and logs were not available. No original inference command is reconstructed or represented as having been executed during deposit preparation.

## Initial selection

The manuscript reports screening 19,243 cyanobacterial genomes available as of January 2026 using Nif-Finder v1 for the six core genes nifHDKENB. Concatenated NifH, NifD, and NifK sequences were grouped using CD-HIT at 99% amino acid sequence identity, yielding 889 representatives. The supplied initial-screen worksheet contains a field labelled `GTTDB R226`. This label is retained as source context and has not been reconciled against database release files. The database provenance and actual historical command options cannot be established from the supplied FASTA files alone.

## Broad analysis

The manuscript reports inclusion of 1,129 additional reference NifHDK sequences representing nitrogenase groups I to IV, alignment with MAFFT v7.5 using --add and --keeplength, trimming with trimAl v1.5.1, and concatenation in NifH, NifD, NifK order. Reported lengths were 520, 1,207, and 917 columns, giving 2,644 columns in total. The inferred tree used FastTree v2.2.0 with the LG model, gamma-rescaled branch lengths, and SH-like local support. The additional reference sequences were removed for display.

The archived alignment and tree contain 889 representatives. They are not the complete historical inference input. The supplied tree filename contains `Bootstrap100`. The manuscript describes its support as SH-like local support. The filename alone does not establish a bootstrap analysis, and execution logs are unavailable to resolve the historical naming. Root placement and support presentation should be interpreted using the manuscript and figure legends.

## Focused analysis

The 40 raw concatenated sequences match the corresponding records in the 889-sequence set. The manuscript reports trimAl v1.5.1 with -noallgaps followed by -automated1, then concatenation of NifH, NifD, and NifK alignments of 286, 481, and 519 columns. IQ-TREE v3.1.2 used separate gene partitions with models LG+I+G4, WAG+I+G4, and Q.PFAM+I+G4, respectively. Support was assessed with 1,000 ultrafast bootstrap replicates and -bnni. The final concatenated alignment and tree are available. Original partition files, separate trimmed gene alignments, seeds, and complete execution commands are unavailable.

## Newly prepared boundary tables

Broad boundaries are NifH 1 to 520, NifD 521 to 1,727, and NifK 1,728 to 2,644. Focused boundaries are NifH 1 to 286, NifD 287 to 767, and NifK 768 to 1,286. Coordinates are 1-based and inclusive. These tables are calculated from the lengths reported in the manuscript. They are not recovered original partition files or an independent validation of historical inference settings.

## Missing provenance

The genome mapping uses per-genome protein headers to connect each tree-tip ID to the supplied genome filename. The pairing is supported by the supplied directory structure and agreement between per-genome and aggregate protein sequences. Protein loci have not been independently reannotated or mapped to the genome DNA during this preparation.

The supplied metadata contain unresolved MAG origins, missing assembly versions, and blank biological source fields. Missing values have not been filled by inference from file names. An NCBI assembly link indicates that an accession was supplied, not that the assembly bytes or metadata were independently retrieved and verified. The absence of an assembly accession does not establish that an assembly is newly generated in this study.
