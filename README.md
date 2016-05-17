Problem: spelling variation when collating medieval text.
---------------------------------------------------------

**Different approaches have been tried**:
- "normalize" changing into a standard form just for the purpose of the collation
- consider different kind of matches; not only agreement or disagreement, but also what has been called fuzzy match based on the edit distance among the words.

Another approach is made possible only recently by the development of modules for **automatic lemmatization of medieval texts**.

Considering **old French**, there are two parameter files available for TreeTagger (an open source tool for annotating text with part-of-speech and lemma information)
--> the Stein parameter file
--> the BFM parameter file (for POS annotations, not for lemmatization)

NEW PROPOSAL:
-------------
1. lemmatize
2. collate the lemmas, instead of the original forms
(For more details, see the examples)


Check **prerequisites.txt**