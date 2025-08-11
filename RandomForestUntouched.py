import pandas as pd
import csv
from collections import defaultdict

print("Checking genotypeHolder function")

genotypesFile = "G:\\Shared drives\\csds456\\Project Midterm\\combined_output.csv" #wherever your genotypes file is located
phenotypesFile = "G:\\Shared drives\\csds456\\Project Midterm\\phenotypes_202503091344.csv" #wherever your phenotypes file is located

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
print("Cleaning up genotypes data efficiently...")
print(genotypes.head(10))
# Pivot the genotypes DataFrame so that each Filename is a row, and all SNPs (rsid, chromosome, position, genotype) are columns.
# We'll use a MultiIndex for columns: (rsid, chromosome, position, genotype)
genotypes_pivot = genotypes.pivot_table(
    index='Filename',
    columns=['rsid', 'chromosome', 'position'],
    values='genotype',
    aggfunc='first'
)
genotypes_pivot.reset_index(inplace=True)
print(genotypes_pivot.head(100))
print("Genotypes data reshaped so each Filename is a row, retaining all SNP data.")