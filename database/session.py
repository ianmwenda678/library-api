from sqlmodel import create_engine, Session

# Hardcoded database URL for development
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/library_db"

# Create the engine
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    '''Dependency for getting a database session'''
    with Session(engine) as session:
        yield session
