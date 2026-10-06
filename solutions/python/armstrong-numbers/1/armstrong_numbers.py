def is_armstrong_number(number):
    digit_str=str(number)
    find_length=len(digit_str)
    k=0
    for i in digit_str:
        conversion=int(i)
        total = conversion ** find_length
        k += total
    return k == number 

    
