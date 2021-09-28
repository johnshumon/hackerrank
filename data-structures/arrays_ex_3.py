# Create a list of all odd numbers between 1 and a max number.
# Max number is something you need to take from a user using input() function


# ref: https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md


def main():
    """
    Main method
    """
    while True:
        try:
            upper_bound = int(input("Enter a number between 0 & 1 million: "))

        except ValueError:
            print("Input should be a number.")
            continue

        if upper_bound < 0 or upper_bound > 10 ** 9:
            print("Input value is either too low or too high. Try again")
            continue

        break

    odd_numbers = []
    for i in range(upper_bound):
        if i % 2 != 0:
            odd_numbers.append(i)

    print("Odd numbers in given range: {}".format(odd_numbers))


if __name__ == "__main__":
    main()
