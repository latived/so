
def first_fit(process, blocks, mapping):
    # iterate through blocks searching by the first block that isn't allocated
    # and have its size less or equal process size

    p_sz = process[1]

    for i in range(len(blocks)):
        if p_sz <= blocks[i] and i not in mapping.keys():
            return i, blocks[i] - p_sz  # pos, fg_sz

    return -1, -1

def next_fit(process, blocks, mapping):
    pass

def best_fit(process, blocks, mapping):
    pass

def worst_fit(process, blocks, mapping):
    pass

