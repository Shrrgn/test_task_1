import uvicorn

from api.app import app
from api.config import settings


if __name__ == "__main__":
    # for debug
    uvicorn.run(app, host=settings.host, port=settings.port)
