"""Reverse a string using recursion.

For example::

    >>> rev_string("")
    ''

    >>> rev_string("a")
    'a'

    >>> rev_string("porcupine")
    'enipucrop'

"""


def rev_string(astring):
    """Return reverse of string using recursion.

    You may NOT use the reversed() function!
    """

    # w/out recursion, just convert str to lst, [::-1], convert back to str
    # e.g. 'abc' --> c + 'ab' --> c + b + 'a' --> c + b + a + ''

    # BASE
        # when str empty, stop recursing
    if len(astring) == 1:
        return astring[0]

    # PROGRESSION
        # get last letter
        # call fn w/ last letter removed

    letter = astring[-1]
    return letter + rev_string(astring[:-1])


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. !KROW DOOG\n"
