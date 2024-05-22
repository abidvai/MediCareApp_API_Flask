import sqlite3
import random
import uuid
from datetime import date


def createTables():
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()

    # create table user
    cursor.execute('''
CREATE TABLE IF NOT EXISTS User (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_id varchar(255),
                   password varchar(255),
                   level INT,
                   DateOfAccountCreation DATE,
                   approved boolean,
                   Block boolean,
                   name varchar(255),
                   address varchar(255),
                   email varchar(255),
                   phone varchar(255),
                   PinCode varchar(255)
);

''')
    
    # create table products
    
    cursor.execute('''
CREATE TABLE IF NOT EXISTS Products (
                   Product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name VARCHAR(255),
                   price FLOAT,
                   category VARCHAR(255),
                   stock INTEGER,
                   isActive BOOLEAN
);

''')

    
    conn.commit()
    conn.close()



def createUser(name, password, Address, Email, Phone, PinCode):
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()
    user_id = str(uuid.uuid4())
    dateOfCreation = date.today()
    createUser = cursor.execute("""
INSERT INTO User (id,user_id, password, level, DateOfAccountCreation, approved, Block, name, address, email, phone, Pincode)
VALUES
(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""",(None, user_id, password, -1, dateOfCreation, 0, 0, name, Address, Email, Phone, PinCode)
)
    conn.commit()
    conn.close()
    return True
