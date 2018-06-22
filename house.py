from mcpi.minecraft import Minecraft
from mcpi import block	  

mc = Minecraft.create()
                                            
x, y, z = mc.player.getPos()  
zz = z + 2

mc.setBlocks(x+10, y+3, z+10, x, y, z+5, 5)
mc.setBlocks(x+9, y+2, z+9, x+1, y+1, z+6, 0)
mc.setBlocks(x+1, y+1, z+5, x+1, y+2, z+5, 0)
mc.setBlock(x+1,y,z+4,44)
mc.setBlock(x+9, y+1,z+9,X+1,Y+1,z+9,50)

