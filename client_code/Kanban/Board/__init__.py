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
    self._headers = {} # Header Map
    self._items = {} # Item Map
    self._grids  =  {}  #grid Map
    self._created = False # Flag to indicate if the board has been created. This determines if the board is built on form_show event.
    self._built = False # Flag to indicate if the board has been built
    
    self.grids = [] # Muuri Grids
    self.board = None 
    if data:
      self.create_board(data)

  def create_board(self,data):
    """
    This method creates the headers, items, and columns. It then inserts all 
    the respective components into their html slots.
    """
    if not self._created:
      self._created = True
      for row in data:
        header = Label(text=row['header'],align='center') if isinstance(row['header'],str) else row['header']
        column = Column()
        self._headers[column.uid] = header.text
        column.add_header(header,color=row.get('background'))
        for item in row['items']:
          I = Item()
          I.add_item(item)
          column.add_item(I)
          self._items[I.uid] = item
        self.add_column(column)

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
    column_id = item.getGrid().getElement().getAttribute('column_id')
    if raise_event:
      self.raise_event('x-items_changed',muuri=item,item=self._items[item_id],column=self._headers[column_id])

  def layout_start(self,item,*args):
    if self.board:
      self.board.refreshItems().layout();
    
  def build_board(self,draggable_columns=True,**event_args):
    """
    This method builds the Muuri Board. It is important that 'create_build' is called before
    build board. Muuri raises errors if the items cannot be found.
    """
    if not self._built:
      self._built = True
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
      headers = list(self._headers.values())
      
      for idx,container in enumerate(itemContainers):
        grid = Muuri(container,{
          'items': items[idx],
          'dragEnabled':True,
          'dragSort': self.drag_sort,
          'dragContainer':dragContainer, 
        })      
        grid.on('dragInit',self.drag_init) # Adding event handler for drag init of an item
        grid.on('dragReleaseEnd',self.drag_release_end) # Adding event handler for drag release of an item
        grid.on('layoutStart',self.layout_start) # Adding event to refresh the board layout
        self.grids.append(grid)
        self._grids[headers[idx]] = grid
        
      # Init board grid so we can drag those columns around.
      self.board = Muuri('.board', {
        'items': columns,
        'dragEnabled': draggable_columns,
        'dragHandle': '.board-column-header'
      })
    
  def add_item(self,column_name,item):
    """ Add item to the board component"""
    I = Item()
    I.add_item(item)
    self._items[I.uid] = item
    grid = self.get_grid(column_name)
    muuri_items = grid.add(I.get_item_node())
    self.raise_event('x-items_changed',muuri=muuri_items[0],item=item,column=column_name)

  def remove_item(self,column_name,item):
    grid = self.get_grid(column_name)
    grid.remove(item)
    
  def add_column(self,column):
    """ Add column to the board component"""
    self.add_component(column,slot="board-slot")
    self._columns.append(column)
    
  def get_columns(self):
    return [column.get_column_node() for column in self._columns]

  def get_item(self,item_id):
    return self._items[item_id]
    
  def get_grid(self,grid_name):
    return self._grids[grid_name]

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    if self._created and not self._built:
      self.build_board()