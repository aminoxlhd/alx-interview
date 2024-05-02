#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """
    a method that determines if all the boxes can be opened.

    Args:
        boxes: A list of lists, where each inner list represents the keys
               a specific box contains.

    Returns:
          True if all boxes can be opened, False otherwise.
    """
    tested = set()
    queue = [0]
    tested.add(0)

    while queue:
        box_number = queue.pop(0)
        for key in boxes[box_number]:
            if key not in tested:
                tested.add(key)
                queue.append(key)

    return len(tested) == len(boxes)
