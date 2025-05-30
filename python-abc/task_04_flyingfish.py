#!/usr/bin/python3
"""Define the Fish class with swim and habitat behavior"""


class Fish:
    def swim(self):
        """Print a message indicating the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print a message about where the fish lives."""
        print("The fish lives in water")


# Define the Bird class with fly and habitat behavior
class Bird:
    def fly(self):
        """Print a message indicating the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print a message about where the bird lives."""
        print("The bird lives in the sky")


# Define FlyingFish, inheriting from both Fish and Bird
class FlyingFish(Fish, Bird):
    def swim(self):
        """Override swim to describe unique behavior of flying fish."""
        print("The flying fish is swimming!")

    def fly(self):
        """Override fly to describe unique behavior of flying fish."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Override habitat to reflect both environments."""
        print("The flying fish lives both in water and the sky!")
