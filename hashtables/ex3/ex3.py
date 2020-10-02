def intersection(arrays):
   
    check = {}

    length = len(arrays)

    intersection ={}
   
    for num in arrays[0]:
        check[num] = num

    # check if array has a number in check
    for i in range(length-1):
        for num in arrays[i +1]:
            if num in check:
                intersection[num] = True

    intersection = list(intersection)
    return intersection
    


# arrays = [
#     [1, 2, 3, 4, 5],
#     [12, 7, 2, 9, 1],
#     [99, 2, 7, 1,]
# ]

# print(intersection(arrays))

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
