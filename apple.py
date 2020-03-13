# Simple Pythong lines: Fibonacci, tuple assignment
parents, babies = (1, 1)
while babies < 450:
    print ('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)
