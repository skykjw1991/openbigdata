import csv
import sqlite3
import sys



create_table= """create table if not exists Suppliers
                (Supplier_Name VARCHAR(20),
                Invoice_Number VARCHAR(20),
                Part_Number VARCHAR(20),
                Cost FLOAT,
                Purchase_Date DATE);"""
