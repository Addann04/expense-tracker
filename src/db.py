from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from datetime import date

Base = declarative_base()

class Expense(Base):
    __tablename__ = 'expenses'
    
    id = Column(Integer, primary_key=True)
    item_name = Column(String)
    item_type = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    date_of_purchase = Column(Date)  

DATABASE_URL = "sqlite:///expenses.db" 

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

def add_expense(item_name, item_type, quantity, price, date_of_purchase):
    session = Session()
    new_expense = Expense(
        item_name=item_name,
        item_type=item_type,
        quantity=quantity,
        price=price,
        date_of_purchase=date_of_purchase
    )
    session.add(new_expense)
    session.commit()
    session.close()

def get_expenses():
    session = Session()
    expenses = session.query(Expense).all()
    session.close()
    return expenses

def clear_expenses():
    session = Session()
    session.query(Expense).delete()
    session.commit()
    session.close()