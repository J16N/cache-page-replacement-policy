# let p be the number of pages
p = int(input())
data = list(map(int, input().split()))

# setup empty cache
cache = ['-'] * p
miss = 0

for i, d in enumerate(data):
    # if the data is not in cache...
    if (d not in cache):
        # increment miss counter
        miss += 1
        # If i is equal or greater
        # than p then that means cache 
        # is full and so we need to 
        # remove a element.
        idx = -1
        if (i >= p):
            # Initially the minimum frequency
            # is set to infinity.
            minfreq = float('inf')
            # For each given element in the cache
            # search the one that is going to be
            # used minimum number of times. Store
            # its index.
            for j, v in enumerate(cache):
                freq = data[i+1:].count(v)
                if (minfreq >= freq):
                    minfreq = freq
                    idx = j
        
        # We need to remove the element 
        # that is going to be used least
        # in the future.            
        if (idx > -1):
            cache[idx] = d
        else:
            cache[i] = d
        
    # Display the cache
    print(f"{i + 1:02})", end='\t')
    print(*cache, sep='\t')

print(f"\nTotal Miss = {miss}")
print(f"Total Hits = {len(data) - miss}")
