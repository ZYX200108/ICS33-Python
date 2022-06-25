from performance import Performance
from goody import irange
from graph_goody import random_graph,spanning_tree

# Put script below to generate data for Problem #1
# In case you fail, the data appears in sample8.pdf in the helper folder
def create_random(x):
    global ranDom
    ranDom = random_graph(x,lambda n : 10*n)

for i in irange(0,7):
    y = 1000 * 2 ** i
    p = Performance(lambda: spanning_tree(ranDom), lambda: create_random(y), 5, '\nSpanning Tree of size '+str(y))
    p.evaluate()
    p.analyze()