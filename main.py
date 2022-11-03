from fastapi import FastAPI, HTTPException, status
from schema import Siswa
import json

app = FastAPI()

fakeDb = []

@app.post("/siswa")
async def Add_siswa_with_nilai(payload:Siswa):
    if not fakeDb:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Get Data First")
    data = payload.dict()
    fakeDb.append(data)

    return fakeDb

@app.get("/siswa")
async def get_data():
    f = open ('data_siswa.json', "r")

    data = json.loads(f.read())

    for i in data:
        fakeDb.append(i)

    return fakeDb

@app.get("/generete")
async def generate():
    if not fakeDb:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Data")

    with open('data_siswa.json', 'w') as outfile:
        outfile.write(json.dumps(fakeDb, indent=4))

    return fakeDb

@app.get("/nilai")
async def look_nilai():
    if not fakeDb:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Get Data First")

    data_nilai = []
    for i in fakeDb:
        data = {}
        data["nama"] = i.get("nama")
        data["nilai"] = i.get("nilai")
        
        data["nilai_ascending"] = sorted(i.get("nilai"))
        data["nilai_descending"]= sorted(i.get("nilai"), reverse=True)

        data_nilai.append(data)
    return data_nilai