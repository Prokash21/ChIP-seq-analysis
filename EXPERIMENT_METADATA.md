# ChIP-seq Experiment Metadata

**Project:** ChIP-seq Analysis of DMTF1 and H2AZ in Mouse Neural Stem Cells

**Generated:** October 24, 2025

---

## Experimental Overview

### Primary Research Question
Investigation of DMTF1 protein binding and its role in regulating H2AZ chromatin dynamics in mouse neural stem cells (NSCs), with particular focus on how DMTF1 knockdown affects H2AZ distribution genome-wide.

---

## Experimental Design

### Experiment 1: DMTF1 ChIP-seq
- **Protein Target:** DMTF1 (Cyclin D/CDK Binding Protein)
- **Cell Type:** Mouse neural stem cells (NSCs)
- **Condition:** Wild-type (WT)
- **Purpose:** Map DMTF1 binding sites across the genome

### Experiment 2: H2AZ ChIP-seq - Control
- **Histone Variant:** H2AZ (Histone 2A variant)
- **Cell Type:** Mouse neural stem cells (NSCs)
- **Condition:** Wild-type (WT) - Control group
- **Purpose:** Establish baseline H2AZ distribution in unperturbed NSCs

### Experiment 3: H2AZ ChIP-seq - DMTF1 Knockdown
- **Histone Variant:** H2AZ (Histone 2A variant)
- **Cell Type:** Mouse neural stem cells (NSCs)
- **Condition:** DMTF1 knockdown (KD)
- **Purpose:** Determine how DMTF1 loss affects H2AZ chromatin localization

---

## Sample Information

### Total Samples: 16 (across all experiments)

| Experiment | Condition | Replicates | SRR IDs | Purpose |
|------------|-----------|-----------|---------|---------|
| DMTF1 ChIP-seq | WT NSCs | Multiple | SRR28702398-SRR28702410 (subset) | DMTF1 binding map |
| H2AZ ChIP-seq | WT NSCs (Control) | Multiple | SRR28702398-SRR28702407 (subset) | Baseline H2AZ |
| H2AZ ChIP-seq | DMTF1 KD | Multiple | SRR28702408-SRR28702413 (subset) | H2AZ after DMTF1 loss |

*Note: Exact sample assignment to conditions will be determined during analysis phase.*

---

## Biological Context

### DMTF1 (Cyclin D/CDK Binding Protein)
- **Function:** Transcriptional regulator and cell cycle control protein
- **Role in NSCs:** Potential regulator of neural stem cell self-renewal and differentiation
- **Mechanism of Interest:** Possible interaction with chromatin remodeling complexes

### H2AZ (Histone 2A Variant)
- **Function:** Histone variant incorporated at promoters and regulatory regions
- **Genomic Distribution:** 
  - Enriched at nucleosome-depleted regions (NDRs)
  - Associated with active promoters
  - Found at both active and poised genes
- **Role in Gene Regulation:** 
  - Promotes transcriptional activation
  - Maintains chromatin accessibility
  - Important for developmental gene regulation

### Mouse Neural Stem Cells (NSCs)
- **Cell Type:** Neural progenitor cells with self-renewal capacity
- **Developmental Significance:** 
  - Critical for brain development
  - Maintained throughout adult neurogenesis
  - Sensitive to epigenetic regulation
- **ChIP-seq Advantages:** 
  - Well-characterized cell type
  - High chromatin accessibility
  - Relevant for developmental biology

---

## Experimental Hypothesis

### Primary Hypothesis
DMTF1 acts as a co-factor or regulator of chromatin remodeling complexes that affect H2AZ incorporation at specific genomic loci in mouse neural stem cells.

### Predicted Outcomes

#### If DMTF1 facilitates H2AZ incorporation:
- H2AZ signal will decrease at DMTF1 binding sites after DMTF1 knockdown
- Correlation between DMTF1 peaks and H2AZ peaks in WT NSCs
- Gene expression changes corresponding to H2AZ loss

