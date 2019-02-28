
from simulator import Simulator


def main():
    s = Simulator(strategy='first_fit')

    s.build_blocks()
    s.build_processes()

    blocks = s.get_blocks()
    procs = s.get_processes()


    for p in procs:
        s.allocate(p)

    print(s.map_proc_to_block)

    print('{} blocks\n{} processes'.format(len(blocks), len(procs)))

    frags_info = s.generate_fragments_info()
    print('SUMMARY')
    print('{} free fragments\n{} lowest\n{} highest\n{} mean size'.
            format(frags_info[0],
                   frags_info[1],
                   frags_info[2],
                   frags_info[3]))


main()
