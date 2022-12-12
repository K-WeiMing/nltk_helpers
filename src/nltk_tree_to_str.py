import nltk


def convert_tree_to_str(tree_bank: nltk.Tree) -> str:
    """
    Converts Treebank object to string representation

    Args:
        tb (Treebank): nltk.Tree object

    Returns:
        str: String representation (Treebank Format) from nltk.Tree object
    """
    treebank_list = []
    for tree in tree_bank.pformat().split("\n"):
        treebank_list.append(" " + tree.lstrip())

    treebank_str = "".join(treebank_list)

    return treebank_str.strip()
