from ._anvil_designer import BoardTemplate
from anvil import *

from anvil import js

from ..Column import Column
from ..Item import Item

class Board(BoardTemplate):
  def __init__(self,data,**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self._columns = []
    if data:
      self.build_board(data)

  def build_board(self,data):
    for row in data:
      header = Label(text=row['header'],background=row['background'],align='center') if isinstance(row['header'],str)
      column = Column()
      column.add_header(header)
      for item in row['items']:
        I = Item()
        I.add_item(item)
        column.add_item(I)
      self.grid.add_column(column)

  def add_column(self,column):
    self.add_component(column,slot="board-slot")
    self._columns.append(column)

  def create_board(self,**event_args):
    """This method is called when the form is shown on the page"""
    items = [column.get_items() for column in self._columns]
    columns = self.get_columns()
    js.call_js('create_board',items,columns)

  def get_columns(self):
    return [column.get_column_node() for column in self._columns]
