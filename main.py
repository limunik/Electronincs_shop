import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, func
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


load_dotenv()


db_password = os.getenv("DB_PASSWORD")

engine = create_engine(f"postgresql://postgres:{db_password}@localhost/courcces")

Base = declarative_base()


class   Category(Base):
    __tablename__ = 'category'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)

class   Product(Base):
    __tablename__ = 'product'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    category_id = Column(Integer)

   

def create_tables():
    Base.metadata.create_all(engine)

    
Session = sessionmaker(bind=engine)

session = Session()

def add_category(name):
    category = Category(name=name)
    session.add(category)
    session.commit()
    print(f"category was added {category}")
    return category

def get_categories():
    return session.query(Category).all()

def update_category(category_id, new_name):
    category = session.get(Category, category_id)
    if category:
        category.name = new_name
        session.commit()
        print(f"category was updated")
    else:
        print(f"category was not found")
    return category
def delete_category(category_id):
    category = session.get(Category, category_id)
    if category:
        session.delete(category)
        print(f"category was deleted")
    else:
        print(f"this category was not found")

# ==================================================================== #

def add_product(name, price, quantity, category_id):
    product = Product(name = name, price = price, quantity = quantity, category_id = category_id)
    session.add(product)
    session.commit()
    print(f"the product has been added")
    return product

def get_products():
    return session.query().all()

def update_product(product_id = None, name= None, price= None, quantity= None, category_id= None):
    product = session.get(Product, product_id)
    if not product:
        print(f"product was not found")
    return None

    if name is not None:
        product.name = name
    if price is not None:
        product.price = price
    if quantity is not None:
        product.quantity = quantity
    if category_id is not None:
        product.category_id = category_id

    session.commit()
    print(f"product was updated")
    return product

def delete_product(product_id):
    product = session.get(Product, product_id)
    if product:
        product.delete(product)
        session.commit()
        print(f"the product was deleted")
    else:
        print(f"product was not found")