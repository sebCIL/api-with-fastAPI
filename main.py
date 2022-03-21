from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

import pyodbc
conn = pyodbc.connect("DSN=*LOCAL;CCSID=1208;")

app = FastAPI()

# Se baser sur Java pour découper le code

class CustCdt(BaseModel):
    CUSNUM: int
    LSTNAM: str
    INIT: str
    STREET: str
    CITY: str
    STATE: str
    ZIPCOD: int
    CDTLMT: int
    CHGCOD: int
    BALDUE: float
    CDTDUE: float

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# Tous les custumers
@app.get("/custumer", response_model=list[CustCdt])
def getCustumerAll():
    objects_list = []
    cursor = conn.cursor()
    cursor.execute('select * from qiws.qcustcdt')
    columns = [column[0] for column in cursor.description]

    for row in cursor.fetchall():
        result = dict(zip(columns, row))
        objects_list.append(result)
    return objects_list
    conn.close()

# Un custumer par son numéro
@app.get("/custumer/{cusnum}", response_model=CustCdt)
def getCustumerByCusnum(cusnum: int):
    cursor = conn.cursor()
    cursor.execute('select * from qiws.qcustcdt where cusnum = ?', cusnum)
    columns = [column[0] for column in cursor.description]
    result = {}
    for row in cursor.fetchall():
        result = dict(zip(columns, row))
    return result
    conn.close()

# Mise à jour d'un custumer
@app.post("/custumer/{cusnum}", response_model=CustCdt)
def getCustumerByCusnum(cusnum: int, custumer: CustCdt):
    cursor = conn.cursor()
    cursor.execute('update qiws.qcustcdt set ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? where cusnum = ?', custumer.CUSNUM, custumer.LSTNAM, custumer.INIT, custumer.STREET, custumer.CITY, custumer.STATE, custumer.ZIPCOD, custumer.CDTLMT, custumer.CHGCOD, custumer.BALDUE, custumer.CDTDUE, cusnum)
    # return result
    conn.close()

# Ajout d'un custumer
@app.put("/custumer/", response_model=CustCdt)
def getCustumerByCusnum(custumer: CustCdt):
    cursor = conn.cursor()
    cursor.execute('insert into qiws.qcustcdt (CUSNUM, LSTNAM, INIT, STREET, CITY, STATE, ZIPCOD, CDTLMT, CHGCOD, BALDUE, CDTDUE) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', custumer.CUSNUM, custumer.LSTNAM, custumer.INIT, custumer.STREET, custumer.CITY, custumer.STATE, custumer.ZIPCOD, custumer.CDTLMT, custumer.CHGCOD, custumer.BALDUE, custumer.CDTDUE, cusnum)
    columns = [column[0] for column in cursor.description]
    result = {}
    for row in cursor.fetchall():
        result = dict(zip(columns, row))
    return result
    conn.close()

# Suppression d'un custumer
@app.delete("/custumer/{cusnum}")
def deleteCustumerByCusnum(cusnum: int):
    cursor = conn.cursor()
    cursor.execute('delete from qiws.qcustcdt where cusnum = ?', cusnum)
    # return result
    conn.close()