import sys


def part1(G: dict, path: list = None, visited: list = None) -> list:
    # e is a list of edges
    # v is a list of vertices
    # lowercase names can be visited once, and are added to visited
    if visited is None:
        visited = ['start']
    if path is None:
        path = ['start']
    here = path[-1]
    if here == 'end':
        return [path]
    paths = []
    if here not in visited and here.islower():
        visited.append(here)  # only add lowercase vertices to visited
    for v in G[here]:
        if v not in visited:
            paths += part1(G, path + [v], visited.copy())
    # dead ends are not added to paths
    return paths

# part 2 is same as part 1, except each small cave can be visited twice


def part2(G: dict, path: list = None, visited: dict = None) -> list:
    # e is a list of edges
    # v is a list of vertices
    # only lowercase names can be visited once, and are added to visited

    # first call setup
    if visited is None:
        # set start as visited twice
        visited = {i: 0 for i in G.keys() if i.islower()}
        # will become 3 after first pass, must not be visited again
        visited['start'] = 2
        visited.pop('end')
    if path is None:
        path = ['start']
    # it is faster to copy the string of where I am
    here = path[-1]
    # base case is end cave
    if here == 'end':
        return [path]
    # increment the number of times this vertex has been visited, if a small cave
    if here.islower():
        visited[here] += 1
    # for each vertex not an end cave, create a list of paths of where to go from here
    paths = []
    # visit each vertex connected to here, if conditions are met
    for v in G[here]:
        # only visit one small cave twice, the rest can only be visited once
        if v not in visited or (visited[v] < 2 if not any(val == 2 for val in visited.values()) else visited[v] < 1):
            paths += part2(G, path + [v], visited.copy())
    # return all path possibilities from here
    return paths


def main():
    e = [tuple(l.strip().split("-")) for l in open(sys.argv[1], 'r')]
    v = {vertex for edge in e for vertex in edge}
    G = {vertex: [(edge[0] if edge[1] == vertex else edge[1])
                  for edge in e if vertex in edge] for vertex in v}

    print(len(part1(G)))
    print(len(part2(G)))


# I need to get into the habit of using the main function
if __name__ == "__main__":
    main()
