def main(database='ProjectManagement.db', **kwargs):
    from .Database.connection import Connection
    conn = Connection(database, **kwargs)
    engine = conn.get_engine()
    session = conn.get_session()
    return engine, session
