from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from DB_setup import Restaurant, Base, MenuItem
 
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()


spinach = session.query(MenuItem).filter_by(name='Spinach Ice Cream').one()
session.delete(spinach)
session.commit()
