from sqlmodel import create_engine, Session # type: ignore

engine = create_engine(
    "sqlite:///./app/carsharing.db",
    connect_args={"check_same_thread": False},
    echo=True
)

def get_session():
    with Session(engine) as session:
        yield session
