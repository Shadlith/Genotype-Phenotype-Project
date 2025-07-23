import pypyodbc
import pandas as pd
import csv
import tensorflow as tf

print("Initial Commit to check this is working")

def pheotypeHolder(file, phenotypes):
    
    with open(file, 'r', encoding="utf8") as f:
        reader = csv.reader(f)
        for row in reader:
            phenotypes.append(row)
    return phenotypes


def genotypeHolder(file, genotypes):
    with open(file, 'r', encoding="utf8") as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            # Skip header lines
            if row[0].startswith("#"):
                continue
            # Append genotype data to the list
            if len(row) > 1:
                genotypes.append(row)
    return genotypes


def connect_to_database(server, database, username, password):
    try:
        connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        conn = pypyodbc.connect(connection_string)
        print("Connection successful")
        return conn
    except pypyodbc.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def push_to_database(database, table_name, csvfile, start=0, end=None):
    cursor = database.cursor()
    cursor.execute(f"""
        IF OBJECT_ID(N'{table_name}', N'U') IS NULL
        CREATE TABLE {table_name} (
            Filename NVARCHAR(255) NULL,
            rsid NVARCHAR(50) NULL,
            chromosome NVARCHAR(10) NULL,
            position NVARCHAR(50) NULL,
            genotype NVARCHAR(255) NULL
        )
    """)
    #cursor.execute(f"DELETE FROM {table_name}")  # Clear existing data
    with open(csvfile, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        next(reader)
        for i, row in enumerate(reader):
            if i < start:
                continue
            if end is not None and i >= end:
                break
            #print(f"Inserting row {i}: {row}")
            cursor.execute(f"INSERT INTO {table_name} (Filename, rsid, chromosome, position, genotype) VALUES (?, ?, ?, ?, ?)", row)
            if i%100 == 0:
                print(f"Inserted {i} rows so far...")
                database.commit()
    df = pd.read_sql(f"SELECT * FROM {table_name}", database)
    print(df.head())

database = connect_to_database("2.tcp.us-cal-1.ngrok.io,11916", "OpenSNPDB", "shadlith", "Pingity!")
#num_lines = sum(1 for _ in open('C:\College\Masters Semster 5\Privacy\opensnp_datadump.current\combined_output.csv'))
#print(f"{num_lines} in file combined_output.csv")
#push_to_database_bulk_version(database, "GenotypeData", "C:\College\Masters Semster 5\Privacy\opensnp_datadump.current\combined_output.csv")
#push_to_database(database, "GenotypeData", "C:\College\Masters Semster 5\Privacy\opensnp_datadump.current\combined_output.csv", start=0)
#phenotypes = pheotypeHolder('Data Samples\\phenotypes_202503091344.csv', [])
#genotypes = genotypeHolder('Data Samples\\user1_file9_yearofbirth_1985_sex_XY.23andme.txt', [])

##print("Phenotypes:", pheonotypes)
#print("Genotypes:", genotypes[0:3])

#print(tf.reduce_sum(tf.random.normal([1000, 1000])))


