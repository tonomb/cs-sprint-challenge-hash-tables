def has_negatives(a):
    
    post = {}
    neg = {}
    repeat = []

    for num in a:
        # check if number is positive
        if num > 0:
            post[num] = num
            num *= -1 
            if num in neg:
                repeat.append(num * -1)
        else:
            neg[num] = num
            num *= -1 
            if num in post:
                repeat.append(num)

    
    return repeat



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
