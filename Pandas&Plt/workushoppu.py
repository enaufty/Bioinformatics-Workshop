import pandas as pd
#import matplotlib.pyplot as plt
pd.set_option('display.max_colwidth', None)
annotation_df = pd.read_tableannotation_df = pd.read_table('schistosoma_mansoni.PRJEA36577.WBPS11.annotations.gff3',
                                                            names = ['SeqID', 'Source', 'Type', 'Start', 'End', 'Score', 'Strand', 'Phase', 'Attributes'],
                                                            comment='#')
annotation_df.head(1)
exons_df = annotation_df[annotation_df['Type']=='exon']
exons_df[['SeqID', 'Start', 'End', 'Strand', 'Attributes']].head(3)
exons_df = exons_df.reset_index(drop=True)
print(exons_df.head(5))