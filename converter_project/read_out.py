import csv
import sqlite3


# Database connection and cursor
conn = sqlite3.connect('databases/converter_database.db')
c = conn.cursor()

# open and read CSV exported file
with open ("/home/andreas/Documents/Project/logger_str/converter_project/testpack.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    #lifts out name, set#, reps and weight.
    for line in csv_reader:
        add_list = []
        add_list.append(line[0])
        add_list.append(line[2])
        add_list.append(line[4])
        add_list.append(line[6])

        
        
        
        

        c.execute('''
        INSERT INTO workout (name, round, rep, weight)
        VALUES (?, ?, ?, ?)
        ''', add_list)
        conn.commit()

conn.close()
