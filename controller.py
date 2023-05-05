from view import View
from model import Model

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View( self.model)
