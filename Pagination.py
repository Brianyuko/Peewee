from peewee import *

sqlite_db = SqliteDatabase('student.db')


class Student(Model):
    name = CharField()
    email = CharField()

    class Meta:
        database = sqlite_db


sqlite_db.connect()

# Count
print(Student.select().count())

# Limit
students = Student.select().limit(5)
for student in students:
    print(student.name)

# Pagination
# Paginate (page, item per page)
students1 = Student.select().paginate(1, 5)
for student1 in students1:
    print(student1.name)
