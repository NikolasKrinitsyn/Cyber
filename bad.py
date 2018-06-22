from mcpi.minecraft import Minecraft
from mcpi import block	  

mc = Minecraft.create('10.183.0.33', 4711)
                                            
x, y, z = mc.player.getPos()  
zz = z + 2

mc.setBlocks(x+1000, y+1000, z+1000, x-1000, y-1000, z-1000, 0)

