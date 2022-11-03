from pydantic import BaseModel
from typing import Optional

class Siswa(BaseModel):
    nama : str
    jurusan :str
    nilai:list
    
    class Config:
        schema_extra = {
            "example": {
                "nama": "Airin",
                "jurusan": "Rekayasa Perangkat Lunak",
                "nilai":[]
            }
        }