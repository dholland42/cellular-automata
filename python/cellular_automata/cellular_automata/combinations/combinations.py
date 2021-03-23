from typing import List, Iterable

import itertools


def zpad(state: List[int]) -> List[int]:
    return [0] + list(state) + [0]

def sliding_window(iterable: Iterable, n: int = 2) -> Iterable:
    iterables = itertools.tee(iterable, n)
    for iterable, num_skipped in zip(iterables, itertools.count()):
        for _ in range(num_skipped):
            next(iterable, None)
    return zip(*iterables)

def transition(state: List[int]) -> List[int]:
    newstate = list()
    for batch in sliding_window(zpad(state), 3):
        if batch[0] + batch[-1] == 1:
            newstate.append(1)
        else:
            newstate.append(0)
    return newstate


if __name__ == "__main__":
    state = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    print(state)
    for _ in range(20):
        state = transition(state)
        print(state)
