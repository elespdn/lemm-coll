
# COLLATE THE LEMMAS
W1 = open("C:/Users/Elena/Documents/example-3wss/halfway/W1-lemmas.txt").read()
W2 = open("C:/Users/Elena/Documents/example-3wss/halfway/W2-lemmas.txt").read()
W3 = open("C:/Users/Elena/Documents/example-3wss/halfway/W3-lemmas.txt").read()
outfile = open('C:/Users/Elena/Documents/example-3wss/collation-output-lemmas.txt', 'w', encoding='utf-8')

from collatex import *

collation = Collation()

collation.add_plain_witness('W1', W1)
collation.add_plain_witness('W2', W2)
collation.add_plain_witness('W3', W3)

alignment_table = collate(collation, segmentation=False)
print(alignment_table, file=outfile)
outfile.close()


