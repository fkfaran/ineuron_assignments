import sqlite3

# Connect to SQLite (or create DB)
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# 1. Create student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    rollno INTEGER PRIMARY KEY,
    name TEXT,
    course TEXT
)
""")
print("1. Student table created.")

# 2. Insert 4 student records
students = [
    (1, "Alice", "Python"),
    (2, "Bob", "Java"),
    (3, "Charlie", "C++"),
    (4, "David", "Python")
]
cursor.executemany("INSERT OR REPLACE INTO student VALUES (?, ?, ?)", students)
conn.commit()
print("2. Inserted 4 student records.")

# 3. Select all students
cursor.execute("SELECT * FROM student")
print("3. All students:")
for row in cursor.fetchall():
    print(row)

# 4. Update student name of rollno 3
cursor.execute("UPDATE student SET name = 'Mohan' WHERE rollno = 3")
conn.commit()
print("4. Updated rollno 3 name to Mohan.")

# 5. Delete a student with rollno 2
cursor.execute("DELETE FROM student WHERE rollno = 2")
conn.commit()
print("5. Deleted student with rollno 2.")

# 6. Delete all data from student table
# cursor.execute("DELETE FROM student")
# conn.commit()
# print("6. Deleted all data from student table.")

# 7. Drop student table
# cursor.execute("DROP TABLE student")
# conn.commit()
# print("7. Dropped student table.")

# 8. Create Courses table and Student table with foreign key
cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    cid INTEGER PRIMARY KEY,
    cname TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    rollno INTEGER PRIMARY KEY,
    name TEXT,
    cid INTEGER,
    FOREIGN KEY (cid) REFERENCES courses(cid)
)
""")
print("8. Courses and Student tables created with foreign key.")

# 9. Insert data in both tables
courses = [
    (1, "Python"),
    (2, "Java"),
    (3, "C++")
]
students = [
    (1, "Alice", 1),
    (2, "Bob", 2),
    (3, "Mohan", 3),
    (4, "David", 1)
]
cursor.executemany("INSERT OR REPLACE INTO courses VALUES (?, ?)", courses)
cursor.executemany("INSERT OR REPLACE INTO student VALUES (?, ?, ?)", students)
conn.commit()
print("9. Inserted data into Courses and Student tables.")

# 10. Select all students who are doing Python course
cursor.execute("""
SELECT s.rollno, s.name, c.cname
FROM student s
JOIN courses c ON s.cid = c.cid
WHERE c.cname = 'Python'
""")
print("10. Students enrolled in Python course:")
for row in cursor.fetchall():
    print(row)

# Close connection
conn.close()
