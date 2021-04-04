from typing import List, Iterable

import itertools

from cellular_automata import RULES


def zpad(state: List[int]) -> List[int]:
    """Zero pad a state on either end in order to correctly apply rule(s).
    
    Args:
        state: A state (list of 0's and 1's) to zero pad.

    Returns:
        The state passed in, padded with a zero on either end.
    """
    return [0] + list(state) + [0]

def sliding_window(iterable: Iterable, n: int = 2) -> Iterable:
    """Create a sliding window on an iterable.

    Args:
        iterable: An iterable to create a sliding window over.
        n: The size of the sliding window. Defaults to 2.

    Returns:
        An iterable where each element is a window of size n on the
        original iterable.

    Example:
        >>> list(sliding_window(range(5), 3))
        [(0, 1, 2), (1, 2, 3), (2, 3, 4)]
    """
    iterables = itertools.tee(iterable, n)
    for iterable, num_skipped in zip(iterables, itertools.count()):
        for _ in range(num_skipped):
            next(iterable, None)
    return zip(*iterables)

def transition(state: List[int], rule: int = 30) -> List[int]:
    """Transition a state to a new state.

    Args:
        state: The state to transition represented as a list of 0's and 1's.
        rule: The id of the rule to apply. Defaults to rule 30.

    Returns:
        An updated state, also a list of 0's and 1's.

    Example:
        >>> transition([0, 0, 1, 0, 0])
        [0, 1, 1, 1, 0]
        >>> transition([0, 1, 1, 1, 0])
        [1, 1, 0, 0, 1]
    """
    return list(RULES[rule][s] for s in sliding_window(zpad(state), 3))


if __name__ == "__main__":
    state = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    print(state)
    for _ in range(20):
        state = transition(state)
        print(state)
