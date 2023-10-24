import sys

sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head('..'),
    to_cor(),
    to_begin(),
    # to_out(pathfile="kiva_small_60_agents_opt_unrepaired",
    #        name="output1",
    #        offset="1.5",
    #     #    to="(conv4-east)",
    #        width=2.5,
    #        height=2.5),
    # to_out(pathfile="kiva_small_60_agents_opt",
    #        name="output2",
    #        offset="1.5",
    #     #    to="(conv4-east)",
    #        width=2.5,
    #        height=2.5),
    # to_out(pathfile="kiva_small_dsage_opt_tile-usage",
    #        name="output3",
    #        offset="1.5",
    #     #    to="(conv4-east)",
    #        width=2.5,
    #        height=2.5),
    to_Conv("conv1",
            4,
            256,
            offset="(1.5,0,0)",
            # to="(conv2-east)",
            height=5,
            depth=5,
            width=30),
    # to_Conv("conv2",
    #         32,
    #         64,
    #         offset="(1.5,0,0)",
    #         # to="(conv2)",
    #         height=10,
    #         depth=10,
    #         width=3.5),
    # to_connection("conv2", "conv1"),
    to_end()
]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()
