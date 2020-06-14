from peewee import *

sqlite_db = SqliteDatabase('student.db')


class Student(Model):
    name = CharField()
    email = CharField()

    class Meta:
        database = sqlite_db


sqlite_db.connect()
sqlite_db.create_tables([Student])
# safe = true -> Automatically

# Insert Data
# Option One
Student.create(name='Dandy Arisandy', email='dandy@gmail.com')
Student.create(name='Erwin Pujianto', email='erwin@gmail.com')

# Option Two
student = Student(name='Jallue', email='jalue@gmail.com')
# student Will Return Primary Key
student.save()

# Option Three
Student.insert(name='angga', email='angga@gmail.com').execute()
# Option Three Will Return Primary Key

# Option Four
dataStudent = [
    {'name': 'Andhika', 'email': 'andhika@gmail.com'},
    {'name': 'Andi', 'email': 'andi@gmail.com'},
]

# Option Five
fields = [Student.name, Student.email]
data = [
    ('Alan', 'alan@gmail.com'),
    ('Huda', 'huda@gmail.com')
]

Student.insert_many(data, fields=fields).execute()
