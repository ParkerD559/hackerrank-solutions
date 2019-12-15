regex_integer_in_range = r"^[1-9][0-9]{5}$"  # [100000, 999999]
regex_alternating_repetitive_digit_pair = (
    r"(.)(?=[^\1]\1)"  # Alternating repetitions (xx1x1x)
)
