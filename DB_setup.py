import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# telling we are connecting between code and db
from sqlalchemy import create_engine

# Let SqlAlchemy know our classes
# are special SQLAlchemy classes that correspond to
# tables in DB
Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'
    
    name = Column(
        String(80), nullable = False
    )
    id = Column(
        Integer, primary_key = True
    )

class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(
        String(80), nullable = False
    )
    id = Column(
        Integer, primary_key = True
    )
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    
    #Create foreign relation between two tables
    restaurant_id = Column(
        Integer, ForeignKey('restaurant.id')#look inside the restaurant table
    )
    restaurant = relationship(Restaurant)

##### insert at end of file #####

# Telling our code, the path for connecting to db
# point to the db we want to use
engine = create_engine(
    'sqlite:///restaurantmenu.db'
)
# Create DB table
Base.metadata.create_all(engine)


