#!/usr/bin/python3
""" defines class DBStorage """

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import MetaData, create_engine
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os


class DBStorage:
    """ defines database called DBStorage """

    __engine = None
    __session = None

    def __init__(self):
        """ initialization of  DBStorage """
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(user, pswd, host, db),
                                      pool_pre_ping=True)
        Base.metadata.create_all(self._engine)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """  must return a dictionary: (like FileStorage)
            all elements in database """
        database_dic = {}
        if cls:
            objects = self.__session.query(cls).all()
            for objs in objects:
                key = "{}.{}".format(type(objs).__name__, objs.id)
                database_dic[key] = objs
       
        else:
            for objs in self.__session.query(City, State, User,\
                                             Place, Review, Amenity).all():
                key = "{}.{}".format(type(objs).__name__, objs.id)
                database_dic[key] = objs
        return database_dic
            
    def new(self obj):
        """ adds the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """ * create all tables in the database (feature\
             of SQLAlchemy) (WARNING: all classes who \
             inherit from Base must be imported before \
             calling Base.metadata.create_all(engine))
            * create the current database session\
             (self.__session) from the engine\
            (self.__engine) by using a \
            sessionmaker - the option expire_on_commit \
            must be set to False ; and scoped_session - \
            to make sure your Session is thread-safe"""

            Base.metadata.create_all(self._engine)
            session = sessionmaker(bind=self.__engine,
                                   expire_on_commit=False)
            Session = scoped_session(session)
            self.__session = Session()

    def close(self):
        """ closes the current session """
        self.__session.close()


