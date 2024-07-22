#!/usr/bin/python3
"""
Defines a function that determines if a box containing a list
of lists can be opened using keys stored in the lists
"""


def canUnlockAll(boxes):
    """ Determines if all the boxes can be opened. """
    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
