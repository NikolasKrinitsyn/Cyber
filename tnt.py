from mcpi.minecraft import Minecraft
from mcpi import block	  

mc = Minecraft.create('10.183.0.33', 4711)
                                            
x, y, z = mc.player.getPos()  
zz = z + 2

mc.setBlocks(x+100, y+100, z+100, x, y, z+1, 46, 1)

