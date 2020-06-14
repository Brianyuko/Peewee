from peewee import *

sqlite_db = SqliteDatabase('student.db')


class Student(Model):
    name = CharField()
    email = CharField()

    class Meta:
        database = sqlite_db


sqlite_db.connect()
sqlite_db.create_tables([Student])

# Option One To Get Data
student1 = Student.get(Student.name == 'Huda')
print(student1)

# Option Two To Get Data
student2 = Student.get_by_id(5)
print(student2.email)

# Option Three To Get Data
student3 = Student[21]
print(student3.name)

# Option Four To Get Many Data
query = Student.select()
for student in query:
    print(student.name)
