
import treetaggerwrapper, os, re


# create a folder where to store intermediate results.
# They can be used for refining the data in between.
try:
    os.makedirs('C:/Users/Elena/Documents/example-3wss/halfway')
except OSError:
    pass


def lemmatization(indir, outdir):
    for infile, outfile in zip(indir, outdir):
            open(outfile, 'w', encoding='utf-8')
            tagger = treetaggerwrapper.TreeTagger(TAGLANG='stein')
            tagger.tag_file_to(infile, outfile)


# CLEAN THE OUTPUT OF THE LEMMATIZATION
# ('_.*', ''),
# ('\d', '')

def clean(indir, outdir):
    patterns = [('_.*', ''),
                ('\d.*', ''),
                ('\|.*', '')]
    for infile, outfile in zip(indir, outdir):
        t = open(infile).read()

        for (p1,p2) in patterns:
            print(p1)
            p = re.compile(p1)
            t = p.sub(p2, t)

        o = open(outfile, 'w', encoding='utf-8')
        o.write(t)
        o.close()


# EXTRACT ONLY THE LEMMAS
def extract_lemmas(indir, outdir):
    for infile, outfile in zip(indir, outdir):
        infile = open(infile, 'r')
        outfile = open(outfile, 'w')
        for aline in infile:
            values = aline.split()
            lemmas = values[2]
            outfile.write(lemmas + '\n')

        infile.close()
        outfile.close()


# WSSin = 'C:/Users/Elena/Documents/example-3wss/WSSin'
# I have tried to put all the input file into one folder and point to that one,
# instead of specifying the single files, but this way it does not work

W1in = 'C:/Users/Elena/Documents/example-3wss/W1.txt'
W2in = 'C:/Users/Elena/Documents/example-3wss/W2.txt'
W3in = 'C:/Users/Elena/Documents/example-3wss/W3.txt'
WSSin = [W1in, W2in, W3in]

W1out = 'C:/Users/Elena/Documents/example-3wss/halfway/W1-lemmatized.txt'
W2out = 'C:/Users/Elena/Documents/example-3wss/halfway/W2-lemmatized.txt'
W3out = 'C:/Users/Elena/Documents/example-3wss/halfway/W3-lemmatized.txt'
WSSout = [W1out, W2out, W3out]

W1out_clean = 'C:/Users/Elena/Documents/example-3wss/halfway/W1-lemmatized-clean.txt'
W2out_clean = 'C:/Users/Elena/Documents/example-3wss/halfway/W2-lemmatized-clean.txt'
W3out_clean = 'C:/Users/Elena/Documents/example-3wss/halfway/W3-lemmatized-clean.txt'
WSSout_clean = [W1out_clean, W2out_clean, W3out_clean]

W1out_lemmas = 'C:/Users/Elena/Documents/example-3wss/halfway/W1-lemmas.txt'
W2out_lemmas = 'C:/Users/Elena/Documents/example-3wss/halfway/W2-lemmas.txt'
W3out_lemmas = 'C:/Users/Elena/Documents/example-3wss/halfway/W3-lemmas.txt'
WSSout_lemmas = [W1out_lemmas, W2out_lemmas, W3out_lemmas]



lemmatization(WSSin, WSSout)

clean(WSSout, WSSout_clean)

extract_lemmas(WSSout_clean, WSSout_lemmas)