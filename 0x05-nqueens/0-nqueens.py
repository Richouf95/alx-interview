#!/usr/bin/python3
"""
The N queens puzzle
"""


def is_safe(board, row, col, N):
    """
    Déterminer si une position est sécurisée
    """
    # Vérifier cette colonne sur les lignes au-dessus
    for i in range(row):
        if board[i] == col:
            return False

    # Vérifier la diagonale supérieure gauche
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False

    # Vérifier la diagonale supérieure droite
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i] == j:
            return False

    return True


def solve_n_queens(board, row, N, solutions):
    """
    Resolution du problème
    """
    # Si toutes les reines sont placées, ajouter la solution à la liste
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return

    # Essayer de placer une reine dans chaque colonne de cette ligne
    for col in range(N):
        if is_safe(board, row, col, N):
            # Placer une reine à la position (row, col)
            board[row] = col

            # Recur pour placer les reines restantes
            solve_n_queens(board, row + 1, N, solutions)

            # Retirer la reine de (row, col) (backtrack)
            board[row] = -1


def n_queens(N):
    """
    Fonction principale de N Queens
    """
    board = [-1] * N
    solutions = []
    solve_n_queens(board, 0, N, solutions)
    return solutions


# Fonction principale pour exécuter le script
if __name__ == "__main__":
    """
    if main
    """
    import sys
    if len(sys.argv) != 2:
        print("Usage: ./0-nqueens.py N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = n_queens(N)
    for solution in solutions:
        print(solution)
