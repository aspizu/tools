input = """
alpha = 123
beta = 3
playground = 2
"""[
    1:-1
]

output = """
alpha      = 123
beta       = 3
playground = 2
"""[
    1:-1
]
assert input == output
