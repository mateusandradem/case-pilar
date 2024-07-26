import uvicorn

from src.main import app


def run():
    uvicorn.run(app, host="127.0.0.1", port="8080")


if __name__ == "__main__":
    run()
