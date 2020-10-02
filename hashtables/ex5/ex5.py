# Your code here



def finder(files, queries):
    paths = {}
    results = []
    for path in files:
        file = path.split('/')
        if file[-1] not in paths:
            paths[file[-1]] = []
            paths[file[-1]].append(path)
        else:
            paths[file[-1]].append(path)


    for querie in queries:
        if querie in paths:
            for p in paths[querie]:
                results.append(p)

    return results




files = [
    "/usr/local/share/foo.txt",
    "/usr/bin/ls",
    "/home/davidlightman/foo.txt",
    "/bin/su"
]

queries = [
    "ls",
    "foo.txt",
    "nosuchfile.txt"
]

print(finder(files, queries))
# if __name__ == "__main__":
#     files = [
#         '/bin/foo',
#         '/bin/bar',
#         '/usr/bin/baz'
#     ]
#     queries = [
#         "foo",
#         "qux",
#         "baz"
#     ]
#     print(finder(files, queries))
