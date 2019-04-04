"""DESCRIPTION OF THE MODULE GOES HERE TODO

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
    """Store and retrieve options for a web server"""

    def __init__(self, *args, **kwargs):
        super().__init__(kwargs)
        for arg in args:
            if isinstance(arg, str):
                self[arg] = True
            else:
                raise TypeError("Expected String")

    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except KeyError:
            return False

    def __getattr__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def __setattr__(self, key, value):
        pass

    def __delattr__(self, item):
        pass

