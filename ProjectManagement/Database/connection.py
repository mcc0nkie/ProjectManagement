from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ProjectManagement.Models import Base

class Connection:
    def __init__(self, db_name, verbose=False):
        if verbose:
            print("Creating database connection to " + db_name)
        self.engine = create_engine('sqlite:///' + db_name, echo=True)

        if verbose:
            print("Creating session")
        self.session = sessionmaker(bind=self.engine)

        if verbose:
            print("Checking tables")
        Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.session()

    def get_engine(self):
        return self.engine

    
