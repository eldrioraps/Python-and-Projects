from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pyodbc
from db_connection import get_connection

app = FastAPI(title="Passenger Upload API")

# --- Define schema for validation ---
class Passenger(BaseModel):
    Name: str
    Age: int
    Sex: str
    Fare: float

class PassengerList(BaseModel):
    passengers: list[Passenger]

# --- Endpoint ---
@app.post("/upload_passengers")
def upload_passengers(payload: PassengerList):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        for p in payload.passengers:
            cursor.execute("""
                INSERT INTO Passengers (Name, Age, Sex, Fare)
                VALUES (?, ?, ?, ?)
            """, (p.Name, p.Age, p.Sex, p.Fare))

        conn.commit()
        conn.close()
        return {"status": "success", "inserted": len(payload.passengers)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
