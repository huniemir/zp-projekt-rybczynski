import primelib
from fastapi import FastAPI
from primelib import isprime

app = FastAPI()

@app.get("/prime/number")
async def isprime(number):
    if number.isnumeric():
        return {
                "isInt": True,
                "isPrime": primelib.isprime(int(number))
        }
    else:
        return {"isInt": False,
                "isPrime": None}