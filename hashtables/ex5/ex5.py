def finder(files, queries):
    q_dict = {}
    result = []
    for file in files:
        last = file.split("/")[-1]
        if last in q_dict:
            q_dict[last].append(file)
        else:
            q_dict[last] = [file]
    for query in queries:
        if query in q_dict:
            result += [file for file in q_dict[query]]

    return result

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
