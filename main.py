from string import ascii_lowercase
from random import choice

chars = "".join([choice(ascii_lowercase) for _ in range(4)])

print(chars)
