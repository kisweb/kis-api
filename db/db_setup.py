from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLALCHEMY_DATABASE_URL = settings.SUPABASE_CONN_STRING # rollingambit acc
# ASYNC_SQLALCHEMY_DATABASE_URL = settings.ASYNC_SUPABASE_CONN_STRING
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:kisarrw3b@localhost:5432/fastapi"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, future=True
)

# AsyncSessionLocal = sessionmaker(
#     async_engine, class_=AsyncSession, expire_on_commit=False
# )

Base = declarative_base()

# DB utilities
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# async def async_get_db():
#     async with AsyncSessionLocal() as db:
#         yield db
#         await db.commit()
