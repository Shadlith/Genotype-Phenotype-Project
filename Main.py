import csv

print("Initial Commit to check this is working")

pheonotypes = []
with open('Data Samples\phenotypes_202503091344.csv', 'r', encoding="utf8") as file:
    reader = csv.reader(file)
    for row in reader:
        pheonotypes.append(row)

genotypes = []
with open('Data Samples\\user1_file9_yearofbirth_1985_sex_XY.23andme.txt', 'r', encoding="utf8") as file:
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        # Skip header lines
        if row[0].startswith("#"):
            continue
        # Append genotype data to the list
        if len(row) > 1:
            genotypes.append(row)
        
##print("Phenotypes:", pheonotypes)
print("Genotypes:", genotypes[0:3])