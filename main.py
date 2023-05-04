from fastapi import FastAPI
from sympy import is_prime

app = FastAPI()

@app.get("/hello")
async def read_root():
    return {"message": "Hello FastAPI"}

@app.get("/IsPrime/{number}")
async def is_prime_number(number: int):
    return {"IsPrime": is_prime(number)}

@app.get("/fibonacci/{position}")
async def fibonacci(position: int):
    a, b = 0, 1
    for i in range(position):
        a, b = b, a + b
    return {"fibonacci": a}
