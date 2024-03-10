# schema.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Insight(Base):
    __tablename__ = 'insights'

    id = Column(Integer, primary_key=True)
    end_year = Column(String)
    intensity = Column(Integer)
    sector = Column(String)
    topic = Column(String)
    insight = Column(String)
    start_year = Column(String)
    impact = Column(String)
    added = Column(String)
    published = Column(String)
    country = Column(String)
    relevance = Column(Integer)
    pestle = Column(String)
    source = Column(String)
    title = Column(String)
    likelihood = Column(Integer)
    region = Column(String)
    city = Column(String)

# Replace 'mysql://user:password@localhost/dbname' with your actual MySQL connection URL
engine = create_engine('mysql://db_assignment:db_assignment@localhost/DB_Assignment', echo=True)
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()
