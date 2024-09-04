#!/usr/bin/python3
"""
0x0A. Prime Game
"""


def isWinner(x, nums):
    """
    check winner
    """
    if x < 1 or not nums:
        return None

    # Déterminer la limite maximale des nombres dans les nums
    max_n = max(nums)

    # Générer un tableau pour vérifier les nombres premiers jusqu'à max_n
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 et 1 ne sont pas des nombres premiers

    # Crible d'Ératosthène pour marquer les nombres non premiers
    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    # Préparer un tableau pour compter les nombres premiers jusqu'à chaque n
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Compteurs de victoires pour Maria et Ben
    maria_wins = 0
    ben_wins = 0

    # Simuler chaque round du jeu
    for n in nums:
        # Le nombre de tours possibles est égal au
        # nombre de nombres premiers jusqu'à n
        if prime_count[n] % 2 == 1:
            maria_wins += 1  # Maria gagne si le nombre de tours est impair
        else:
            ben_wins += 1  # Ben gagne si le nombre de tours est pair

    # Déterminer le gagnant final
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
