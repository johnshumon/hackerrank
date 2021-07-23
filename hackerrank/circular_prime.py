"""Circular prime module"""

# problem_statement: https://www.hackerrank.com/contests/projecteuler/challenges/euler035/problem

# Find out all the circular prime below 1 million


class Solution:
    """Solution class"""

    def get_circular_primes(self, limit: int) -> list:
        """Returns the list of circular prime
        for a given boundary.
        """
        if limit < 2 or limit > 10 ** 6:
            return []

        # exclude all primes contains any of ("0", "2", "4", "5", "6", "8")
        # because it would make it non-prime during a rotation.
        exclude = set("024568")
        primes = ["2", "5"] + [
            prime
            for prime in map(str, self.get_primes(limit))
            if not set(prime).intersection(exclude)
        ]

        # the all() function returns True if all the rotations are a
        # member of the primes set. This would make "prime" a circular
        # prime number and it's added to the list.
        circular_primes = []
        for prime in primes:
            if all(prime_r in primes for prime_r in self.rotate(prime)):
                circular_primes.append(int(prime))

        return sorted(circular_primes)

        # below is the compact way to write above logic
        # circular_primes = [int(prime) for prime in primes
        #   if all(prime_r in primes for prime_r in self.rotate(prime))]

    @staticmethod
    def rotate(rotate_str: str) -> list[str]:
        """Returns true if all the rotations of a number
        is also prime. False otherwise.
        """

        return [rotate_str[i:] + rotate_str[:i] for i in range(len(rotate_str))]

    @staticmethod
    def get_primes(limit: int) -> list:
        """Returns list of primes for a given limit"""

        # Return all between 2 to below 1
        # million. Empty list otherwise
        if limit < 2 or limit > 10 ** 6:
            return []

        prime_sieve = [True] * limit

        # limit**0.5 -> square root of limit
        # + 1 for celling value
        for i in range(2, (int(limit ** 0.5) + 1)):
            if prime_sieve[i]:
                for j in range(i * i, limit, i):
                    prime_sieve[j] = False

        return [prime for prime in range(2, limit) if prime_sieve[prime]]


def main():
    solution = Solution()
    limit = int(input())
    circular_primes = solution.get_circular_primes(limit)
    print(sum(circular_primes))


if __name__ == "__main__":
    main()
