from ._anvil_designer import columnTemplate
from anvil import *

from anvil import js


class column(columnTemplate):
  def __init__(self,header,**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def set_width(self,width):
    dom_node = js.get_dom_node(self)
    dom_node.style.width = width

  def set_items(self,items):
    for item in items:
      item.role ='board-item'
      self.column_content.add_component(item)

