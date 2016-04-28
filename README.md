Rhythm analyzer
====================

This project attempts to analyze the rhythm of prose through the use of a machine learning algorithm.

Text conversion
------------------

The first part takes the text and uses the CMU dictionary to substitute words with the respective accents and punctuations with pause values.
While the assigned values for pauses are arbitrary, they were chosen with a psycholingustic approach, considering the perceived value of the pauses.

Though it's using some texts from the Guntenberg Project as a test, the NLTK library can take plaintext files.

Text analysis
-----------------

TODO Use an unsupervised machine learning algorithm to find patterns of interest (k-means to cluster phrases or texts maybe)