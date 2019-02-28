
from simulator import Simulator


def main():
    s = Simulator(strategy='first_fit')

    s.build_blocks()
    s.build_processes()

    procs = s.get_processes()

    for p in procs:
        s.allocate(p)

    print(s.map_proc_to_block)


main()
