from nltk.corpus.reader import BracketParseCorpusReader
import pandas as pd


def count_pos_tags(reader: BracketParseCorpusReader) -> pd.DataFrame:
    """
    Generate DataFrame of Parts-of-Speech tags in a corpus

    Args:
        reader (BracketParseCorpusReader): BracketParseCorpusReader object from a file

    Returns:
        pd.DataFrame: DataFrame of POS counts
    """
    pos_counter = dict()

    for word, tag in reader.tagged_words():
        if tag in pos_counter:
            pos_counter[tag] += 1
        else:
            pos_counter[tag] = 1
    df = pd.DataFrame(pos_counter, index=["counts"])
    df = (
        df.T.sort_values(by="counts", ascending=False)
        .reset_index()
        .rename(columns={"index": "pos_tag"})
    )
    return df
