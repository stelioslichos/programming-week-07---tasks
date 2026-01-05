def base_10_convertor_rec(num_string, convert_from_base):
    if num_string == "":
        return 0
    else:
        first_dig = int(num_string[0])
        power = len(num_string) - 1
        dig_value = first_dig * convert_from_base ** power
    return dig_value + base_10_convertor_rec(num_string[1:], convert_from_base)

if __name__ == "__main__":
    print(base_10_convertor_rec("1011", 2)) # prints 11
    print(base_10_convertor_rec("00341", 5)) # prints 96
    print(base_10_convertor_rec("00341", 6)) # prints 133
    print(base_10_convertor_rec("00341", 10)) # prints 341