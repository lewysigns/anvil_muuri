from ._anvil_designer import ItemTemplate
from anvil import *
from anvil import js 

class Item(ItemTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def add_item(self,item):
    self.add_component(item,slot="item-slot")

  def get_item_node(self):
    return js.get_dom_node(self).querySelector(".board-item")
    
