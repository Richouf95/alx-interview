#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    """

    # Initialiser le périmètre
    perimeter = 0

    # Obtenir les dimensions de la grille
    rows = len(grid)
    cols = len(grid[0])

    # Parcourir chaque cellule de la grille
    for i in range(rows):
        for j in range(cols):
            # Si la cellule est de la terre
            if grid[i][j] == 1:
                # Chaque cellule de terre a
                # initialement 4 côtés potentiels
                perimeter += 4

                # Vérifier le voisin du haut
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                # Vérifier le voisin de gauche
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
