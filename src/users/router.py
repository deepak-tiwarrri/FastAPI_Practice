from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from src.users.dtos import UserSchema
from src.utils.db import get_db
from src.users import controllers

user_router = APIRouter(prefix='/user')


@user_router.post('/register',status_code= status.HTTP_200_OK)
def register(body:UserSchema,db:Session=Depends(get_db)):
   return  controllers.register_user(body,db)


















# from dtos import ProductDTO
# from fastapi import FastAPI,Request
# from mockdata import products


# app = FastAPI(title="Task Management API")


# @app.get("/")
# def home():
#     return "Welcome to fastapi"


# @app.get("/products")
# def get_products():
#     return products

# @app.get("/products/{product_id}")
# def get_one_product(product_id:int):
#     for product in products:
#         if product.get('id') == product_id:
#             return product
#     return {"error":"Product not found"}

# @app.get("/greet")
# def greet(name:str,age:int):
#     return {"message":f"Welcome,{name}, your age is {age}"}

# @app.get("/greet_advanced")
# def greet_advanced(request:Request):
#     params = dict(request.query_params)
#     name = params.get('name')
#     age = params.get('age')
#     return {"message":f"Hello {name},your age is {age}","all_params":params}

# # now we have to post the new data of product 
# @app.post('/create_product')
# def create_product(product:ProductDTO):
#     new_product = product.model_dump();
#     products.append(new_product)
#     return {"status":"Product Created Successfully","data":products}

# @app.put("/update_product")
# def update_product(product_id:int,product_data:ProductDTO):
#     for index, product in enumerate(products):
#         if product_id == product.get('id'):
#             products[index]= product_data.model_dump();
#             return {"status":"Product Updated Successfully","data":products}
    
#     return {"error":"Not able to find the Product!!"}


# @app.delete("/delete-product/{product_id}")
# def delete_product(product_id:int):
#     for index, product in enumerate(products):
#         if product_id == product.get('id'):
#             deleted_product = products.pop(index)
#             return {
#                 "status":"Deleted Successfully","deleted_product":deleted_product
#             }
#     return {"error":f"Product not found with ID {product_id} "}


