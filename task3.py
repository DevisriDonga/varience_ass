from fastapi import FastAPI, HTTPException

app = FastAPI()
db = []  # This will act as a simple database

@app.get('/instruments')
def get_instruments():
    return db

@app.post('/add')
def add_instrument(symbol: str):
    db.append(symbol)
    return db

@app.patch('/update')
def update_instrument(index: int, symbol: str):
    if index >= len(db):
        raise HTTPException(status_code=400, detail="No symbol found")
    db[index] = symbol
    return db

@app.delete('/remove')
def remove_instrument(index: int):
    if index >= len(db):
        raise HTTPException(status_code=400, detail="No symbol found")
    db.pop(index)
    return db
