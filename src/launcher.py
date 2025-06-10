#!/usr/local/bin/python3

import os
import click
from SigProfilerAssignment import Analyzer as Analyze

@click.command(name="SigProfilerAssignment")
@click.option("--samples",
              type=click.Path(exists=True),
              required=True,
              help="Path to the input somatic mutations file (if using segmentation file/mutational matrix) or input folder (mutation calling file/s)")
@click.option("--output",
              type=click.Path(exists=True, file_okay=False),
              required=False,
              default=os.getcwd(),
              show_default=True,
              help="Path to the output folder")
@click.option("--input_type",
              type=click.Choice(["vcf", "seg:ASCAT", "seg:ASCAT_NGS", "seg:SEQUENZA", "seg:ABSOLUTE", "seg:BATTENBERG", "seg:FACETS", "seg:PURPLE", "seg:TCGA", "matrix"]),
              metavar="STRING",
              show_choices=True,
              required=False,
              default="vcf",
              show_default=True,
              help="Three accepted input types: vcf (for vcf/maf files), seg (for different segmentation files) and matrix (for mutational matrix)")
@click.option("--context_type",
              type=click.Choice([96, 288, 1536, "DINUC", "ID"]),
              metavar="INT/STRING",
              show_choices=True,
              required=False,
              default=96,
              show_default=True,
              help="Required context type if input_type is vcf. context_type takes which context type of the input data is considered for assignment")
@click.option("--collapse_to_SBS96", "collapse",
              type=click.Choice(['True', 'False']),
              metavar="BOOL",
              show_choices=True,
              required=False,
              default='True',
              show_default=True,
              help="By default sigantures are collapsed to SBS96 context. Use this option to disable the collapsing to SBS96 context if you are using other context types")
@click.option("--cosmic_version",
              type=click.Choice([1, 2, 3, 3.1, 3.2, 3.3, 3.4]),
              metavar="FLOAT",
              show_choices=True,
              required=False,
              default=3.4,
              show_default=True,
              help="Defines the version of the COSMIC reference signatures")
@click.option("--exome",
              type=click.BOOL,
              required=False,
              default=False,
              show_default=True,
              help="Defines if the exome renormalized COSMIC signatures will be used")
@click.option("--genome_build",
              type=click.Choice(["GRCh37", "GRCh38", "mm9", "mm10", "rn6"]),
              metavar="STRING",
              show_choices=True,
              required=False,
              default="GRCh37",
              show_default=True,
              help="The reference genome build, used for select the appropriate version of the COSMIC reference signatures, as well as processing the mutation calling file/s")
@click.option("--signature_database",
              type=click.Path(exists=True, file_okay=True),
              required=False,
              help="Path to the input set of known mutational signatures (only in case that COSMIC reference signatures are not used), a tab delimited file that contains the signature matrix where the rows are mutation types and columns are signature IDs")
@click.option("--export_probabilities",
              type=click.BOOL,
              required=False,
              default=True,
              show_default=True,
              help="Defines if the probability matrix per mutational context for all samples is created")
@click.option("--export_probabilities_per_mutation",
              type=click.BOOL,
              required=False,
              default=False,
              show_default=True,
              help="Defines if the probability matrices per mutation for all samples are created. Only available when input_type is vcf")
@click.option("--make_plots",
              type=click.BOOL,
              required=False,
              default=True,
              show_default=True,
              help="Toggle on and off for making and saving plots")
@click.option("--sample_reconstruction_plots",
              type=click.Choice(["pdf", "png", "both", None]),
              metavar="STRING",
              show_choices=True,
              required=False,
              default=None,
              show_default=True,
              help="Select the output format for sample reconstruction plots")
@click.option("--verbose",
              type=click.BOOL,
              required=False,
              default=False,
              show_default=True,
              help="	Prints detailed statements")
def sig_profiler_assignment(samples, output, input_type, context_type, collapse, cosmic_version, exome, genome_build, signature_database, export_probabilities, export_probabilities_per_mutation, make_plots, sample_reconstruction_plots, verbose):
    
    """
    Run SigProfilerAssignment
    """

    Analyze.cosmic_fit(samples, output, input_type=input_type,
                       context_type=str(context_type), collapse_to_SBS96=collapse, 
                       cosmic_version=cosmic_version, exome=exome, genome_build=genome_build, 
                       signature_database=signature_database, exclude_signature_subgroups=None,
                       export_probabilities=export_probabilities, export_probabilities_per_mutation=export_probabilities_per_mutation,
                       make_plots=make_plots, sample_reconstruction_plots=sample_reconstruction_plots,
                       verbose=verbose)
    
if __name__ == '__main__':
    sig_profiler_assignment()