import pandas as pd

print("Checking genotypeHolder function")

genotypesFile = "C:\College\Masters Semster 5\Privacy\opensnp_datadump.current\combined_output.csv" #wherever your genotypes file is located
phenotypesFile = "C:\College\Masters Semster 5\Privacy\Genotype-Phenotype-Project\Data Samples\phenotypes_202503091344.csv" #wherever your phenotypes file is located

#genotypes = pd.read_csv(genotypesFile, encoding='utf-8', header=0)
phenotypes = pd.read_csv(phenotypesFile, encoding='utf-8', header=0, sep=';')
#print(genotypes.head())
print(phenotypes.head())
for col in phenotypes.columns:
    print(col)


