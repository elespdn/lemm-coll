
# COLLATE THE LEMMAS
W1 = open("C:/Users/Elena/Documents/example-8wss/W1.txt").read()
W2 = open("C:/Users/Elena/Documents/example-8wss/W2.txt").read()
W3 = open("C:/Users/Elena/Documents/example-8wss/W3.txt").read()
W4 = open("C:/Users/Elena/Documents/example-8wss/W4.txt").read()
W5 = open("C:/Users/Elena/Documents/example-8wss/W5.txt").read()
W6 = open("C:/Users/Elena/Documents/example-8wss/W6.txt").read()
W7 = open("C:/Users/Elena/Documents/example-8wss/W7.txt").read()
W8 = open("C:/Users/Elena/Documents/example-8wss/W8.txt").read()
outfile = open('C:/Users/Elena/Documents/example-8wss/collation-output-original.txt', 'w', encoding='utf-8')

from collatex import *

collation = Collation()

collation.add_plain_witness('W1', W1)
collation.add_plain_witness('W2', W2)
collation.add_plain_witness('W3', W3)
collation.add_plain_witness('W4', W4)
collation.add_plain_witness('W5', W5)
collation.add_plain_witness('W6', W6)
collation.add_plain_witness('W6', W7)
collation.add_plain_witness('W8', W8)


alignment_table = collate(collation, segmentation=False)
print(alignment_table, file=outfile)
outfile.close()


