#!/usr/bin/python3
""" This defines a function that determines if a box containing 
    a list of lists can be opened using keys stored in the lists
"""


def canUnlockAll(boxes):
    """
     This a method that determines if all the boxes can be opened

    :param boxes:
    :return: True or False
    """
    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for s in unlocked:
        for key in boxes[s]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
