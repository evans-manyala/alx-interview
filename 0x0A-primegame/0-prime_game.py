#!/usr/bin/python3
"""
Function that generates a list of prime numbers to
determine the winner of the game
"""

def sieve(n):
    """
    Function generates a list of primes up to n 
    using the Sieve of Eratosthenes.
    """
    
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]

def count_primes_up_to(n):
    """
    Counts the number of prime moves in a game with n numbers.
    """
    primes = sieve(n)
    count = 0
    while primes:
        prime = primes[0]
        primes = [p for p in primes if p % prime != 0]
        count += 1
    return count

def isWinner(x, nums):
    """
    Determines the winner of the game.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
        else:
            prime_count = count_primes_up_to(n)
            if prime_count % 2 == 1:
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
