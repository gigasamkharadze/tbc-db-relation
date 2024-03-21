## Relations in the database

### Description
The repository contains a database of relations between students and
advisors. Initially, the database is empty. 
The database is created and filled with data by the `main.py` script.

In the beginning, the relation was a one-to-many relation.
A student can have only one advisor, but an advisor can have many students.

Then, the relation was changed to a many-to-many relation.
A student can have many advisors, and an advisor can have many students.

### Implementation details
The database is implemented using SQLite. The database is created and filled with data by the `main.py` script.
The database had two tables: `students` and `advisors`.
To implement the many-to-many relation, the `enrollment` table was added representing the relation between students and advisors.

```SQL
CREATE TABLE Advisor(
AdvisorID INTEGER NOT NULL,
AdvisorName TEXT NOT NULL,
PRIMARY KEY(AdvisorID)
);
```

```SQL
CREATE TABLE Student(
StudentID NUMERIC NOT NULL,
StudentName NUMERIC NOT NULL,
AdvisorID INTEGER,
FOREIGN KEY(AdvisorID) REFERENCES Advisor(AdvisorID),
PRIMARY KEY(StudentID)
);
```

```SQL
CREATE TABLE Enrollment(
StudentID NUMERIC NOT NULL,
AdvisorID INTEGER NOT NULL,
FOREIGN KEY(StudentID) REFERENCES Student(StudentID),
FOREIGN KEY(AdvisorID) REFERENCES Advisor(AdvisorID),
PRIMARY KEY(StudentID, AdvisorID)
);
```

### Requirements
The `main.py` script requires the `sqlite3` module to be installed.
The `sqlite3` module is included in the Python standard library.
Thus, no additional installation is required.