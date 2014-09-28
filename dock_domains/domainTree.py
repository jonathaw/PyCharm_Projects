from Bio import Phylo
import MySQLdb
from ete2 import Tree
print "hi2"
#tree = Phylo.read('/Users/jonathan/Documents/docks_DB/single_domain/all_docks_domain.dnd', 'newick')

#tree.ladderize()

#Phylo.draw(tree)

IN = open("/Users/jonathan/Documents/docks_DB/single_domain/all_docks_domain.dnd", 'r')
t = file.read(IN)
t = Tree(t)