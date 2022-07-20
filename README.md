# nltk_helpers
Repository to store helper functions for NLTK package for Natural Language Processing

These functions aid in data processing of dependency and constituency treebanks such as Exploratory Data Analysis and processing

1. `count_pos_tags`

Counts the different Parts-Of-Speech tags in a constituency treebank and returns a Pandas DataFrame

2. `extract_constituents`

Extracts the different constituents in a constituency treebank and returns a list.
Additional preprocessing such as using a Counter object to count the items can be used.

3. `nltk_tree_to_str`

Extracts all the leaves in a constituency treebank and returns the sentence

4. `remove_null_elements`

Function to remove all `-NONE-` tags in a constituency treebank. Note: constituency tag of the removed branches may not be syntactically correct after `-NONE-` removal

5. `swap_xpos_tags`

Swaps out the UPOS tags to XPOS tags in a dependency treebank. This is in reference to [LAL-HPSG](https://github.com/KhalilMrini/LAL-Parser/blob/master/README.md) for your custom dataset

# Credits

The use of such functions are to aid in research on top of the current [Natural Language Tool Kit (nltk)](https://www.nltk.org/) python package.