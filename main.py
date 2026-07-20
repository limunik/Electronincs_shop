from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('postgresql://postgres:Limunik756900@localhost/electronics_store')

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Category(Base):
    __tablename__ = 'category'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)

    products = relationship("Product", back_populates="category")

class Product(Base):
    __tablename__ = 'product'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    
    category_id = Column(Integer, ForeignKey('category.id'))

    category = relationship("Category", back_populates="products")


def create_tables():
    Base.metadata.create_all(engine)


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
    return session.query(Product).all()

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
        session.delete(product)
        session.commit()
        print(f"the product was deleted")
    else:
        print(f"product was not found")