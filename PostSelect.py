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


# Option One
query = Post.select().join(User).where(User.username == 'Chris')
for post in query:
    print(post.posting)

# Option Two
bellaPost = User.get(User.username == 'Bella')
for post in bellaPost.posts:
    print(post.posting)

# Print with DatePost
datePost = Post.select().order_by(Post.create_date)
for post in datePost:
    print(post.posting + ' ' + str(post.create_date))