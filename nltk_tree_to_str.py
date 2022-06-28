import nltk

Treebank: nltk.Tree


def convert_tree_to_str(tb: Treebank) -> str:
    """
    Converts Treebank object to string representation

    Args:
        tb (Treebank): nltk.Tree object

    Returns:
        str: String representation (Treebank Format) from nltk.Tree object
    """
    treebank_list = []
    for t in tb.pformat().split("\n"):
        treebank_list.append(" " + t.lstrip())

    treebank_str = "".join(treebank_list)

    return treebank_str.strip()
