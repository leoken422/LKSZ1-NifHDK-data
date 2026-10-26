# Data definitions and table legends

All TSV files are UTF-8 text with a header row and tab-separated columns. Blank cells and supplied phrases such as `Not resolved` retain their original meanings. They indicate unavailable metadata and do not establish biological absence.

## genome_sequence_manifest.tsv

One row per supplied genome and NifHDK representative, for 889 rows. `tree_tip_id` is the exact FASTA and Newick leaf identifier. `genome_id` identifies the matching supplied genome and per-strain protein directory. `genome_archive_path` locates the FASTA within the genome archive. The association was made from per-strain protein FASTA headers and checked against the aggregate protein sets.

`genome_file_bytes`, `genome_contigs`, and `genome_length_bp` describe the supplied FASTA file. Genome length counts all nucleotide symbols, including ambiguous bases. `first_contig_header` is copied from the first FASTA header. `genome_sha256` hashes the original file bytes, including headers and line wrapping.

`nifH_length_aa`, `nifD_length_aa`, and `nifK_length_aa` count amino acid characters in the corresponding unaligned protein sequence. The protein SHA256 fields hash the case-preserved sequence string alone, without its FASTA header or line breaks. They are not FASTA file digests.

`organism_or_tree_taxon`, `strain_or_bin_id`, `assembly_accession`, `biosample_accession`, `bioproject_accession`, `origin`, and `isolation_source` are copied from the supplied S6 table. `in_focused_40` indicates membership in the focused dataset. `assembly_record_url` is formed only when the supplied assembly accession includes an explicit GCA/GCF version. It does not establish a successful remote metadata or sequence check.

`provenance_status`, `original_contig_ids_status`, `source_license`, and `metadata_source` describe the extent of source verification. Missing source licences are recorded as `not_supplied`. An unresolved source does not imply a new assembly or a particular ownership status.

## broad_889_supplied_metadata.tsv and focused_40_supplied_metadata.tsv

These preserve the eight data columns from the supplied S6 and S7 tables as values. The tables contain 889 and 40 sequence records, respectively. The source workbook legends were not copied as assertions about the new release. Some source metadata are incomplete.

## initial_screening_19243_supplied.tsv

This preserves the supplied initial screening worksheet as values. It describes the screened set, not 19,243 archived genome assemblies. `genome_file_id`, `num_sequences`, and `total_length_bp` correspond to the source file identifier, sequence count, and assembly length fields. The seven `taxonomy_column_*` fields retain the source taxonomy cells in their original order. The worksheet header above these cells reads `GTTDB R226`. `supplied_Category` preserves the source Category field without reinterpreting its values. `extra_column_13` retains the final source column.

`selected_ids_not_exactly_matched_to_initial_screen.tsv` records selected genome filenames that did not match an initial screening file ID verbatim. A naming difference is not interpreted as biological inconsistency. `unresolved_assembly_sources.tsv` lists records without an explicit versioned GCA/GCF assembly accession in the supplied S6 metadata.

## Sequence, tree, and partition files

FASTA headers and Newick leaf IDs are preserved exactly. Concatenation order is NifH, NifD, NifK. A hyphen in an aligned sequence represents an alignment gap. Trimming can make an ungapped aligned sequence shorter than its corresponding unaligned sequence. All archived aligned sequences were checked to be ordered subsequences of the corresponding unaligned records.

Partition tables use 1-based inclusive coordinates reconstructed from the manuscript Methods. See `METHODS_AND_LIMITATIONS.md` for model and support definitions. Display roots do not determine the direction of horizontal gene transfer.

## Digests and validation

`additional_supplied_protein_files.tsv` identifies any files additional to the standard NifH.faa, NifD.faa, and NifK.faa trio. The supplied `NifK(1).faa` for GCF_000317125 is byte-identical to NifK.faa. It is retained in the protein archive as an original supplied duplicate, not counted as another representative or biological copy.

`SHA256SUMS.txt` records whole-file hashes for the repository contents, excluding the checksum file itself. `metadata/validation_report.json` describes checks made during local preparation and identifies unavailable historical inputs. Hashes establish the identity of this frozen copy. They do not independently verify source attribution or biological annotation.
