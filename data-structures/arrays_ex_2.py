# heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them
#    with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions
# to list down all functions available in list)


# ref: https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md


def main():
    """
    Main method
    """
    heros = ["spider man", "thor", "hulk", "iron man", "captain america"]

    # 1
    print("1. Length of the list: {}".format(len(heros)))

    # 2
    heros.append("black panther")
    print("2. Heros after adding black panther: {}".format(heros))

    # 3
    heros.pop()
    print("3a. Heros after removing black panther: {}".format(heros))
    heros.insert(3, "black panther")
    print("3b. Heros after adding black panther after hulk: {}".format(heros))

    # 4
    heros[1:3] = ["doctor strange"]
    print("4. Heros after adding doctor strange: {}".format(heros))

    # 5
    heros.sort()
    print("5. Heros after sort: {}".format(heros))


if __name__ == "__main__":
    main()
