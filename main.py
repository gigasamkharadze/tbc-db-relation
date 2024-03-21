import sqlite3

conn = sqlite3.connect('sqlite3.db')
cursor = conn.cursor()

cursor.executescript('''
CREATE TABLE Advisor(
AdvisorID INTEGER NOT NULL,
AdvisorName TEXT NOT NULL,
PRIMARY KEY(AdvisorID)
);

CREATE TABLE Student(
StudentID NUMERIC NOT NULL,
StudentName NUMERIC NOT NULL,
AdvisorID INTEGER,
FOREIGN KEY(AdvisorID) REFERENCES Advisor(AdvisorID),
PRIMARY KEY(StudentID, AdvisorID)
);

INSERT INTO Advisor(AdvisorID, AdvisorName) VALUES
(1,"John Paul"),
(2,"Anthony Roy"),
(3,"Raj Shetty"),
(4,"Sam Reeds"),
(5,"Arthur Clintwood");

INSERT INTO Student(StudentID, StudentName, AdvisorID) VALUES
(1,"John Doe",1),
(2,"Jane Doe",1),
(3,"John Smith",2),
(4,"Jane Smith",2),
(5,"John Johnson",3),
(6,"Jane Johnson",3),
(7,"John Williams",4),
(8,"Jane Williams",4),
(9,"John Brown",5),
(10,"Jane Brown",5),
(11,"John Paul",1),
(12,"Jane Paul",1),
(13,"John Roy",2),
(14,"Jane Roy",2),
(15,"John Shetty",3),
(16,"Jane Shetty",3),
(17,"John Reeds",4),
(18,"Jane Reeds",4),
(19,"John Clintwood",5),
(20,"Jane Clintwood",5),
(21,"Luka Doe",1),
(22,"Buka Doe",1);
''')

cursor.execute('''
SELECT AdvisorName, COUNT(StudentID) FROM Advisor
JOIN Student ON Advisor.AdvisorID = Student.AdvisorID
GROUP BY AdvisorName
ORDER BY COUNT(StudentID) ASC;
''')
print(cursor.fetchall())

conn.commit()
conn.close()
