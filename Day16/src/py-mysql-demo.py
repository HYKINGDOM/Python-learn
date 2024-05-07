import random
import string
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'sys_user'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    nick_name = Column(String)
    email = Column(String)


def random_email():
    characters = string.ascii_letters + string.digits
    random_email = ''.join(random.choices(characters, k=10)) + '@example.com'
    return random_email


# 创建数据库连接
engine = create_engine('mysql+mysqlconnector://root:root@localhost/ry-vue')

# 创建所有表
Base.metadata.create_all(engine)

# 创建Session类
Session = sessionmaker(bind=engine)

# 创建Session实例
session = Session()

# 添加新用户
new_user = User(user_name='John', nick_name='John Doe', email='john@example.com')
session.add(new_user)
session.commit()

# 查询用户
users = session.query(User).filter_by(user_name='John').all()
for user in users:
    print("First Query: ", user.user_id, user.user_name, user.nick_name, user.email)

users_to_update = session.query(User).filter_by(user_name='John')
for user in users_to_update:
    user.email = random_email()

# 提交事务
session.commit()

# 查询用户
users = session.query(User).filter_by(user_name='John').all()
for user in users:
    print("Second Query: ", user.user_id, user.user_name, user.nick_name, user.email)

# 关闭Session
session.close()

# 关闭Session
session.close()
