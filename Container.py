from typing import List, Tuple

from Displayable import Displayable
from Widget import Widget


class Container(Displayable):
    def __init__(self, width_percent, height_percent):  # 'percent' of sheet
        super().__init__(width_percent, height_percent)
        self.widgets: List[Tuple[Widget, str]] = []

    def add_widget(self, widget: Widget, anchor: str = 's'):
        self.widgets.append((widget, anchor))

    def display(self):
        pass  # TODO
