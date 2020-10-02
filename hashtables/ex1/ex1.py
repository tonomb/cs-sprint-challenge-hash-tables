

def get_indices_of_item_weights(weights, length, limit):
    check = {}

    # creates check dict
    for i, weight in enumerate(weights):
        if weight not in check:
            check[weight] =  i
        else:
             check[weight] =  i

    for i, weight in enumerate(weights):
        target = limit - weight
        if target in check:
            answer = [i, check[target]]
            answer.sort(reverse=True)
            answer = tuple(answer)
            return answer
    
    return None



weights = [4, 4]
length = 2
limit = 8

print(get_indices_of_item_weights(weights, length, limit))