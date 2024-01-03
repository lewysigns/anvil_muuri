from ._anvil_designer import boardTemplate
from anvil import *

from anvil import js

class board(boardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.columns = []

  def add_column(self,column):
    self.add_component(column)
    self.columns.append(column)
    self.update_column_widths()

  def update_column_widths(self):
    for col in self.columns:
      col.set_width("100%")

  def create_board(self):
    js.call_js('create_board')
