This will work if you have eight witnesses.

1. Paste the text of each witness in a txt file (W1.txt, W2.txt, W3.txt, W4.txt, etc.)

2. Run 'prepare-for-collation.py'
This creates a folder 'halfway'. If the automatic lemmatization is not satisfactory, edit the 'lemmas' text files inside the folder 'halfway'.

3. Run 'collation-from-lemmas.py'
This runs CollateX (with no segmentation) using as input the 'lemmas' text files in the folder 'halfway'.
The results are in the new text file 'collation-output-lemmas'.

4. You may want to compare the result with the collation on the original forms. Hence run 'collation-from-original.py' --> The results are in the new text file 'collation-output-original', that you can compare with 'collation-output-lemmas'.

