from ._anvil_designer import template_gridTemplate
from anvil import *

from anvil import js

class template_grid(template_gridTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.


  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    js.call_js('create_board')
