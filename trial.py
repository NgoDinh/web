import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:postgres@localhost/mydatabase")
db = scoped_session(sessionmaker(bind=engine))

def main():
    data = db.execute("select * from emp_data")
    for row in data:
        print(row.name, row.age)

if __name__ == "__main__":
    main()
