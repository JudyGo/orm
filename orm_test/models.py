from sqlalchemy import Column, String, create_engine, CHAR, Integer, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from time import strftime, gmtime

# declarative_base() 创建了一个 BaseModel 类，这个类的子类可以自动与一个表关联。
db = declarative_base()
# 链接数据库返回一个db对象
enging = create_engine('mysql+pymysql://root:666666@172.17.78.236:3306/testss', echo=True)

# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'


# 生成数据库会话类
DBSession = sessionmaker(bind=enging)
session = DBSession()


class User(db):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    email = Column(String(200), unique=True)
    password = Column(String(32), nullable=True)
    telephone = Column(Integer)
    info = Column(String(255))
    create_at = Column(DateTime, nullable=False, default=strftime("%Y-%m-%d %H:%M:%S", gmtime()))

    def __init__(self):
        pass


    def add_user(self):
        error = None
        try:
            db.DBSession.add(self)
            db.DBSession.commit()
        except Exception as err:
            db.DBSession.rollback()
            error = str(err)
        finally:
            return error


    def delete_user(self, id):
        error = None
        try:
            user = self.query.get(id)
            if user:
                db.DBSession.delete(user)
                db.DBSession.commit()
            else:
                error = "用户不存在，请输入正确的用户"
        except Exception as err:
            db.DBSession.rollback()
            error = str(err)
        finally:
            return error


    def update_user(self, id, name):
        error = None
        try:
            user = self.query.get(id)
            if user:
                user.name = name
                db.DBSession.add(user)
                db.DBSession.commit()
            else:
                error = "用户不存在，请输入正确的用户"
        except Exception as err:
            db.DBSession.rollback()
            error = str(err)
        finally:
            return error


    @classmethod
    def get_user(self, id=None):
        error = None
        user_value = None
        try:
            if id is not None:
                user = self.query.filter(id=id).first()
            else:
                user = self.query.all()
            if user:
                user_value = user
            else:
                error = "用户不存在，请输入正确的用户"
        except Exception as err:
            db.DBSession.rollback()
            error = str(err)
        finally:
            return error, user_value




