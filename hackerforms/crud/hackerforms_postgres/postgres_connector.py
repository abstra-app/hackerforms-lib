import psycopg2

from hackerforms.crud.client import Connector


class PostgresConnector(Connector):
  def __init__(self, dsn=None, **kwargs):
    self.connection: psycopg2.connect = psycopg2.connect(dsn, **kwargs)

  def select(self, query: str):
    cursor = self.connection.cursor()
    cursor.execute(query)
    output = cursor.fetchall()
    cursor.close()
    return output

  def insert(self, query: str):
    cursor = self.connection.cursor()
    cursor.execute(query)
    self.connection.commit()
    cursor.close()
