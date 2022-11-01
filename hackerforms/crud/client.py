from abc import ABC

from hackerforms.crud.connector import Connector

class Client(ABC):

  def __init__(self, connector: Connector):
    self.connector = connector

  def insert_page():
    pass

  def search_page():
    pass

  