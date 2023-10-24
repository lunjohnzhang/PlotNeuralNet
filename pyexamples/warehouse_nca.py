import sys

sys.path.append('../')
from pycore.tikzeng import *

# WarehouseNCA(
#   (model): Sequential(
#     (initial:conv:in_chan-32): Conv2d(3, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
#     (initial:relu): ReLU(inplace=True)
#     (internal1:conv:32-32): Conv2d(32, 32, kernel_size=(1, 1), stride=(1, 1))
#     (internal1:relu): ReLU(inplace=True)
#     (internal2:conv:32-3): Conv2d(32, 3, kernel_size=(1, 1), stride=(1, 1))
#     (internal2:sigmoid): Sigmoid()
#   )
# )

# defined your arch
arch = [
    to_head('..'),
    to_cor(),
    to_begin(),
    to_input(
        pathfile="../assets/warehouse_nca/kiva_large_seed_block.png",
        name="input-env",
        #  to="(conv4-east)",
        width=4.5,
        height=4.5),
    to_Conv(
        "conv1",
        32,
        3,  # n-channels
        offset="(4,0,0)",
        to="(input-env)",
        height=20,
        depth=20,
        width=2),
    to_Conv("conv2",
            32,
            32,
            offset="(4,0,0)",
            to="(conv1-east)",
            height=20,
            depth=20,
            width=20),
    to_connection("conv1", "conv2"),
    to_Conv("conv3",
            32,
            32,
            offset="(4,0,0)",
            to="(conv2-east)",
            height=20,
            depth=20,
            width=20),
    to_connection("conv2", "conv3"),
    to_Conv("conv4",
            32,
            3,
            offset="(4,0,0)",
            to="(conv3-east)",
            height=20,
            depth=20,
            width=2),
    to_connection("conv3", "conv4"),
    # to_Conv("conv5",
    #         32,
    #         3,
    #         offset="(4,0,0)",
    #         to="(conv4-east)",
    #         height=20,
    #         depth=20,
    #         width=2),
    # to_connection("conv4", "conv5"),
    to_out(pathfile="../assets/warehouse_nca/gen_0049.png",
           name="output-env",
           offset="4",
           to="(conv4-east)",
           width=4.5,
           height=4.5),
    to_skip("conv4", "conv1", 1.5),
    # to_connection("conv4", "conv1"),
    to_end()
]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()
