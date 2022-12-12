from typing import List
import nltk


def zip_data(dep_tbank_path: str, const_tbank_path: str) -> List[list]:
    """

    Args:
        dep_tbank_path (_type_): File path to dependency treebank
        const_tbank_path (_type_): File path to constituent treebank

    Returns:
        List[list]: Output of dependency treebank zipped with constituency treebank for each token [[(Dependency tbank), (word, XPOS)], ...]
    """
    output = []

    # Parse the Dependency Treebank
    with open(dep_tbank_path, "r") as file:
        dep_tbank = file.read().strip().splitlines()

    # Parse the Constituency Treebank
    with open(const_tbank_path, "r") as file:
        const_tbank = file.read().strip().splitlines()

    # Init sentence index for constituency Treebank
    sentence_index_c = 0
    sentence_index_d = 0
    for index, row in enumerate(dep_tbank):

        # Search for the sentence split for the dependency treebank
        if row == "" or index == len(dep_tbank) - 1:
            # Read in the treebank for constituency parsing
            c_tbank = nltk.Tree.fromstring(const_tbank[sentence_index_c]).pos()

            # Combine both treebanks into a tuple
            zipped_tbank = list(zip(dep_tbank[sentence_index_d:index], c_tbank))
            output.append(zipped_tbank)

            sentence_index_c += 1
            sentence_index_d = index + 1

    return output


def swap_pos_tag(zipped_tbank: List[list]) -> list:
    """Swaps the POS tags of UPOS to XPOS

    Args:
        zipped_tbank (List[list]): Input format of: [[(Dependency tbank), (word, XPOS)], ...]

    Returns:
        list: list format for writing to a file
    """
    output = []

    # Parse through the list
    for tags in zipped_tbank:

        # Parse through each item in the list
        for tag in tags:
            sentence = tag[0].split("\t")

            # Swap the POS tags, XPOS -> UPOS
            sentence[4] = tag[1][1]
            output.append("\t".join(sentence))
        output.append("")

    return output


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description="Swaps the UPOS tags in Dependency Treebank to XPOS in Loaded Treebank"
    )

    parser.add_argument(
        "--dep_tbank", default=None, help="Input file path of the dependency treebank"
    )
    parser.add_argument(
        "--const_tbank",
        default=None,
        help="Input file path of the constituency treebank",
    )
    parser.add_argument(
        "--output_file", default=None, help="Output file of the dependency treebank"
    )

    args, unknown = parser.parse_known_args()

    treebank = zip_data(args.dep_tbank, args.const_tbank)
    treebank = swap_pos_tag(treebank)

    with open(args.output_file, "w") as file:
        file.writelines(tree + "\n" for tree in treebank)
