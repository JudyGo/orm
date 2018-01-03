# from sqlalchemy import Column, String, create_engine, CHAR, Integer
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
#
# Base = declarative_base()
#
#
# class User(Base):
#     __tablename__ = "user"
#     id = Column(Integer, primary_key=True)
#     nameuser = Column(String(200), unique=True)
#     undergraduate = Column(String(250))
#     graduatestudent = Column(String(100))
#     international_ratio = Column(String(250))
#     teacher_student = Column(String(100))
#     url = Column(String(250))
#     address = Column(String(100))
#
#
# engine = create_engine(
#     "mysql+pymysql://root:666666@172.18.0.1:3306/mypydb")
# Base.metadata.create_all(engine)
# DBSession = sessionmaker(bind=engine)
#
#
#
# session =DBSession()
#
# obj=User(nameuser="sss")
# session.add(obj)
# session.commit()



import pymysql


pymysql.connect(db='center', user='bnu', passwd='bnu', host='172.16.160.203', port=3306)