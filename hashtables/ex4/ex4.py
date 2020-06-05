def has_negatives(a):
    num_dict = {}
    result = []
    for num in a:
        num_dict[num] = None
    for num in a:
        if num > 0:
            if num * -1 in num_dict:
                result.append(num)
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
