from collections import deque

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
        print(*s, sep='\t')
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
cache = [deque("-" * k, maxlen=k) for _ in range(n)]
    
miss = 0
total = 0
# Start putting data into the cache
for i, d in enumerate(data):
    print(f"Step-{i + 1}")
    s = cache[d % n] if len(cache) > 1 else cache[0]
    # Check whether d is in 
    # the set. If not include
    # it and increment the 
    # miss counter
    if d not in s:
        miss += 1
        s.append(d)
    
    display(cache)
    #print a newline
    print()
    total += 1
    
print(f"Total Miss = {miss}")
print(f"Total Hits = {total - miss}")
