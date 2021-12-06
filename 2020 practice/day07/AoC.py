import sys

# Handy Haversacks

def basebag(count:str):
    if count.strip() == "no":
        return 0
    else:
        return int(count)

# bag is the item to start from
# item is the item we are looking for
# bagmap is the dictionary of bags and what they can contain
# list is a list of all the bags we have found so far that contain item
def contains(bag:str, item:str, bagmap:dict, cache:dict):
    # no other bags means this is a base case
    if bag == item:
        return True
    if bag == "other": # base case bag
        return False
    if bag in cache:
        return cache[bag] # either true or false
    # if not already found, create a call for each of the sub bags
    cache[bag] = any([contains(b, item, bagmap, cache) for b in bagmap[bag]])
    return cache[bag]

# find the number of bags that a bag must contain
def countbags(bag:str, bagmap:dict, cache:dict):
    if bag == "other": # base case bag
        return 0
    if bag in cache:
        return cache[bag] # either true or false
    # if not already found, create a call for each of the sub bags
    cache[bag] = sum([(countbags(b, bagmap, cache) + 1) * bagmap[bag][b] for b in bagmap[bag]])
    return cache[bag]

def main():
    # start by getting file as a list of strings
    f = [l.replace(" bags", "").replace(" bag", "").replace(".", "").strip() for l in open(sys.argv[1], 'r')]

    # each line is separated by " contain " 
    bags = [l.split(" contain ")[0] for l in f]
    # each bag has a list of contents
    contents = [l.split(" contain ")[1].split(", ") for l in f]
    contents = [{v.strip():basebag(k) for k,v in [c.split(" ", 1) for c in l]} for l in contents]

    # the bagmap is a dictionary of bags and what they can contain
    bagmap = {b:c for b,c in zip(bags, contents)}

    cache = {}  # record all bags that contain gold, key=true if yes, false if no (prevents loops)
    # cache will be a dictionary of bags and what they can contain
    for b in bagmap:
        contains(b, "shiny gold", bagmap, cache) # call with the cache for all bags, cache will prevent repeated calculations

    # PART 1
    # this is a recursive algotithm, we follow the path of bags to calculate how many base bags we have
    # count the number of bags that contain gold
    print(sum([1 for b in cache if cache[b]]))

    # PART 2
    cache = {}
    print(countbags("shiny gold", bagmap, cache))

# I need to get into the habit of using the main function
if __name__ == "__main__":
    main()