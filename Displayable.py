from abc import abstractmethod, ABC


class Displayable(ABC):
    def __init__(self, width_percent: float = 10, height_percent: float = 10):  # percent of sheet
        self.width_percent = width_percent
        self.height_percent = height_percent

    def set_width(self, width_percent):
        self.width_percent = width_percent

    def set_height(self, height_percent):
        self.height_percent = height_percent

    @abstractmethod
    def display(self):
        pass
