from typing import List


class CombinationsCA:
    def __init__(self, initial_state: List[int] = [0 if r != 5 else 1 for r in range(11)]) -> None:
        self.initial_state = initial_state
        self.cells = [CombinationCell(i) for i in initial_state]
        for c1, c2 in zip(self.cells[:-1], self.cells[1:]):
            c1.neighbors.append(c2)
            c2.neighbors.append(c1)

    def step(self) -> "CombinationsCA":
        newvals = [cell.transition() for cell in self.cells]
        for cell, value in zip(self.cells, newvals):
            cell.value = value
        return self

    def reset(self, state=None) -> None:
        if state:
            self.cells = [CombinationCell(i) for i in state]
            for c1, c2 in zip(self.cells[:-1], self.cells[1:]):
                c1.neighbors.append(c2)
                c2.neighbors.append(c1)

        for cell in self.cells:
            cell.reset()

    @property
    def value(self) -> List[int]:
        return [cell.value for cell in self.cells]

    def __repr__(self) -> str:
        return str(self.value)

    def run(self, num_steps: int = 20) -> List[List[int]]:
        for _ in range(num_steps):
            yield self.step().value


class CombinationCell:
    def __init__(self, initial_value: int = 0) -> None:
        self.value = self.initial_value = initial_value
        self.neighbors = list()

    def transition(self) -> int:
        if sum(cell.value for cell in self.neighbors) == 1:
            return 1
        return 0

    def reset(self) -> None:
        self.value = self.initial_value


if __name__ == "__main__":
    ca = CombinationsCA()
    for row in ca.run():
        print(row)
