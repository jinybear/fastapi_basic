import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from app import app

origin = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8008)

