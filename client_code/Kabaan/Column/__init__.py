from ._anvil_designer import ColumnTemplate
from anvil import *
from anvil import js 

from ..Item import Item

class Column(ColumnTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def add_header(self,header):
    self.add_component(header,slot='header-slot')
    
  def add_item(self,item):
    self.add_component(item,slot="content-slot")

  def get_items(self):
    items = []
    for comp in self.get_components():
      if isinstance(comp,Item):
        items.append(comp.get_item_node())
    return items

  def get_column_node(self):
    return js.get_dom_node(self).querySelector(".board-column")

  def set_width(self,num):
    node = js.get_dom_node(self).querySelector(".board-column")
    node.style.width = f"calc(100%/{num})"
    