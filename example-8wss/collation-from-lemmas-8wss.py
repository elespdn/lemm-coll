
# COLLATE THE LEMMAS
W1 = open("C:/Users/Elena/Documents/example-8wss/halfway/W1-lemmas.txt").read()
W2 = open("C:/Users/Elena/Documents/example-8wss/halfway/W2-lemmas.txt").read()
W3 = open("C:/Users/Elena/Documents/example-8wss/halfway/W3-lemmas.txt").read()
W4 = open("C:/Users/Elena/Documents/example-8wss/halfway/W4-lemmas.txt").read()
W5 = open("C:/Users/Elena/Documents/example-8wss/halfway/W5-lemmas.txt").read()
W6 = open("C:/Users/Elena/Documents/example-8wss/halfway/W6-lemmas.txt").read()
W7 = open("C:/Users/Elena/Documents/example-8wss/halfway/W7-lemmas.txt").read()
W8 = open("C:/Users/Elena/Documents/example-8wss/halfway/W8-lemmas.txt").read()
outfile = open('C:/Users/Elena/Documents/example-8wss/collation-output-lemmas.txt', 'w', encoding='utf-8')

from collatex import *

collation = Collation()

collation.add_plain_witness('W1', W1)
collation.add_plain_witness('W2', W2)
collation.add_plain_witness('W3', W3)
collation.add_plain_witness('W4', W4)
collation.add_plain_witness('W5', W5)
collation.add_plain_witness('W6', W6)
collation.add_plain_witness('W7', W7)
collation.add_plain_witness('W8', W8)


alignment_table = collate(collation, segmentation=False)
print(alignment_table, file=outfile)
outfile.close()


