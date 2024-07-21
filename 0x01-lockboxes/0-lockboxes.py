#!/usr/bin/python3
"""
Defines a function that determines if a box containing a list
of lists can be opened using keys stored in the lists
"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened."""
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and not opened[key]:
                opened[key] = True
                keys.append(key)
        return all(opened)
