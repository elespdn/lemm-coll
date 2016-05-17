Question: how to deal with spelling variation when collating medieval texts?
----------------------------------------------------------------------------

**Different approaches have been tried**:
- normalize, i.e. changing into a standard form just for the purpose of the collation
- consider different kind of matches: not only agreement or disagreement, but also what has been called *fuzzy match*, based on the edit distance among the words.

Another approach is recently made possible by the development of **NLP resources for medieval languages**.

Considering **old French**, there are two modules available for [TreeTagger] (http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/), which is an open source tool using decision trees for annotating text with part-of-speech and lemma information. The two modules are based respectively upon:
* the [Nouveau corpus d’Amsterdam] (http://www.uni-stuttgart.de/lingrom/stein/corpus) and it provides POS annotation and lemma (*stein* parameter file)
* the [Base de français médiéval] (http://txm.bfm-corpus.org) and it provides POS annotation (mainly used in [TXM] (http://textometrie.ens-lyon.fr/?lang=en)).

The joint effort of the two équipes are now available in the Github repository [Medieval French Language Toolkit] (https://github.com/sheiden/Medieval-French-Language-Toolkit).

Proposal:
---------
1. **lemmatize the texts**. For this task, you can use the *stein* parameter file in TreeTagger
2. **collate the lemmas**, instead of the original forms.

For more details, have a look at *prerequisites.txt*

and at the **examples**.