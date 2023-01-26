from fractions import Fraction

def nth_term(seq: list) -> str:
    # Finds nth term formula of a sequence.

    def change_int(n):
        # Checks if float is a whole number. If it is, it is changed to an integer.

        if n == int(n):
            return int(n)
        return n

    def find_difference(lst: list) -> list:
        # Finds difference between each item of the list

        difference = list()

        for i in range(len(lst) - 1):
            difference.append(lst[i + 1] - lst [i])

        return difference

    def linear_seq_nth_term(seq: list) -> str:
        # Finds nth term formula of a linear sequence.

        # Finds common difference

        common_diff = seq[1] - seq[0]
        constant = seq[0] - common_diff
        formula = str()

        if common_diff == int(common_diff):
            common_diff = int(common_diff)

        if constant == int(constant):
            constant = int(constant)

        def formula_creator(formula, common_diff, constant) -> str:
            formula += "Un = "

            if common_diff == 1:
                formula += "n"
            elif common_diff == -1:
                formula += "-n"
            elif common_diff != 0:
                formula += f"{common_diff}n"

            if constant > 0:
                formula += f" + {constant}"
            elif constant < 0:
                formula += f" - {abs(constant)}"

            return formula

        formula = formula_creator(formula, common_diff, constant)

        return formula

    def quadratic_seq_nth_term(seq: list) -> str:
        # Finds nth term formula of a quadratic sequence.

        # Finds first and second difference
        first_diff = find_difference(seq)
        second_diff = find_difference(first_diff)

        # Finds a, b, c variables for the formula in the form of Un = an² + bn + c
        a = change_int(second_diff[0] / 2)
        b = change_int(first_diff[0] - (3 * a))
        c = change_int(seq[0] - a - b)

        formula = str()

        def formula_creator(formula: str, a: int, b: int, c: int) -> str:
            # Creates formula, if a variable is 0 it won't show the n thing and if it's 1 it won't show the 1
            # Sooo much junk I had to hide in its own function, sorry :(

            formula += "Un = "

            if a == 1:
                formula += "n²"
            elif a == -1:
                formula += "-n²"
            elif a != 0:
                formula += f"{a}n²"

            if b == 1:
                formula += " + n"
            elif b == -1:
                formula += " - n"
            elif b > 0:
                formula += f" + {b}n"

            elif b < 0:
                formula += f" - {abs(b)}n"

            if c > 0:
                formula += f" + {c}"
            elif c < 0:
                formula += f" - {abs(c)}"

            return formula

        formula = formula_creator(formula, a, b, c)

        return formula

    def cubic_seq_nth_term(seq: list) -> str:
        # Finds nth term formula of a cubic sequence.

        # Finds first, second, and third difference
        first_diff = find_difference(seq)
        second_diff = find_difference(first_diff)
        third_diff = find_difference(second_diff)

        # Finds a, b, c, d variables for the formula in the form of Un = an² + bn + c
        a = change_int(third_diff[0] / 6)
        b = change_int((second_diff[0] - (12 * a)) / 2)
        c = change_int(first_diff[0] - (7 * a) - (3 * b))
        d = change_int(seq[0] - a - b - c)

        formula = str()

        def formula_creator(formula: str, a: int, b: int, c: int, d: int) -> str:
            # Creates formula, if a variable is 0 it won't show the n thing and if it's 1 it won't show the 1
            # Sooo much junk I had to hide in its own function, sorry :(

            formula += "Un = "

            if a == 1:
                formula += "n³"
            elif a == -1:
                formula += "-n³"
            elif a != 0:
                formula += f"{a}n³"

            if b == 1:
                formula += " + n²"
            elif b == -1:
                formula += " - n²"
            elif b > 0:
                formula += f" + {b}n²"
            elif b < 0:
                formula += f" - {abs(b)}n²"

            if c == 1:
                formula += " + n"
            elif c == -1:
                formula += " - n"
            elif c > 0:
                formula += f" + {c}n"
            elif c < 0:
                formula += f" - {abs(c)}n"

            if d > 0:
                formula += f" + {d}"
            elif d < 0:
                formula += f" - {abs(d)}"

            return formula

        formula = formula_creator(formula, a, b, c, d)

        return formula

    def exponential_seq_nth_term(seq: list) -> str:
        # Finds nth term formula of a cubic sequence.

        # Finds the ratio between the first and second term of the sequence.
        common_ratio = seq[1] / seq[0]

        # Checks if common ratio is a whole number or a fraction.

        if common_ratio == int(common_ratio):
            common_ratio = int(common_ratio)
        else:
            common_ratio = str(Fraction(common_ratio).limit_denominator())

        # If the first term of the sequence is 1, then it will not include it in the formula.
        if seq[0] == 1:
            formula = formula = f"Un = {common_ratio}ⁿ ⁻ ¹"
        else:
            formula = f"Un = {change_int(seq[0])} x {common_ratio}ⁿ ⁻ ¹"

        return formula

    first_diff = find_difference(seq)

    if first_diff[0] == first_diff[1]:
        return linear_seq_nth_term(seq)

    second_diff = find_difference(first_diff)

    if second_diff[0] == second_diff[1]:
       return quadratic_seq_nth_term(seq)

    third_diff = find_difference(second_diff)

    if third_diff [0] == third_diff[1]:
        return cubic_seq_nth_term(seq)

    if seq[1] / seq[0] == seq[2] / seq[1]:
        return exponential_seq_nth_term(seq)

    return "Type of sequence not identified."

# SMH