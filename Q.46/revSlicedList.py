
# Python program to slice list into 3 chunks and reverse each chunks

# User-defined function to split the list into chunks and return it one by one
def rev_list_chunks(list_items):
    chunk_size = 3
    for i in range(0, len(list_items), chunk_size):
        yield list_items[i:i + chunk_size]
        # yield keyword will be responsible for returning the chunk and will resume
        # exactly from where it left off(it's last state)


list_1 = [11, 45, 8, 23, 14, 12, 78, 45, 89]
res = list(rev_list_chunks(list_1))
print("Sliced List into 3 chunks:", res)
rev_chunks = [x[::-1] for x in res]  # Variable holding the chunks of list in reversed order
print("Reversed Chunks:", rev_chunks)