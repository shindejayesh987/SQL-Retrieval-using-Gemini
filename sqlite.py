import sqlite3

connection = sqlite3.connect("student.db")

#Creating cursor for inserting record and creating table
cursor = connection.cursor()

table_info="""
Create table STUDENTRECORDS(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25));
"""

cursor.execute(table_info)

#Insert some records

cursor.executemany('''INSERT INTO STUDENTRECORDS (NAME, CLASS, SECTION) VALUES (?, ?, ?)''', [
    ('Amit', 'ML', 'A'),
    ('Neha', 'DL', 'B'),
    ('Ravi', 'AI', 'C'),
    ('Sita', 'DS', 'A'),
    ('Manish', 'ML', 'B'),
    ('Priya', 'NLP', 'C'),
    ('Arjun', 'DL', 'A'),
    ('Komal', 'AI', 'B'),
    ('Ankit', 'ML', 'C'),
    ('Meena', 'NLP', 'A'),
    ('Rahul', 'DS', 'B'),
    ('Naina', 'ML', 'A'),
    ('Karan', 'DL', 'C'),
    ('Simran', 'AI', 'A'),
    ('Deepak', 'NLP', 'B')
])



#Display records

print("The inserted records are")

data=cursor.execute('''Select * from STUDENTRECORDS''')
for row in data:
    print(row)



connection.commit()
connection.close()
