"""Application entry point."""
# from app import create_app
from app import app
# app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
