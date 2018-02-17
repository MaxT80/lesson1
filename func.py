def get_summ(one, two, delimeter='&'):
    return str(one) + str(delimeter) + str(two)
get_summ("hello", "word")
one ="hello"
two ="word"
print(get_summ(one, two).upper())
