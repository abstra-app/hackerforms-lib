from hackerforms import Page

class NewPageBuilder():

  def __init__(self, table_name):
    self.table_name = table_name
    self._page = 'Page()\\\n'
    self.add_title()

  def add_title(self):
    self._page += f"  .display('{self.table_name}')\\\n"

  def add_widget(self, widget, key):
    self._page += f"  .{widget}('{key}')\\\n"

  def close(self):
    self._page += f"  .run()"


  @property
  def page(self):
    return self._page

  def eval_page(self):
    return eval(self.page)
  

  @staticmethod
  def createPage(table_name: str):
    return NewPageBuilder(table_name)