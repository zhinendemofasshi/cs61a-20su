
def fibonacci(n):
    """ Input a number that is bigger than 3. Then it will compute the nth fibnacci number.

    >>> fibonacci(3)
    1
    >>> fibonacci(8)
    13
    >>> fibonacci(1)
    0
    """
    pre, cur = 0, 1
    i = 2
    while i < n: 
        pre, cur = cur, pre+cur
        i = i + 1
    return cur

from doctest import run_docstring_examples
run_docstring_examples(fibonacci, globals(), True)