
# COLLATE THE LEMMAS
W1 = open("C:/Users/Elena/Documents/example-3wss/W1.txt").read()
W2 = open("C:/Users/Elena/Documents/example-3wss/W2.txt").read()
W3 = open("C:/Users/Elena/Documents/example-3wss/W3.txt").read()
outfile = open('C:/Users/Elena/Documents/example-3wss/collation-output-original.txt', 'w', encoding='utf-8')

from collatex import *

collation = Collation()

collation.add_plain_witness('W1', W1)
collation.add_plain_witness('W2', W2)
collation.add_plain_witness('W3', W3)


alignment_table = collate(collation, segmentation=False)
print(alignment_table, file=outfile)
outfile.close()


