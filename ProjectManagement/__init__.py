import ProjectManagement.Models
import ProjectManagement.Database

def main(database='ProjectManagement.db', **kwargs):
    conn = Database.Connection(database, **kwargs)
    engine = conn.get_engine()
    session = conn.get_session()
    return engine, session
