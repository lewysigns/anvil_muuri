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
    self._columns = []
    self.grids = []
    self.board = None
    if data:
      self.build_board(data)

  def build_board(self,data):
    for row in data:
      header = Label(text=row['header'],background=row.get('background'),align='center') if isinstance(row['header'],str) else row['header']
      column = Column()
      column.add_header(header)
      for item in row['items']:
        I = Item()
        I.add_item(item)
        column.add_item(I)
      self.add_column(column)

  def add_column(self,column):
    self.add_component(column,slot="board-slot")
    self._columns.append(column)

  def drag_sort(self):
    return self.grids

  def drag_init(self,item):
    item.getElement().style.width = item.getWidth() + 'px'
    item.getElement().style.height = item.getHeight() + 'px'

  def drag_release_end(self,item):
    item.getElement().style.width = ''
    item.getElement().style.height = ''
    item.getGrid().refreshItems([item])

  def layout_start(self,item):
    pass
    
  def create_board(self,**event_args):
    """This method is called when the form is shown on the page"""
    #
    # Adjusting width to based on number of columns in the board
    #
    for column in self._columns:
      column.set_width(len(self._columns))
      
    items = [column.get_items() for column in self._columns]
    columns = self.get_columns()
    #js.call_js('create_board',items,columns)
    from anvil.js.window import Muuri
    print("Start")
    dragContainer = js.get_dom_node(self).querySelector('.drag-container')
    itemContainers = js.get_dom_node(self).querySelectorAll('.board-column-content')
    self.grid = []
    
    print("Create Containers")
    for idx,container in enumerate(itemContainers):
      grid = Muuri(containier,{
        'items': items[idx],
        'dragEnabled':True,
        'dragSort': self.drag_sort,
        'dragContainer':dragContainer, 
      })
      grid.on('layoutStart', function () {
        
      });
      
      self.grids.append(grid)
    });
    print("Grids Added")
    #// Init board grid so we can drag those columns around.
    print("Adding Board")
    self.board = Muuri('.board', {
      items: columns,
      'dragEnabled': True,
      'dragHandle': '.board-column-header'
    }); 
    print("Done!")
  

  


  def get_columns(self):
    return [column.get_column_node() for column in self._columns]

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    self.create_board()

