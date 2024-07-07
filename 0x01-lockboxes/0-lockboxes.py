#!/usr/bin/python3
"""
Lockboxes Python Code
"""

"""
You have a lockbox of n number of boxes in front of you. Each box is
locked by a sequence of keys in other boxes. Can you open all the boxes?
"""


def canUnlockAll(boxes):
    # Number of boxes
    n = len(boxes)
    
    # Set of opened boxes
    opened = set()
    
    # Queue for BFS, starting with the first box
    queue = [0]
    
    while queue:
        box_index = queue.pop(0)
        
        # If the box is not already opened
        if box_index not in opened:
            # Open the box
            opened.add(box_index)
            
            # Add all keys in this box to the queue
            for key in boxes[box_index]:
                if key < n:  # Ensure the key is valid
                    queue.append(key)
    
    # Check if all boxes have been opened
    return len(opened) == n
