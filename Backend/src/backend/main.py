from fastapi import FastAPI,HTTPException,status
from typing import Annotated
from database import Base,engine,get_db

app = FastAPI(title="SmartWash")

@app.get("/api/reading/{reading_id}",response_model = ModelResponse)
def get_reading(reading_id:int,db:Annotated[Session,Depends(get_db)]):
    result = db.execute(select(models.reading).where(models.Food.code == code))
    reading = result.scalars().first()
    if reading:
        return reading
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="reading not found")