This will work if you have three witnesses.

1. Paste the text of each witness in a txt file (W1.txt, W2.txt, W3.txt)

2. Run 'prepare-for-collation.py'
It lemmatizes the texts and clean the output. The results are in the new folder 'halfway'. If the automatic lemmatization is not satisfactory, edit the 'lemmas' text files inside the folder 'halfway'.

3. Run 'collation-from-lemmas.py'
It runs CollateX (with no segmentation) using as input the 'lemmas' text files in the folder 'halfway'.
The results are in the new text file 'collation-output-lemmas'.

4. You may want to compare the result with the collation on the original forms. Hence run 'collation-from-original.py' --> The results are in the new text file 'collation-output-original', that you can compare with 'collation-output-lemmas'.

