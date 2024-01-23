#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    elements_printed = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            elements_printed += 1
    except IndexError:
        pass  # Ignore the IndexError if we go beyond the length of the list

    print()  # Print a new line after all elements have been printed
    return elements_printed

# Example usage
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
