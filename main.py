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

CREATE TABLE Enrollment(
StudentID NUMERIC NOT NULL,
AdvisorID INTEGER NOT NULL,
FOREIGN KEY(StudentID) REFERENCES Student(StudentID),
FOREIGN KEY(AdvisorID) REFERENCES Advisor(AdvisorID),
PRIMARY KEY(StudentID, AdvisorID)
);

INSERT INTO Advisor(AdvisorID, AdvisorName) VALUES
(1,"John Paul"),
(2,"Anthony Roy"),
(3,"Raj Shetty"),
(4,"Sam Reeds"),
(5,"Arthur Clintwood");

INSERT INTO Student(StudentID, StudentName) VALUES
(1,"John"),
(2,"Paul"),
(3,"Anthony"),
(4,"Raj"),
(5,"Sam"),
(6,"Arthur");

INSERT INTO Enrollment(StudentID, AdvisorID) VALUES
(1,1),
(1,2),
(1,3),
(2,1),
(2,2),
(2,3),
(3,1),
(3,2),
(4,3),
(4,4),
(5,4),
(5,5),
(6,5);
''')

# advisors with the amount of students they have
cursor.execute("""
SELECT AdvisorName, COUNT(StudentID) FROM Enrollment
JOIN Advisor ON Advisor.AdvisorID = Enrollment.AdvisorID
GROUP BY Advisor.AdvisorID;
""")
print(cursor.fetchall())

conn.commit()
conn.close()
