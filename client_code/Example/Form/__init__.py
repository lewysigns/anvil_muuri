from ._anvil_designer import FormTemplate
from anvil import *

from ..ItemForm import ItemForm

from ...template_column import template_column
from ...template_item import template_item

class Form(FormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    data = [
      {'header':"column 1",'background':'red','items':[ItemForm('test 1'),ItemForm('test 2')]},
      {'header':"column 2",'background':'blue','items':[ItemForm('test 3'),ItemForm('test 6')]},
      #{'header':"column 3",'background':'green','items':[ItemForm('test 4'),ItemForm('test 5')]}
    ]
    for row in data:
      header = Label(text=row['header'],background=row['background'])
      column = template_column()
      #column.add_component(header,slot="header")
      #for item in row['items']:
      #  I = template_item()
      #  I.add_component(item,slot="default")
      #  column.add_component(I,slot="content")
      self.grid.add_component(column,slot="board")
      

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.grid.create_board()