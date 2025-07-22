import csv
import tensorflow as tf

print("Initial Commit to check this is working")

def pheotypeHolder(file, phenotypes):
    
    with open('Data Samples\phenotypes_202503091344.csv', 'r', encoding="utf8") as file:
        reader = csv.reader(file)
        for row in reader:
            phenotypes.append(row)
    return phenotypes


def genotypeHolder(file, genotypes):
    with open('Data Samples\\user1_file9_yearofbirth_1985_sex_XY.23andme.txt', 'r', encoding="utf8") as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            # Skip header lines
            if row[0].startswith("#"):
                continue
            # Append genotype data to the list
            if len(row) > 1:
                genotypes.append(row)
    return genotypes


phenotypes = pheotypeHolder('Data Samples\\phenotypes_202503091344.csv', [])
genotypes = genotypeHolder('Data Samples\\user1_file9_yearofbirth_1985_sex_XY.23andme.txt', [])

##print("Phenotypes:", pheonotypes)
print("Genotypes:", genotypes[0:3])

print(tf.reduce_sum(tf.random.normal([1000, 1000])))