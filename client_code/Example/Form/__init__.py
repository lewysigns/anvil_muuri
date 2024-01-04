from ._anvil_designer import FormTemplate
from anvil import *

from anvil import js

from ..ItemForm import ItemForm

from ...Kabaan.Column import Column
from ...Kabaan.Item import Item
from ...Kabaan.Board import Board

class Form(FormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    
    data = [
      {'header':"column 1",'background':'','items':[ItemForm('test 1'),ItemForm('test 2')]},
      {'header':"column 2",'background':'blue','items':[ItemForm('test 3'),ItemForm('test 6')]},
      {'header':"column 3",'background':'green','items':[ItemForm('test 4'),ItemForm('test 5')]},
      {'header':Label(text="TESTING"),'background':'green','items':[ItemForm('test 42'),ItemForm('test 10')]}
    ]
    
    self.grid = Board(data)
    self.add_component(self.grid)
    self.grid.add_event_handler('x-items_changed',self.handle_change)

  def handle_change(self,**event_args):
    item = event_args['item']
    muuri = event_args['muuri']
    item.background='blue'
    item.label_1.remove_from_parent()
    #
    # You must refresh the grid cache to get the new dimensions
    # when you alter the size of an item by calling 'refreshItems'. 
    # Then you can update the table layout  by calling 'layout'
    #
    muuri.getGrid().refreshItems([muuri])
    muuri.getGrid().layout()
