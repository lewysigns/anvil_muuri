from ._anvil_designer import template_columnTemplate
from anvil import *

class template_column(template_columnTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
