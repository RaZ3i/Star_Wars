from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from routers.router import router as information_router
from routers.pages import router as pages_router
import uvicorn

app = FastAPI(title="Homework")
app.mount("/static", StaticFiles(directory="static", html=True), name="static")
app.include_router(information_router)
app.include_router(pages_router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8001, reload=True)
