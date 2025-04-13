from Menu import Menu
from HR import HR

class Restaurant:
    def __init__(self, name, tagline, location):
        self.name = name
        self.tagline = tagline
        self.location = location
        # Menu Implementation
        self.menu = Menu()
        self.__hr=HR()
        self.__admin = None
    # add a check if admin is operating or not
    def set_admin(self, admin):
        self.__admin = admin

    @property
    def hr(self):

        return self.__hr

