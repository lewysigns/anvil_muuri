from ._anvil_designer import template_itemTemplate
from anvil import *

class template_item(template_itemTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
