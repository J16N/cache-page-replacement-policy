def display(cache):
    """
        @description
          Display the given cache
        
        @parameter
          cache : Cache to be displayed
        
        @return
          This function does not return anything
    """
    for i, s in enumerate(cache):
        print(f"\tSet-{i + 1}:", end='\t')
        print(*list(s), sep='\t')
    # print a newline
    print()


# Let s be total cache size,
# k be the number of blocks 
# in each set and n be the total
# number of sets
s, k = map(int, input().split())
data = map(int, input().split())
n = s // k

# Initialize the cache
cache = [
    {'-': 0 for _ in range(k)} 
    for _ in range(n)
]
    
miss = 0
total = 0
# Start putting data into the cache
for i, d in enumerate(data):
    print(f"Step-{i + 1}")
    s = cache[d % n]
    # Update the miss counter when the
    # data is not in the cache
    if (not s.get(d)):
        miss += 1
        
    # Remove the item with lowest priority
    # once the cache is filled
    if (len(s) == k):
        s.pop(list(s)[0])
    
    # Insert data to the cache along with
    # its priority and sort the cache from
    # the item with the lowest priority to 
    # the item with the highest priority.
    s[d] = i + 1
    s = sorted(s, key=s.get)
    display(cache)
    print()
    total += 1

print(f"Total Miss = {miss}")
print(f"Total Hits = {total - miss}")
