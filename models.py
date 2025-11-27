from sqlmodel import SQLModel, Field
from connection import create_tables

class Users2(SQLModel, table= True):
    id : int= Field(primary_key = True)
    username: str
    password: str


class Employee(SQLModel, table = True):
    id : int = Field(primary_key = True)
    employee_name: str
    employee_email : str
    employee_phoneno : int
    employee_age : int



class Books(SQLModel, table = True):
    id : int = Field(primary_key = True)
    book_name : str
    book_author : str
    book_year : int
    sold : bool


class Bank(SQLModel, table = True):
    id : int = Field(primary_key = True)
    account_holder_name: str
    account_no: int
    ifsc_code : str

create_tables()