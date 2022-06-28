import nltk

Treebank: nltk.Tree

def convert_tree_to_str(tb: Treebank):
    """Converts Treebank object to string representation

    Args:
        tb (Treebank): _description_
    """
    
    treebank_list = []
    for t in tb.pformat().split('\n'):
        treebank_list.append(' ' + t.lstrip())
        
    treebank_str = ''.join(treebank_list)

    return treebank_str.strip()