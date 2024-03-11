from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_app():
        return {"message" : "Hello World!"}

@app.post("/", description = "Post app")
async def post():
        return {"message" : "Hello from post route"}

@app.put("/")
async def put():
        return {"message" : "Hello from put route"}



#path-parameters

@app.get("/items") #if i add "/items" after the localhost route, then the below content will be displayed
def list_items():
        return {"message": "list items route"}

@app.get("/items/{item_id}") #add route for the existing route
def get_item(item_id : int): #we can add type for parameter passed like def get_item(item_id : int)
        return {"item_id": item_id}



@app.get("/users/me")
def get_user():
        return {"user_id": "I am the current user"}

@app.get("/users/{user_id}")
def get_user(user_id: str):
        return {"user_id": user_id}
# specific paths like me, host should be put before the general one which takes id as input 
# because fastAPI scans the input from top to bottom and it print whichever path it matches with first



#Enum usage

from enum import Enum

class FoodEnum(str, Enum):
        fruits = "fruits"
        vegetables = "vegetables"
        dairy = "dairy"

@app.get("/foods/{food_name}")
def get_food(food_name: FoodEnum):
        if food_name == FoodEnum.vegetables:
                return {"food name": food_name, "message": "healthy vegetables"}
        if food_name == FoodEnum.fruits:
                return {"food name": food_name, "message": "sweet fruits"}
        return {"food name": food_name, "message": "dairy product"}