from ._anvil_designer import ItemFormTemplate
from anvil import *

class ItemForm(ItemFormTemplate):
  def __init__(self,label, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.label_1.text =label
