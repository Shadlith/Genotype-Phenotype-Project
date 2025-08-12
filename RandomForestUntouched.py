import pandas as pd
import csv
from collections import defaultdict
import tensorflow as tf
import sklearn
import re

print("Checking genotypeHolder function")

genotypesFile = "C:\\College\\Masters Semster 5\\Privacy\\opensnp_datadump.current\\combined_output.csv" #wherever your genotypes file is located
phenotypesFile = "C:\\College\\Masters Semster 5\\Privacy\\Genotype-Phenotype-Project\\Data Samples\\phenotypes_202503091344.csv" #wherever your phenotypes file is located

print("Importing genotypes and phenotypes...")

genotypes = pd.read_csv(genotypesFile, low_memory=False, sep=',')
print("Genotypes imported successfully.")
phenotypes = pd.read_csv(phenotypesFile, encoding='utf-8', header=0, sep=';')
print("Phenotypes imported successfully.")
phenotypes = phenotypes[['user_id', 'genotype_filename', 'date_of_birth', 'chrom_sex', 'Eye color', 'white skin', 'Beard Color', 'Hair Color', 'Sex',
                         'ethnicity', 'Ancestry', 'Dyslexia', 'Jewish Ancestry', 'Birth year', 'Weight', 'Autism', 'eye colour', 'Black', 'Blood Type',
                         'Favorite Color/Colour', 'black skin', 'dark Blonde', 'blood type', 'Skintype', 'Hair color', 'hair colour', 'Red Hair', 'african-northern european', 
                         'brunette', 'Nationality', 'Hair colour', 'Eye Color', 'Physical', 'black', 'Alcoholism', 'Mother\'s eye color', 'Latino Ancestry', 'hair color', 'Scottish Ancestry',
                         'Welsh Ancestry', 'Caffeine dependence', 'Medium brown skin', 'Hazel Eyes', 'Extra Teeth', 'Eye Color - Heterochromia', 'Skin color.', 'Brown hair, Hazel, Caucasian.', 
                         'black hair and brown eyes, blood B+, 6,5 tall', 'blood compatibility for transfussion', 'Blue eyes', 'Eye', 'Skin color']]
print("Created phenotypes dataframe with selected columns.")

# Function to extract userX_fileY from genotype_filename in phenotypes
def extract_user_file_from_phenotype(geno_filename):
    match = re.match(r'(\d+)\.[^\.]*\.(\d+)', str(geno_filename))
    if match:
        return f"user{match.group(1)}_file{match.group(2)}"
    return geno_filename

phenotypes['genotype_filename'] = phenotypes['genotype_filename'].apply(extract_user_file_from_phenotype)
print(phenotypes.head(10))
print("Cleaning up genotypes data efficiently...")
print(genotypes.count(0))
print(genotypes.head(10))
# Pivot the genotypes DataFrame so that each Filename is a row, and all SNPs (rsid, chromosome, position, genotype) are columns.
# We'll use a MultiIndex for columns: (rsid, chromosome, position, genotype)
# Create a single-level column index by combining rsid, chromosome, and position into a tuple
genotypes['snp_tuple'] = list(zip(genotypes['rsid'], genotypes['chromosome'], genotypes['position']))
genotypes_pivot = genotypes.pivot_table(
    index='Filename',
    columns='snp_tuple',
    values='genotype',
    aggfunc='first'
)
genotypes_pivot.reset_index(inplace=True)
percent_kept = 0.5 #Percent of values that have to be non-NA for the column to be kept
genotypes_pivot.dropna(axis=1, thresh=percent_kept * len(genotypes_pivot), inplace=True)  
# Function to extract userX_fileY from the genotypes_pivot index
def extract_user_file(filename):
    match = re.match(r'(user\d+_file\d+)', str(filename))
    return match.group(1) if match else filename

# Apply to genotypes_pivot['Filename']
genotypes_pivot['Filename'] = genotypes_pivot['Filename'].apply(extract_user_file)


print("Genotypes data reshaped so each Filename is a row, retaining all SNP data.")
print(f"Number of rows in genotypes_pivot: {len(genotypes_pivot)}")
print(f"Number of columns in genotypes_pivot: {genotypes_pivot.shape[1]}")
print(genotypes_pivot.head(100))
print("Genotypes data reshaped so each Filename is a row, retaining all SNP data.")

merged_data = pd.merge(phenotypes, genotypes_pivot, left_on='genotype_filename', right_on='Filename', how='right')
print("Merged phenotypes and genotypes data successfully.")
print(f"Number of rows in merged_data: {len(merged_data)}")
print(merged_data.head(10))
print(merged_data.columns)
