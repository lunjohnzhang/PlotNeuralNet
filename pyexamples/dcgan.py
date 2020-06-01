
import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    
    # input
    to_FullConnect("rand", 1, 32, "(1.5,0,0)", to="(0,0,0)", caption="Random Noise \\\\ Input", width=3.5, height=1, depth=1),
    to_ConvBNReLU("conv1", 4, 256, offset="(1.1,0,0)", to="(rand-east)", height=4, depth=4, width=8, caption=" "),
    to_connection("rand", "conv1"),
    to_ConvBNReLU("conv2", 8, 128, offset="(0.8,0,0)", to="(conv1-east)", height=6, depth=6, width=6, caption=" "),
    to_connection("conv1", "conv2"),
    to_ConvBNReLU("conv3", 16, 64, offset="(0.9,0,0)", to="(conv2-east)", height=8, depth=8, width=4, caption=" "),
    to_connection("conv2", "conv3"),
    to_ConvBNReLU("conv4", 32, 8, offset="(0.9,0,0)", to="(conv3-east)", height=10, depth=10, width=1, caption=" "),
    to_connection("conv3", "conv4"),
    to_out(pathfile="zelda_out.png", name="output", offset="1.2", to="(conv4-east)", width=2.5, height=2.5),
    to_Conv("conv5", 32, 8, offset="(2.4,0,0)", to="(conv4-east)", height=10, depth=10, width=1, caption=""),
    to_ConvBNReLU("conv6", 16, 64, offset="(1., 0, 0)", to="(conv5-east)", height=8, depth=8, width=4, caption=""),
    to_connection("conv5", "conv6"),
    to_ConvBNReLU("conv7", 8, 128, offset="(0.8, 0, 0)", to="(conv6-east)", height=6, depth=6, width=6, caption=""),
    to_connection("conv6", "conv7"),
    to_ConvBNReLU("conv8", 4, 256, offset="(0.8, 0, 0)", to="(conv7-east)", height=4, depth=4, width=8, caption=""),
    to_connection("conv7", "conv8"),
    to_Conv("conv9", 1, 1, offset="(0.8, 0, 0)", to="(conv8-east)", height=1, depth=1, width=1, caption=""),
    to_connection("conv8", "conv9"),
    #to_Pool("pool1", offset="(0,0,0)", to="(conv1-east)"),
    #to_Conv("conv2", 128, 64, offset="(1,0,0)", to="(pool1-east)", height=32, depth=32, width=2 ),
    #to_connection( "pool1", "conv2"), 
    #to_Pool("pool2", offset="(0,0,0)", to="(conv2-east)", height=28, depth=28, width=1),
    #to_SoftMax("soft1", 10 ,"(3,0,0)", "(pool1-east)", caption="SOFT"  ),
    #to_connection("pool2", "soft1"),    
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
