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



### PREREQUISITES

1. INSTALL TREE TAGGER
	at [www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/] (http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/)


2. INSTALL THE STEIN PARAMETER FILE
	* for lemmatization and POS annotation of ancient French at [www.uni-stuttgart.de/lingrom/stein/#sec:ressourcen] (http://www.uni-stuttgart.de/lingrom/stein/#sec:ressourcen) 
	
	* or directly at [www.uni-stuttgart.de/lingrom/stein/downloads/stein-oldfrench.par.zip] (http://www.uni-stuttgart.de/lingrom/stein/downloads/stein-oldfrench.par.zip)


3. INSTALL TREETAGGERWRAPPER
	* (full doc at [treetaggerwrapper.readthedocs.org/en/latest/] (http://treetaggerwrapper.readthedocs.org/en/latest/) )
	pip install treetaggerwrapper
	
	* (In order to have treetaggerwrapper working, you may need to install the six module as well)
	pip install six


4. ADD SPECIFICATION FOR ANCIENT FRENCH (STEIN MODULE) 
	* in 'treetaggerwrapper.py' (for example Python34\Lib\site-packages\treetaggerwrapper.py)
	after line 594 (or anywhere among the languages in g_langsupport = {}  )

	
    "stein": {
        "encoding": "utf-8",
        "tagparfile": "stein-utf8.par",
        "abbrevfile": "french-abbreviations-utf8",
        "pchar": ALONEMARKS + "'",
        "fchar": ALONEMARKS + "'",
        "pclictic": "[dcjlmnstDCJLNMST]'|[Qq]u'|[Jj]usqu'|[Ll]orsqu'",
        "fclictic": "'-t-elles|-t-ils|-t-on|-ce|-elles|-ils|-je|-la|"
					"-les|-leur|-lui|-mêmes|-memes|-même|-meme|-m'|-moi|-on|-toi|-tu|-t'|"
					"-vous|-en|-y|-ci|-là|-la",
		"number": NUMBER_EXPRESSION,
		"dummysentence": "Pas d'ancien français. Cela est une phrase inutile pour assurer la "
                         "transmission des données .",
		"replurlexp": 'url-remplacée',        
		"replemailexp": 'email-remplacé',        
		"replipexp": 'ip-remplacée>',        
		"repldnsexp": 'dns-remplacé'		
    },
