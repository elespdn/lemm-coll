Question: how to deal with spelling variation when collating medieval texts?
----------------------------------------------------------------------------

**Different approaches have been tried**:
- "normalize", i.e. changing into a standard form just for the purpose of the collation
- consider different kind of matches: not only agreement or disagreement, but also what has been called fuzzy match based on the edit distance among the words.

Another approach is recently made possible by the development of **NLP resources for medieval languages**.

Considering **old French**, there are two modules available for TreeTagger (an open source tool using decision trees for annotating text with part-of-speech and lemma information)
* the Stein parameter file (for POS annotation and lemmatization)
* the BFM parameter file (for POS annotations, not for lemmatization)

Proposal:
---------
1. lemmatize
2. collate the lemmas, instead of the original forms

For more details, see the **examples**.
Before testing, have a look at  prerequisites.txt