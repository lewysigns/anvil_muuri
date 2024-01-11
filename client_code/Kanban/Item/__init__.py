from ._anvil_designer import ItemTemplate
from anvil import *
from anvil import js 

import random

class Item(ItemTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.uid = None

  def add_item(self,item):
    """Add Component to board item"""
    self.add_component(item,slot="item-slot")
    self.set_uid()
    item.item_id = self.uid

  def get_item_node(self):
    return js.get_dom_node(self).querySelector(".board-item")

  def set_uid(self):
    hexdigits = "0123456789ABCDEF"
    self.uid = "".join([hexdigits[random.randint(0,0xF)] for _ in range(25)])
    node = self.get_item_node()
    node.setAttribute("item_id",self.uid)
    
    
