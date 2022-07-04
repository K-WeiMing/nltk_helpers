import re
import nltk
from nltk.tree import collapse_unary

"""
Example input from Kethu dataset

(S (NP-SBJ (NP (NN Jenis) (NN monyet)) (SBAR (IN yang) (S (NP-SBJ-1 (-NONE- *)) (VP (VB dikerahkan) (NP (-NONE- *-1)) (NP-LGS (NN pemkot)))))) (VP (VP (VB berbadan) (ADJP (JJ besar))) (, ,) (VP (VB berekor) (ADJP (JJ panjang))) (, ,) (CC dan) (VP (VB memiliki) (NP (NN wajah) (SBAR (-NONE- 0) (S (NP-SBJ (-NONE- *)) (VP (VB berwarna) (ADJP (JJ hitam)))))))) (. .))

"""

def remove_none(input_str):
    
    none_count = input_str.count('(-NONE- ')
    
    res = ''
    
    for _ in range(none_count):
        if '(-NONE- ' in input_str:
            start_index = input_str.find('(-NONE- ')
            res = input_str[:start_index]
            
            # Get the closing bracket
            for i in range(start_index, len(input_str)):
                # On the first match of close bracket, remove the characters
                if input_str[i] == ')' and input_str[i+1] == ' ': # Extra space to account for ') (NP....)
                    res += input_str[i+2:]
                    break
                elif input_str[i] == ')': # Else it will be: ))
                    res += input_str[i+1:]
                    break
        input_str = res
    return res



def remove_no_leaves(input_str):
    res = re.sub(r"\([a-zA-Z\-1-9\*]*\s\)",'', input_str)
    return res


def remove_null_elements(input_string):
    
    # Step 1: Remove -NONE- pos tags
    remove_none_tags = remove_none(input_string)
    
    # Step 2: Remove any outstanding constituents without any 'leaves' -> (NP-SBJ )
    removed_invalid_constituents = remove_no_leaves(remove_none_tags)
    
    # Step 3: Collapse unary -> Collapse all the subtrees with a single child
    # Collapse unary requires a tree object
    tree_processed = nltk.Tree.fromstring(removed_invalid_constituents)
    collapse_unary(tree_processed)
    
    # Step 4: Remove the head branches of the collapsed unaries e.g. NP + VB -> VB
    final_preprocess = ' '.join(str(tree_processed).split())
    
    # Step 5: Remove the parent constituent that has been collapsed
    res = ''
    i = len(final_preprocess)-1
    while i >= 0:
        if final_preprocess[i] == '+' and final_preprocess[i-1].isalpha(): # use isalpha() as it omits white space
            # Search for the next open bracket
            while i >= 0:
                if final_preprocess[i] == '(':
                    res += final_preprocess[i]
                    break
                i -= 1
        else:
            res += final_preprocess[i]
        i -= 1

    
    return res[::-1]