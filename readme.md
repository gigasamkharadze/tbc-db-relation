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
The database has two tables: `students` and `advisors`.
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

Here, the primary key constraint is used to ensure that
the `studentID` is unique in the `students` table.

To obtain the many-to-many relation, we simpy change
primary key constraint to unique constraint in the `students` table.
```SQL
CREATE TABLE Student(
StudentID NUMERIC NOT NULL,
StudentName NUMERIC NOT NULL,
AdvisorID INTEGER,
FOREIGN KEY(AdvisorID) REFERENCES Advisor(AdvisorID),
PRIMARY KEY(StudentID, AdvisorID)
);
```

### Requirements
The `main.py` script requires the `sqlite3` module to be installed.
The `sqlite3` module is included in the Python standard library.
Thus, no additional installation is required.