import __main__
__main__.pymol_argv = ['pymol','-qc'] # Pymol: quiet and no GUI
import pymol
from pymol import cmd
pymol.finish_launching()

print 'ffff'
cmd.fetch('1ahw')
cmd.fetch('1x9q')
cmd.align('1ahw', '1x9q')
cmd.save('temp')
print 'peirjfg'