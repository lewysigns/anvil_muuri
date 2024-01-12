from ._anvil_designer import FormTemplate
from anvil import *

from ..ItemForm import ItemForm #Example Item Form to be added to a column.

from ...Kanban.Board import Board

class Form(FormTemplate):
  """Example using the Kanban.Board via code"""
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    
    data = [
      {'header':"column 1",'background':'','items':[ItemForm('test 1'),ItemForm('test 2')]},
      {'header':"column 2",'background':'blue','items':[ItemForm('test 3'),ItemForm('test 6')]},
      {'header':"column 3",'background':'green','items':[ItemForm('test 4'),ItemForm('test 5')]},
      {'header':Label(text="column 4",align="center",foreground='black'),'background':'yellow','items':[ItemForm('test 42'),ItemForm('test 10')]}
    ]
    
    self.board = Board(data)
    self.add_component(self.board,full_width_row=True)
    self.board.add_event_handler('x-items_changed',self.handle_change)

  def handle_change(self,**event_args):
    column_name = event_args['column']
    item = event_args['item']
    muuri_item = event_args['muuri']
    Notification(f"Item moved to {column_name}").show()
    item.label_1.visible = column_name in ["column 1","column 3"]
    #
    # You must refresh the grid cache to get the new dimensions
    # when you alter the size of an item by calling 'refreshItems'. 
    # Then you can update the table layout  by calling 'layout'
    #
    muuri_item.getGrid().refreshItems([muuri_item])
    muuri_item.getGrid().layout()

  def button_add_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.board.add_item("column 1",ItemForm('test added'))
