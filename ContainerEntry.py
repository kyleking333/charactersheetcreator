
from Displayable import Displayable


class ContainerEntry(Displayable):
    def __init__(self, title: Displayable, body: Displayable):
        super().__init__(title.width_percent + body.width_percent, title.height_percent + body.height_percent)
        self.title = title
        self.body = body

    def display(self):
        pass  # TODO
