import pyodbc

try:
    connect =  pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\LANDON\Desktop\Database01.accdb;')
    print("Database is connected")

    database = connect.cursor()
    database.execute('''
                    INSERT INTO Table1 (ID, FullName, Age, SemGrade, Address)
                    VALUES
                    (11,'Landon S. Lorica', 19, 90, 'Cavite')
                    ''')
    database.commit()

    print("Data Added")

except pyodbc.Error:
    print("Error in Connection")
