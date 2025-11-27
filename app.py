from fastapi import FastAPI
from pydantic import BaseModel
from models import Users2, Employee, Books, select
from connection import get_session

app = FastAPI()

class Response_model(BaseModel):
    username: str
    password: str
    employee_name: str
    employee_email : str
    employee_phoneno : int
    employee_age : int    
    book_name : str
    book_author : str
    book_year : int
    sold : bool



@app.get("/health_check")
def health_check():
    return "FastAPI is running properly"


@app.post("/insert_data")
def insert_data(data : Response_model):
    with get_session() as db:
        insert_data = Users2(username= data.username, password= data.password)
        db.add(insert_data)
        insert_data2 = Employee(employee_name= data.employee_name, employee_age= data.employee_age, employee_email= data.employee_email, employee_phoneno= data.employee_phoneno)
        db.add(insert_data2)
        insert_data3 = Books(book_name = data.book_name, book_author= data.book_author, book_year= data.book_year, sold = data.sold)
        db.add(insert_data3)
        db.commit()
    return{"msg" : "Data added"}


@app.get("/get_all_data")
def get_all_data():
    with get_session() as db:
        read_all_data = db.exec(select (Books)).all()
        return(read_all_data)
    

@app.get("/get_specific_data/{id}")
def get_specific_data(id: int):
    with get_session() as db:
        read_specific_data = db.get(Books, id)
        return(read_specific_data)
    


@app.patch("/update_book_data/{id}")
def update_book_data(id):
    with get_session() as db:
        patch_data = db.get(Books, id)
        patch_data.book_author = "Benjamin"
        patch_data.book_year = 2014
        db.add(patch_data)
        db.commit()
        return {"msg" : "data updated"}
    


@app.delete("/delete_book_data/{id}")
def delete_book_data(id):
    with get_session() as db:
        delete_data = db.get(Books, id)
        db.delete(delete_data)
        db.commit()
        return {"msg" : "data deleted"}