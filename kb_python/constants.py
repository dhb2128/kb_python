INFO_FILENAME = 'info.txt'

# Default filenames
CDNA_FILENAME = 'cdna.fa'
INTRON_FILENAME = 'introns.fa'
SORTED_FASTA_FILENAME = 'sorted.fa'
SORTED_GTF_FILENAME = 'sorted.gtf'
COMBINED_FILENAME = 'combined.fa'
INDEX_FILENAME = 'transcriptome.idx'
WHITELIST_FILENAME = 'whitelist.txt'
FILTER_WHITELIST_FILENAME = 'filter_barcodes.txt'
INSPECT_FILENAME = 'inspect.json'

BUS_FILENAME = 'output.bus'
BUS_S_FILENAME = 'output.s.bus'
BUS_SC_FILENAME = 'output.s.c.bus'
BUS_UNFILTERED_FILENAME = 'output.unfiltered.bus'
BUS_FILTERED_FILENAME = 'output.filtered.bus'
BUS_CDNA_PREFIX = 'spliced'
BUS_INTRON_PREFIX = 'unspliced'
ECMAP_FILENAME = 'matrix.ec'
TXNAMES_FILENAME = 'transcripts.txt'
KB_INFO_FILENAME = 'kb_info.json'
KALLISTO_INFO_FILENAME = 'run_info.json'
REPORT_NOTEBOOK_FILENAME = 'report.ipynb'
REPORT_HTML_FILENAME = 'report.html'
COUNTS_PREFIX = 'cells_x_genes'
TCC_PREFIX = 'cells_x_tcc'
FEATURE_PREFIX = 'cells_x_features'
ADATA_PREFIX = 'adata'
GENE_NAME = 'gene'
FEATURE_NAME = 'feature'
TRANSCRIPT_NAME = 'transcript'

UNFILTERED_COUNTS_DIR = 'counts_unfiltered'
FILTERED_COUNTS_DIR = 'counts_filtered'
CELLRANGER_DIR = 'cellranger'
CELLRANGER_MATRIX = 'matrix.mtx'
CELLRANGER_BARCODES = 'barcodes.tsv'
CELLRANGER_GENES = 'genes.tsv'

BUS_UNFILTERED_SUFFIX = '.unfiltered.bus'
BUS_FILTERED_SUFFIX = '.filtered.bus'

# Smartseq file names
BATCH_FILENAME = 'batch.txt'
ABUNDANCE_FILENAME = 'matrix.abundance.mtx'
CELLS_FILENAME = 'matrix.cells'
GENE_DIR = 'counts_gene'

# File codes.
# These are appended to the filename whenever it undergoes some kind of
# transformation.
SORT_CODE = 's'
CORRECT_CODE = 'c'
FILTERED_CODE = 'filtered'
UNFILTERED_CODE = 'unfiltered'
PROJECT_CODE = 'p'
