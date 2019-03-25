from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DB_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

# Create a link of communication between code exe and engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
### syntax
# newEntry = ClassName(property="value", ...)
#session.add(newEntry)
#session.commit()
#myFirstRestaurant = Restaurant(name = 'Pizza Hot')
#session.add(myFirstRestaurant)
#session.commit()

#Asking session to go into db, find table that
# Corresponds to the restaurant class in tables
# and return them in a list
print(session.query(Restaurant).all())

#cheesepizza = MenuItem(name = 'Cheese Pizza', 
    #description = 'Made with all nature ingredients and fresh mozzarella',
    #course = 'Entree', price = '$8.99',
    #restaurant = myFirstRestaurant
    #)
#session.add(cheesepizza)
#session.commit()
print(session.query(MenuItem).all())
firstResult = session.query(Restaurant).first()
print(firstResult.name)