#### If DMTF1 competes with or excludes H2AZ:
- H2AZ signal will increase at DMTF1 binding sites after DMTF1 knockdown
- Negative correlation between DMTF1 and H2AZ peaks
- Opposite chromatin accessibility patterns

#### If DMTF1 has indirect effects:
- H2AZ changes will be genome-wide and less localized
- Effects on H2AZ may be secondary to transcriptional changes

---

## Expected Analyses

### 1. Quality Control and Preprocessing
- FastQC analysis of raw reads
- Adapter trimming and quality filtering
- Alignment to mouse reference genome (mm10 or mm39)
- BAM file sorting and indexing

### 2. Peak Calling
- **DMTF1 ChIP-seq:** MACS2 peak calling against input control
- **H2AZ ChIP-seq (WT):** Peak calling against input control
- **H2AZ ChIP-seq (KD):** Peak calling against input control
- **Controls:** IgG or input DNA controls for normalization

### 3. Comparative Analysis
- H2AZ peak comparison between WT and DMTF1 KD conditions
- Correlation analysis between DMTF1 and H2AZ peaks
- Differential enrichment analysis
- Annotation of peaks to genes and regulatory elements

### 4. Genomic Feature Analysis
- **Gene Proximity:** Classify peaks relative to TSS, promoters, enhancers
- **Repeat Elements:** Assess if peaks overlap with repetitive sequences
- **CpG Islands:** Analyze CpG enrichment in peak regions
- **Chromatin States:** Cross-reference with chromatin state maps if available

### 5. Motif Analysis
- De novo motif discovery in DMTF1 peaks
- Known transcription factor motif enrichment
- DNA sequence composition analysis

### 6. Gene Expression Correlation
- RNA-seq data integration (if available)
- Correlation of ChIP-seq signal with gene expression
- Pathway analysis of genes near DMTF1 and H2AZ peaks
- GO enrichment analysis (Gene Ontology)

### 7. Functional Analysis
- Integrative Genomics Viewer (IGV) visualization
- Genome browser track generation
- Publication-quality figures

---

## Technical Specifications

### Genome Reference
- **Species:** Mouse (*Mus musculus*)
- **Genome Build:** mm10 or mm39 (specified in config.yaml)
- **Bowtie2 Index:** Located at `/scratch/genomic_med/apps/annot/indexes/bowtie/hg19`
  - *Note: May need to update to mouse mm10 index*

### MACS2 Parameters
- **Genome Size:** hs (human) in current config
  - *Note: Should update to 'mm' for mouse (2.7e9 bp)*
- **Expected p-value:** 0.05 (default)
- **Fold Enrichment:** 2-3x typical threshold

### Sequencing Depth Estimates
- **Target Reads:** 20-50 million mapped reads per sample (standard for ChIP-seq)
- **Expected Coverage:** Sufficient for peak detection with proper biological replicates

---

## Sample Organization Scheme

### Proposed Sample Naming Convention
```
SRR_ID_EXPERIMENT_CONDITION_REPLICATE
```

**Examples:**
- SRR28702398_DMTF1_WT_Rep1
- SRR28702399_DMTF1_WT_Rep2
- SRR28702401_H2AZ_WT_Rep1
- SRR28702403_H2AZ_WT_Rep2
- SRR28702405_H2AZ_KD_Rep1
- SRR28702406_H2AZ_KD_Rep2

*Actual mapping to be confirmed during experimental metadata review*

---

## Control Samples

### Recommended Controls
- **Input DNA:** Sonicated genomic DNA before ChIP (present in most studies)
- **Negative Control:** IgG immunoprecipitation or non-specific antibody
- **Positive Control:** Known peaks (if available from literature)

### Quality Metrics
- **Enrichment (NSC):** Peak signal should be >5-fold over input
- **Library Complexity:** Estimated from duplicate reads
- **Reproducibility:** Replicate correlation (Spearman r > 0.8)

---

## Downstream Computational Tools

### Required Software (via Conda)
1. **Bowtie2** - Read alignment
2. **SAMtools** - BAM processing
3. **MACS2** - Peak calling
4. **Bedtools** - Genomic interval operations
5. **R/Bioconductor** - Statistical analysis
   - ChIPseeker - Peak annotation
   - DiffBind - Differential binding analysis
   - ggplot2 - Visualization

