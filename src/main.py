from fastapi import FastAPI
from routes import base, data, FirebaseData

app = FastAPI()

app.include_router(base.base_router)
app.include_router(data.data_router)
app.include_router(FirebaseData.firebase_router)
