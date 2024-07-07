#!/usr/bin/python3
"""
Lockboxes Python Code
"""

"""
You have a lockbox of n number of boxes in front of you. Each box is
locked by a sequence of keys in other boxes. Can you open all the boxes?
"""


def canUnlockAll(boxes):
    """ Determines if all the boxes can be opened. """
    n = len(boxes)
    opened = set()
    queue = [0]

    while queue:
        box_index = queue.pop(0)

        if box_index not in opened:
            opened.add(box_index)

            for key in boxes[box_index]:
                if key < n:
                    queue.append(key)

    return len(opened) == n