### Optional Tools
- **IGV** - Interactive visualization
- **HOMER** - Motif discovery and annotation
- **DESeq2** - Differential enrichment
- **Vegan** - Diversity analysis

---

## Expected Outputs

### Primary Outputs
1. **Peak Files (BED format)**
   - DMTF1_WT_peaks.bed
   - H2AZ_WT_peaks.bed
   - H2AZ_KD_peaks.bed

2. **Bigwig Tracks (for genome browser)**
   - DMTF1_WT.bw
   - H2AZ_WT.bw
   - H2AZ_KD.bw

3. **Annotated Peak Lists**
   - Peak to gene assignments
   - Chromatin feature annotations
   - Motif enrichment results

### Comparative Analysis Outputs
1. **Differential Enrichment**
   - H2AZ comparison (WT vs KD)
   - Statistically significant changes
   - Log2 fold-change files

2. **Correlation Matrices**
   - DMTF1 vs H2AZ correlation
   - Sample-to-sample correlations
   - Replicate reproducibility metrics

3. **Visualizations**
   - Heatmaps of ChIP-seq signal
   - Venn diagrams of overlapping peaks
   - Genome browser screenshots
   - Distribution plots

---

## Data Integration

### Cross-Reference with Public Databases
- **ENCODE:** Mouse ChIP-seq data for comparison
- **GEO (Gene Expression Omnibus):** Similar experiments
- **UCSC Genome Browser:** Known regulatory elements
- **Roadmap Epigenomics:** Mouse NSC chromatin state

### RNA-seq Integration (if available)
- Gene expression correlation with H2AZ signal
- Validation of ChIP-seq findings
- Functional interpretation of binding events

---

## Timeline and Milestones

| Phase | Task | Expected Duration |
|-------|------|-------------------|
| **Phase 1** | Data QC & Preprocessing | 1-2 days |
| **Phase 2** | Alignment & Peak Calling | 2-3 days |
| **Phase 3** | Basic Analysis | 3-5 days |
| **Phase 4** | Comparative Analysis | 3-5 days |
| **Phase 5** | Motif & Functional Analysis | 3-7 days |
| **Phase 6** | Publication Figures | 2-3 days |

**Total Estimated Time:** 2-3 weeks

---

## Important Considerations

### Biological Replicate Requirements
- Minimum 2-3 biological replicates per condition
- Current samples: 16 total (allows for ~3 replicates per condition)
- More replicates improve statistical power

### Sequencing Depth
- Verify that sequencing depth is sufficient for peak detection
- Check SRA metadata for read numbers and quality

### Genome Version Consistency
- Ensure all reference sequences use same genome build
- Update config.yaml Bowtie index for mouse (not human)
- Update MACS2 genome size parameter

### Antibody Specificity
- Verify antibody quality from source metadata
- Cross-reference peak patterns with known regulatory regions

---

## Next Steps

1. **Confirm sample-to-condition mapping** from original experimental design
2. **Update pipeline configuration** for mouse genome (mm10)
3. **Adjust MACS2 parameters** for mouse genome size
4. **Execute full pipeline** with all 16 samples
5. **Generate comparative analysis** of H2AZ WT vs KD
6. **Correlate DMTF1 and H2AZ** peak locations
7. **Perform functional annotation** and gene enrichment

---

## References and Resources

### Key Publications
- DMTF1 function in gene regulation
- H2AZ in neural development
- ChIP-seq best practices for chromatin analysis

### Bioinformatics Resources
- ENCODE ChIP-seq Best Practices
- Bowtie2 Manual
- MACS2 Documentation
- ChIPseeker Vignettes

### Experimental Context
- Mouse NSC biology and chromatin state maps
- ENCODE data for mouse neural tissues
- Regulatory element annotations

---

**Experiment Metadata Status:** Complete and Ready for Analysis

**Contact/Notes:** Update configuration files before pipeline execution
