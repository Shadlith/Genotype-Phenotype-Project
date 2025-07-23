import pandas as pd

print("Checking genotypeHolder function")

genotypesFile = "C:\College\Masters Semster 5\Privacy\opensnp_datadump.current\combined_output.csv" #wherever your genotypes file is located
phenotypesFile = "C:\College\Masters Semster 5\Privacy\Genotype-Phenotype-Project\Data Samples\phenotypes_202503091344.csv" #wherever your phenotypes file is located

#genotypes = pd.read_csv(genotypesFile, encoding='utf-8', header=0)
phenotypes = pd.read_csv(phenotypesFile, encoding='utf-8', header=0, sep=';')
phenotypes = phenotypes[['user_id', 'genotype_filename', 'date_of_birth', 'chrom_sex', 'Eye color', 'white skin', 'Beard Color', 'Hair Color', 'Sex',
                         'ethnicity', 'Ancestry', 'Dyslexia', 'Jewish Ancestry', 'Birth year', 'Weight', 'Autism', 'eye colour', 'Black', 'Blood Type',
                         'Favorite Color/Colour', 'black skin', 'dark Blonde', 'blood type', 'Skintype', 'Hair color', 'hair colour', 'Red Hair', 'african-northern european', 
                         'brunette', 'Nationality', 'Hair colour', 'Eye Color', 'Physical', 'black', 'Alcoholism', 'Mother\'s eye color', 'Latino Ancestry', 'hair color', 'Scottish Ancestry',
                         'Welsh Ancestry', 'Caffeine dependence', 'Medium brown skin', 'Hazel Eyes', 'Extra Teeth', 'Eye Color - Heterochromia', 'Skin color.', 'Brown hair, Hazel, Caucasian.', 
                         'black hair and brown eyes, blood B+, 6,5 tall', 'blood compatibility for transfussion', 'Blue eyes', 'Eye', 'Skin color']]
#print(genotypes.head())
print(phenotypes.head())
for col in phenotypes.columns:
    print(col)