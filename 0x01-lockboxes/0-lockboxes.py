#!/usr/bin/python3
"""
Defines a function that determines if a box containing a list
of lists can be opened using keys stored in the lists
"""


def canUnlockAll(boxes):
    """ Determines if all the boxes can be opened. """
    if not boxes:
        return False

    n = len(boxes)
    opened = set()
    queue = (0)

    while queue:
        box_index = queue.pop(0)

        if box_index not in opened:
            opened.add(box_index)

            for key in boxes[box_index]:
                if key < n and key not in opened:
                    queue.append(key)

    return len(opened) == n
