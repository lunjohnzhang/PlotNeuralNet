
import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),

    # generator
    to_FullConnect("rand", 1, 32, "(1.5,0,0)", to="(0,0,0)", caption="Latent Vector", width=3.5, height=1, depth=1),
    to_ConvBNReLU("conv2", 4, 128, offset="(1.5,0,0)", to="(rand-east)", height=6, depth=6, width=6, caption="BN+ReLU"),
    to_connection("rand", "conv2"),
    to_ConvBNReLU("conv3", 8, 64, offset="(1.5,0,0)", to="(conv2-east)", height=8, depth=8, width=4, caption="BN+ReLU"),
    to_connection("conv2", "conv3"),
    to_ConvBNReLU("conv4", 16, 8, offset="(1.5,0,0)", to="(conv3-east)", height=10, depth=10, width=1, caption="Tanh"),
    to_connection("conv3", "conv4"),
    to_out(pathfile="gen1_basic_6-1.png", name="output", offset="1.5", to="(conv4-east)", width=2.5, height=2.5),

    # discriminator
    to_Conv("conv5", 16, 8, offset="(3.0,0,0)", to="(conv4-east)", height=10, depth=10, width=1, caption="Input Level"),
    to_ConvBNReLU("conv6", 8, 64, offset="(1.5, 0, 0)", to="(conv5-east)", height=8, depth=8, width=4, caption="LeakyReLU"),
    to_connection("conv5", "conv6"),
    to_ConvBNReLU("conv7", 4, 128, offset="(1.5, 0, 0)", to="(conv6-east)", height=6, depth=6, width=6, caption="BN+LeakyReLU"),
    to_connection("conv6", "conv7"),
    to_Conv("conv9", 1, 1, offset="(1.5, 0, 0)", to="(conv7-east)", height=1, depth=1, width=1, caption="Sigmoid"),
    to_connection("conv7", "conv9"),
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
