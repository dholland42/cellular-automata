from cellular_automata.rules import rule

RULES = {
    n: rule(n)
    for n
    in range(1, 257)
}
