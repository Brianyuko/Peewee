from peewee import *

sqlite_db = SqliteDatabase('student.db')


class Student(Model):
    name = CharField()
    email = CharField()

    class Meta:
        database = sqlite_db


sqlite_db.connect()

# Don't Forget To Looping
# Filter Records Option One
students = Student.select().where(Student.name == 'Dandy Arisandy')
for student in students:
    print(student.name)

# Filter Records Option Two
students1 = Student.select().where(Student.name.contains('Pujianto'))
for student1 in students1:
    print(student1.name)
