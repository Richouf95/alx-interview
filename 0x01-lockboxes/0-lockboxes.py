#!/usr/bin/python3

from collections import deque


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    :param boxes: List of lists, where each sublist contains keys to other boxes
    :return: True if all boxes can be opened, False otherwise
    """
    boxesLength = len(boxes)
    opened = [False] * boxesLength
    opened[0] = True  # Box 0 is always open

    queue = deque([0])  # Start with the first box

    while queue:
        current_box = queue.popleft()

        for key in boxes[current_box]:
            if 0 <= key < boxesLength and not opened[key]:
                opened[key] = True
                queue.append(key)

    return all(opened)
