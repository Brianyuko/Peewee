import datetime
from peewee import *

sqlite_db = SqliteDatabase('post.db')


class BaseModel(Model):
    class Meta:
        database = sqlite_db


class User(BaseModel):
    username = CharField(unique=True)


class Post(BaseModel):
    # ForeignKey (posts), Are Connected To Each User
    user = ForeignKeyField(User, backref='posts')
    posting = TextField()
    create_date = DateTimeField(default=datetime.datetime.now())


sqlite_db.create_tables([User, Post])
data = (
    ('Bella', ('Posting apa ya', 'Gatau aku')),
    ('Chris', ('Kok tanya aku', 'coba tanya dia')),
    ('Peter', ('lah kok tanya aku', 'tanya ke google aja')),
)

# Insert Database
for username, posts in data:
    user = User.create(username=username)
    for post in posts:
        Post.create(user=user, posting=post)
