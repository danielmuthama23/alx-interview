# Prime Game

## Task

Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

    Prototype: def isWinner(x, nums)
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    You cannot import any packages in this task

Example:

    x = 3, nums = [4, 5, 1]

First round: 4

    Maria picks 2 and removes 2, 4, leaving 1, 3
    Ben picks 3 and removes 3, leaving 1
    Ben wins because there are no prime numbers left for Maria to choose

Second round: 5

    Maria picks 2 and removes 2, 4, leaving 1, 3, 5
    Ben picks 3 and removes 3, leaving 1, 5
    Maria picks 5 and removes 5, leaving 1
    Maria wins because there are no prime numbers left for Ben to choose

Third round: 1

    Ben wins because there are no prime numbers for Maria to choose

## Consider

1. In the game, the players take turns removing prime numbers and their multiples from the set of consecutive integers.
If a player cannot make a move, it means there are no prime numbers left for them to choose, and they lose the game.

2. The strategy of the players is to optimize their moves and prevent the other player from making a move.
The optimal strategy is to remove all the prime numbers, leaving only non-prime numbers.

3. If there are an even number of prime numbers in the range from 1 to `n`, it means that after all the prime numbers are removed,
an even number of non-prime numbers will remain. In this case, the player who moves last will be the one unable to make a move,
and they will lose. This corresponds to Ben winning the round.

4. Conversely, if there are an odd number of prime numbers in the range from 1 to `n`, it means that after all the prime numbers
are removed, an odd number of non-prime numbers will remain. In this case, the player who moves last will
be able to make the final move and force the other player into a situation where they cannot make a move,
resulting in their victory. This corresponds to Maria winning the round.

Therefore, by checking whether the count of prime numbers is odd or even, the solution determines whether Maria or Ben
wins each round based on the game's rules and the optimal strategy of the players.
