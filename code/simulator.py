"""
This simulator should contain the following capabilities...

- to produce random sequences of memmory blocks with different sizes,
- to simulate blocks allocation 
- and generate the number of free fragments as output, 
-- its lowest and highest fragments size as well as the mean fragment size

This simulator should compare the allocation strategies first-fit, next-fit, best-fit and worst-fit.
"""

import random
import strategy as stt

class Simulator:

    def __init__(self, strategy=None, mem_size=10000):
        self.strategy = strategy
        self.mem_size = mem_size
        self.blocks = []
        self.processes = []

    def build_blocks(self, min_block=0.1, max_block=1.0):
        # `min_block` is the min. size of a block given by `min_block/100 * mem_size`
        # `max_block` is the max. size of a block given by `max_block/100 * mem_size`
        #
        # If total size of `blocks` exceeds `mem_size` we crop the last (don't
        # care its size).
        # 
        # If total size of `blocks` is less than `mem_size` we add a new one
        # with its size as the differente between those (don't care its size).

        if len(self.blocks):
            print("Non-empty memory. Try clearing it with `clear_blocks` first.")
            return 

        sum_blocks = 0
        lbs = int(min_block/100 * self.mem_size)
        hbs = int(max_block/100 * self.mem_size)

        while sum_blocks < self.mem_size:
            b = random.randint(lbs, hbs)
            sum_blocks += b
            self.blocks.append(b)

        last = self.mem_size - sum_blocks

        if last > 0:
            self.blocks.append(last)
        elif last < 0:
            self.blocks[-1] += last

    def clear_blocks(self):
        self.blocks = []

    def get_blocks(self):
        return self.blocks

    def build_processes(self, min_proc=0.01, max_proc=1.1, n=100):
        # `min_proc` and `max_proc` define the min and max size that a process
        # could have.

        if len(self.processes):
            print("Non-empty list. Try clearing it with `clear_processes` first.")
            return 

        lps = int(min_proc/100 * self.mem_size)
        hps = int(max_proc/100 * self.mem_size)

        for _ in range(n):
            p = random.randint(lps, hps)
            self.processes.append(p)

    def clear_processes(self):
        self.processes = []

    def get_processes(self):
        return self.processes

    def allocate(self, process):
        pass

