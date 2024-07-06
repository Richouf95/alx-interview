#!/usr/bin/python3
'''LockBoxes Challenge'''


def can_open_all_boxes(boxes):
    """
    Returns:
        bool: True si toutes les boîtes peuvent être ouvertes, False sinon.
    """
    total_boxes = len(boxes)
    keys_collected = set()
    opened_boxes = []
    current_box = 0

    while current_box < total_boxes:
        previous_box = current_box
        opened_boxes.append(current_box)
        keys_collected.update(boxes[current_box])
        for key in keys_collected:
            if key != 0 and key < total_boxes and key not in opened_boxes:
                current_box = key
                break

        if previous_box != current_box:
            continue
        else:
            break

    for box_index in range(total_boxes):
        if box_index not in opened_boxes and box_index != 0:
            return False
    return True
