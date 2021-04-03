import itertools
from typing import Tuple

# Set up all possible states of 3 elements in a row
# ((1, 1, 1),
#  (1, 1, 0),
#  (1, 0, 1), 
#  (1, 0, 0),
#  (0, 1, 1),
#  (0, 1, 0),
#  (0, 0, 1),
#  (0, 0, 0))
STATES = tuple(itertools.product((1, 0), repeat=3))

def to_bin(n: int) -> Tuple[int]:
    """Convert an integer to it's 8-digit binary representation.
    """
    assert n > 0 and n < 511, "n must be between 1 and 510 (inclusive)"
    return tuple(int(x) for x in f"{n:08b}")


def rule(n: int) -> dict:
    """Implement one of the 256 rules of elementary cellular automata.

    Args:
        n: The id of the rule (1-256).
    
    Returns:
        A mapping from a tuple of 3 cellvalues to a single cell value.
    """
    assert n > 0 and n < 257, "must choose a rule between 1 and 256"
    values = to_bin(n)
    return {
        s: v
        for s, v
        in zip(STATES, values)
    }

