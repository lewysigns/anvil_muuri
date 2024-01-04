from ._anvil_designer import BoardTemplate
from anvil import *

from anvil import js

from ..Column import Column
from ..Item import Item

class Board(BoardTemplate):
  def __init__(self,data=None,**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self._columns = [] # Column Templates
    self._items = {} # Item Content
    self.grids = [] # Muuri Grids
    self.board = None 
    self.created = False # Flag to indicate if the board has been created. This determines if the board is built on form_show event.
    if data:
      self.create_board(data)

  def create_board(self,data):
    for row in data:
      header = Label(text=row['header'],background=row.get('background'),align='center') if isinstance(row['header'],str) else row['header']
      column = Column()
      column.add_header(header)
      for item in row['items']:
        I = Item()
        I.add_item(item)
        column.add_item(I)
        self._items[I.uid] = item
      self.add_column(column)
    self.created = True

  def drag_sort(self,item):
    return self.grids

  def drag_init(self,item,*args):
    item.getElement().style.width = str(item.getWidth()) + 'px'
    item.getElement().style.height = str(item.getHeight()) + 'px'

  def drag_release_end(self,item,raise_event=True):
    item.getElement().style.width = ''
    item.getElement().style.height = ''
    item.getGrid().refreshItems([item])
    item_id = item.getElement().getAttribute('item_id')
    if raise_event:
      self.raise_event('x-items_changed',muuri=item,item=self._items[item_id])

  def layout_start(self,item,*args):
    self.board.refreshItems().layout();
    
  def build_board(self,draggable_columns=True,**event_args):
    """This method builds the Muuri Board."""
    #
    # Adjusting column width based on number of columns in the board
    #
    for column in self._columns:
      column.set_width(len(self._columns))
      
    items = [column.get_items() for column in self._columns]
    columns = self.get_columns()
    
    #
    # Instead of the below, it can builtin javascript: js.call_js('create_board',items,columns)
    # However, there is an advantage of building the events in anvil/python if built here
    #
    
    from anvil.js.window import Muuri
    
    dragContainer = js.get_dom_node(self).querySelector('.drag-container')
    itemContainers = js.get_dom_node(self).querySelectorAll('.board-column-content')
    self.grid = []
    
    for idx,container in enumerate(itemContainers):
      grid = Muuri(container,{
        'items': items[idx],
        'dragEnabled':True,
        'dragSort': self.drag_sort,
        'dragContainer':dragContainer, 
      })      
      grid.on('dragInit',self.drag_init)
      grid.on('dragReleaseEnd',self.drag_release_end)
      grid.on('layoutStart',self.layout_start)
      self.grids.append(grid)
      
    #// Init board grid so we can drag those columns around.
    self.board = Muuri('.board', {
      'items': columns,
      'dragEnabled': draggable_columns,
      'dragHandle': '.board-column-header'
    })

  def add_column(self,column):
    self.add_component(column,slot="board-slot")
    self._columns.append(column)
    
  def get_columns(self):
    return [column.get_column_node() for column in self._columns]

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    if self.created:
      self.build_board()