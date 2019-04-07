"""Extend the Dictionary Class to store and retrieve options.

Author: Tyler Baker
Class: CSI-260-01
Assignment: Week 12 Lab

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""


class Options(dict):
    """Store and retrieve options for a web server."""

    def __init__(self, *args, **kwargs):
        """Initialize the options."""
        super().__init__(kwargs)
        for arg in args:
            self[arg] = True

    def __getitem__(self, item):
        """Retrieve an item using bracket notation."""
        try:
            return super().__getitem__(item)
        except KeyError:
            return False

    def __getattr__(self, item):
        """Retrieve an item using attribute notation."""
        return self.__getitem__(item)

    def __setitem__(self, key, value):
        """Set an item using bracket notation."""
        if isinstance(key, str):
            self.update({key: value})
        else:
            raise TypeError("Expected String")

    def __setattr__(self, key, value):
        """Set an item using attribute notation."""
        self.__setitem__(key, value)

    def __delattr__(self, item):
        """Delete an attribute from the dictionary."""
        super().__delitem__(item)
