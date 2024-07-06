#!/usr/bin/python3
'''LockBoxes'''


def canUnlockAll(boxes):
    '''
    Returns:
        True: toutes les boîtes peuvent être ouvertes
        False: toutes les boîtes ne peuvent pas être ouvertes
    '''
    num_boxes = len(boxes)
    collected_keys = set()
    accessible_boxes = []
    current_index = 0

    while current_index < num_boxes:
        previous_index = current_index
        accessible_boxes.append(current_index)
        collected_keys.update(boxes[current_index])

        for key in collected_keys:
            if key != 0 and key < num_boxes and key not in accessible_boxes:
                current_index = key
                break

        if previous_index != current_index:
            continue
        else:
            break

    for box_index in range(num_boxes):
        if box_index not in accessible_boxes and box_index != 0:
            return False
    return True
