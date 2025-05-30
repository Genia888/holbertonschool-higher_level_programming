#!/usr/bin/python3
"""SwimMixin provides swim behavior to any class that inherits it"""



class SwimMixin:
    def swim(self):
        """Prints a swimming message, meant to be reused in other classes."""
        print("The creature swims!")


# FlyMixin provides fly behavior to any class that inherits it
class FlyMixin:
    def fly(self):
        """Prints a flying message, meant to be reused in other classes."""
        print("The creature flies!")


# Dragon inherits both swim and fly capabilities via mixins
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        """Adds a custom method specific to Dragon."""
        print("The dragon roars!")
