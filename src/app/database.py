from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

# application import config.
from src.app.config import db_settings

# DB URL for connection - Using SQLite for easy setup
SQLALCHEMY_DATABASE_URL = f"sqlite:///./{db_settings.name}.db"

# Creating DB engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creating and Managing session.
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Domain Modelling Dependency
Base = declarative_base()


TEST_SQLALCHEMY_DATABASE_URL = f"sqlite:///./{db_settings.name}_test.db"
test_engine = create_engine(TEST_SQLALCHEMY_DATABASE_URL)
TestFactory = sessionmaker(autoflush=False, autocommit=False, bind=test_engine)
print("Database is Ready!")


def get_test_db():
    print("Test Database is Ready!")
    test_db = TestFactory()

    try:
        yield test_db
    finally:
        test_db.close()
