from ._anvil_designer import FormTemplate
from anvil import *

from ...column import column
from ..ItemForm import ItemForm

class Form(FormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    data = [
      {'header':"column 1",'background':'red','items':[ItemForm('test 1'),ItemForm('test 2')]},
      {'header':"column 2",'background':'blue','items':[ItemForm('test 3'),ItemForm('test 6')]},
      {'header':"column 3",'background':'green','items':[ItemForm('test 4'),ItemForm('test 5')]}
    ]
    columns = [column(d) for d in data]
    for col in columns:
      self.board_1.add_column(col)

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    pass#self.board_1.create_board()

  
