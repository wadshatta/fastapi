from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


class PackageIn(BaseModel):
    secret_id : int
    name: str
    number: str
    description : Optional [str] = None

class Package(BaseModel):
    name : str
    number : str
    description : Optional[str] = None


app = FastAPI()

@app.get('/')
async def hello_world():
    return {"hello":"world"}


@app.post("/package/" ,response_model=Package,response_model_exclude_unset=True)
async def make_package(package: PackageIn):
    return package




# @app.get("/component/{component_id}")
# async def get_component(component_id: int):
#     return {'component_id':component_id}

# @app.get("/component/")
# async def read_component(number: int,text:str):
#     return {"number":number,"text":text}
