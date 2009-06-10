#!/usr/bin/python

__all__ = ['LazyRegex']


import re


def _check_compile(f):
    def new_f(self, *args, **kwargs):
        # Where the magic happens
        if not self._compiled:
            self._re       = re.compile(self._str)
            self._compiled = True

        return f(self, *args, **kwargs)

    new_f.__dict__.update(f.__dict__)
    new_f.__name__ = f.__name__
    new_f.__doc__  = f.__doc__

    return new_f


class LazyRegex(object):
    """A regular expression that's compiled on the first usage.

    Similar to calling re.compile() at the beginning of a program, but with less
    manual labor.
    """

    def __init__(self, s):
        self._str = s
        self._compiled = False

    # The rest of this is just static boilerplate since _sre.SRE_Match isn't a
    # real class, and therefore is impossible to dynamically query or mutate.
    @_check_compile
    def __copy__(self, *args, **kwargs):
        return self._re.__copy__(*args, **kwargs)

    @_check_compile
    def __deepcopy__(self, *args, **kwargs):
        return self._re.__deepcopy__(*args, **kwargs)

    @_check_compile
    def findall(self, *args, **kwargs):
        return self._re.findall(*args, **kwargs)

    @_check_compile
    def finditer(self, *args, **kwargs):
        return self._re.finditer(*args, **kwargs)

    @_check_compile
    def match(self, *args, **kwargs):
        return self._re.match(*args, **kwargs)

    @_check_compile
    def scanner(self, *args, **kwargs):
        return self._re.scanner(*args, **kwargs)

    @_check_compile
    def search(self, *args, **kwargs):
        return self._re.search(*args, **kwargs)

    @_check_compile
    def split(self, *args, **kwargs):
        return self._re.split(*args, **kwargs)

    @_check_compile
    def sub(self, *args, **kwargs):
        return self._re.sub(*args, **kwargs)

    @_check_compile
    def subn(self, *args, **kwargs):
        return self._re.subn(*args, **kwargs)
