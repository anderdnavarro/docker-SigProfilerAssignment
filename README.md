# docker-SigProfilerAssignment

Dockerfile used to run [SigProfilerAssignment](https://github.com/AlexandrovLab/SigProfilerAssignment) (v.0.1.9) developed by AlexandrovLab.

## Installation

```bash
docker build -t sigprofilerassignment .
```

> *Only the GRCH37 database has been installed. Please modify the Dockerfile before building to install the desired genome.*

## Basic usage

```bash
# For SBS
docker run --rm -u $(id -u):$(id -g) \
           -v $(pwd):/home \
           -it sigprofilerassignment --samples /home/vcfs/ \
                                     --export_probabilities_per_mutation True

# For ID
docker run --rm -u $(id -u):$(id -g) \
           -v $(pwd):/home \
           -it sigprofilerassignment --samples /home/vcf/
                                     --export_probabilities_per_mutation True \
                                     --context_type ID \
                                     --collapse_to_SBS96 False 
```

### Available options
```bash
docker run --rm -it sigprofilerassignment --help

# Options:
#   --samples PATH                  Path to the input somatic mutations file (if using segmentation file/mutational matrix) or input folder (mutation calling file/s) [required]
#   --output DIRECTORY              Path to the output folder  [default: /home]
#   --input_type STRING             Three accepted input types: vcf (for vcf/maf files), seg (for different segmentation files) and matrix (for mutational matrix) [default: vcf]
#   --context_type INT/STRING       Required context type if input_type is vcf. context_type takes which context type of the input data is considered for assignment [default: 96]
#   --collapse_to_SBS96 BOOL        By default sigantures are collapsed to SBS96 context. Use this option to disable the collapsing to SBS96 context if you are using other context types [default: True]
#   --cosmic_version FLOAT          Defines the version of the COSMIC reference signatures  [default: 3.4]
#   --exome BOOLEAN                 Defines if the exome renormalized COSMIC signatures will be used  [default: False]
#   --genome_build STRING           The reference genome build, used for select the appropriate version of the COSMIC reference signatures, as well as processing the mutation calling file/s  [default: GRCh37]
#   --signature_database PATH       Path to the input set of known mutational signatures (only in case that COSMIC reference signatures are not used), a tab delimited file that contains the signature matrix where the rows are mutation types and columns are signature IDs
#   --export_probabilities BOOLEAN  Defines if the probability matrix per mutational context for all samples is created  [default: True]
#   --export_probabilities_per_mutation BOOLEAN
#                                   Defines if the probability matrices permutation for all samples are created. Onlya vailable when input_type is vcf  [default:False]
#   --make_plots BOOLEAN            Toggle on and off for making and saving plots  [default: True]
#   --sample_reconstruction_plots STRING
#                                   Select the output format for sample reconstruction plots
#   --verbose BOOLEAN               Prints detailed statements  [default: False]
#   --help                          Show this message and exit.
```
