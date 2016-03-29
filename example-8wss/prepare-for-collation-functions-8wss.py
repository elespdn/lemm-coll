
import treetaggerwrapper, os, re


# create a folder where to store intermediate results.
# They can be used for refining the data in between.
try:
    os.makedirs('C:/Users/Elena/Documents/example-8wss/halfway')
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
                ('\|.*', ''),
                ('ï¿½', 'e')]
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


# WSSin = 'C:/Users/Elena/Documents/example-8wss/WSSin'
# I have tried to put all the input file into one folder and point to that one,
# instead of specifying the single files, but this way it does not work

W1in = 'C:/Users/Elena/Documents/example-8wss/W1.txt'
W2in = 'C:/Users/Elena/Documents/example-8wss/W2.txt'
W3in = 'C:/Users/Elena/Documents/example-8wss/W3.txt'
W4in = 'C:/Users/Elena/Documents/example-8wss/W4.txt'
W5in = 'C:/Users/Elena/Documents/example-8wss/W5.txt'
W6in = 'C:/Users/Elena/Documents/example-8wss/W6.txt'
W7in = 'C:/Users/Elena/Documents/example-8wss/W7.txt'
W8in = 'C:/Users/Elena/Documents/example-8wss/W8.txt'
WSSin = [W1in, W2in, W3in, W4in, W5in, W6in, W7in, W8in]

W1out = 'C:/Users/Elena/Documents/example-8wss/halfway/W1-lemmatized.txt'
W2out = 'C:/Users/Elena/Documents/example-8wss/halfway/W2-lemmatized.txt'
W3out = 'C:/Users/Elena/Documents/example-8wss/halfway/W3-lemmatized.txt'
W4out = 'C:/Users/Elena/Documents/example-8wss/halfway/W4-lemmatized.txt'
W5out = 'C:/Users/Elena/Documents/example-8wss/halfway/W5-lemmatized.txt'
W6out = 'C:/Users/Elena/Documents/example-8wss/halfway/W6-lemmatized.txt'
W7out = 'C:/Users/Elena/Documents/example-8wss/halfway/W7-lemmatized.txt'
W8out = 'C:/Users/Elena/Documents/example-8wss/halfway/W8-lemmatized.txt'
WSSout = [W1out, W2out, W3out, W4out, W5out, W6out, W7out, W8out]

W1out_clean = 'C:/Users/Elena/Documents/example-8wss/halfway/W1-lemmatized-clean.txt'
W2out_clean = 'C:/Users/Elena/Documents/example-8wss/halfway/W2-lemmatized-clean.txt'
W3out_clean = 'C:/Users/Elena/Documents/example-8wss/halfway/W3-lemmatized-clean.txt'
W4out_clean = 'C:/Users/Elena/Documents/example-8wss/halfway/W4-lemmatized-clean.txt'
W5out_clean = 'C:/Users/Elena/Documents/example-8wss/halfway/W5-lemmatized-clean.txt'
W6out_clean = 'C:/Users/Elena/Documents/example-8wss/halfway/W6-lemmatized-clean.txt'
W7out_clean = 'C:/Users/Elena/Documents/example-8wss/halfway/W7-lemmatized-clean.txt'
W8out_clean = 'C:/Users/Elena/Documents/example-8wss/halfway/W8-lemmatized-clean.txt'
WSSout_clean = [W1out_clean, W2out_clean, W3out_clean, W4out_clean, W5out_clean, W6out_clean, W7out_clean, W8out_clean]

W1out_lemmas = 'C:/Users/Elena/Documents/example-8wss/halfway/W1-lemmas.txt'
W2out_lemmas = 'C:/Users/Elena/Documents/example-8wss/halfway/W2-lemmas.txt'
W3out_lemmas = 'C:/Users/Elena/Documents/example-8wss/halfway/W3-lemmas.txt'
W4out_lemmas = 'C:/Users/Elena/Documents/example-8wss/halfway/W4-lemmas.txt'
W5out_lemmas = 'C:/Users/Elena/Documents/example-8wss/halfway/W5-lemmas.txt'
W6out_lemmas = 'C:/Users/Elena/Documents/example-8wss/halfway/W6-lemmas.txt'
W7out_lemmas = 'C:/Users/Elena/Documents/example-8wss/halfway/W7-lemmas.txt'
W8out_lemmas = 'C:/Users/Elena/Documents/example-8wss/halfway/W8-lemmas.txt'
WSSout_lemmas = [W1out_lemmas, W2out_lemmas, W3out_lemmas, W4out_lemmas, W5out_lemmas, W6out_lemmas, W7out_lemmas, W8out_lemmas]



lemmatization(WSSin, WSSout)

clean(WSSout, WSSout_clean)

extract_lemmas(WSSout_clean, WSSout_lemmas)