
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
    # iterate throught blocks searching by the first block
    # with the minimum size which is less or equal the process size

    p_sz = process[1]

    # find first min block sz >= p_sz
    pos = -1
    fg_sz = -1
    best = max(blocks)
    for i in range(len(blocks)):
        if p_sz <= blocks[i] and i not in mapping.keys():
            if best > blocks[i]:
                best = blocks[i]
                pos = i
                fg_sz = best - p_sz

    return pos, fg_sz


def worst_fit(process, blocks, mapping):
    pass

