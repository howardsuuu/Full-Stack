from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from DB_setup import Restaurant, Base, MenuItem
 
engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

#print(session.query(Restaurant).all())\
#items = session.query(MenuItem).all()
#for item in items:
    #print(item.name)
veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
for veggieBurger in veggieBurgers:
    print(veggieBurger.id, veggieBurger.price, veggieBurger.restaurant.name, '\n')

# use .one() to make sure DB only gives one object instead of list
UrbanVeggieBurger = session.query(MenuItem).filter_by(id = 2).one()
print(UrbanVeggieBurger.price)
UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit()

veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
for veggieBurger in veggieBurgers:
    print(veggieBurger.id, veggieBurger.price, veggieBurger.restaurant.name, '\n')

for veggieBurger in veggieBurgers:
    if veggieBurger.price != '$2.99':
        veggieBurger.price = '$2.99'
        session.add(veggieBurger)
        session.commit()
veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
for veggieBurger in veggieBurgers:
    print(veggieBurger.id, veggieBurger.price, veggieBurger.restaurant.name, '\n')
session.rollback()
