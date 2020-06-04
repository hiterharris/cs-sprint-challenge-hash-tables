def get_indices_of_item_weights(weights, length, limit):
    index_dict = {}
    for i in range(len(weights)):
        if weights[i] not in index_dict:
            index_dict[weights[i]] = [i]
        else:
            index_dict[weights[i]] += [i]

    for weight in weights:
        if limit - weight in index_dict:
            if weight == limit - weight:
                return [index_dict[weight][1], index_dict[weight][0]]
            if weight > index_dict[limit-weight][0]:
                return [index_dict[limit-weight][0], index_dict[weight][0]]
            else:
                return [index_dict[weight][0], index_dict[limit-weight][0]]
    return None
