# Import FastAPI
from fastapi import FastAPI
from fastapi import APIRouter

# Start Create Asyn Function
helloapi = APIRouter()
goodbyeapi = APIRouter()


@helloapi.get("/hello")
async def hello():
    return 'Hello'

@goodbyeapi.get("/goodbye")
async def goodbye():
    return 'GoodBye'

# Main App
app = FastAPI()
app.include_router(helloapi)
app.include_router(goodbyeapi)
