from typing import List, Container, Tuple


class Sheet:
    class Coordinates:
        def __init__(self, x, y):
            self.x = x  # percent of sheet (horizontal, left-to-right)
            self.y = y  # percent of sheet (vertical, top-to-bottom)

    def __init__(self):
        self.containers: List[Tuple[Container, Sheet.Coordinates]] = []

    def add_container(self, container: Container, x_pos: float, y_pos: float):
        self.containers.append((container, Sheet.Coordinates(x_pos, y_pos)))

    def export_to_png(self):
        pass  # TODO
