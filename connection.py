from pathlib import Path
from sqlmodel import SQLModel, create_engine, Session

# Absolute path to your SQLite database file
db_path = Path("/home/ahmedansari/Documents/fastapi_practice/test.db")

# SQLite connection string
connection = f"sqlite:///{db_path}"

# Configure the engine with SQLite-friendly options
engine = create_engine(
    connection,
    echo=True,  # Optional: set to False to hide SQL logs
    connect_args={
        "check_same_thread": False,  # needed when using threads (e.g. FastAPI with uvicorn)
        "timeout": 30,               # wait up to 30s if the database is locked
    },
    pool_pre_ping=True,  # helps avoid stale connections
)

print(engine)


def create_tables() -> None:
    """
    Create all tables defined in SQLModel metadata.
    Call this ONCE at startup or from a one-off script.
    """
    SQLModel.metadata.create_all(engine)