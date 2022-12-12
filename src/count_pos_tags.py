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
    pos_counter = {}

    for _, tag in reader.tagged_words():
        if tag in pos_counter:
            pos_counter[tag] += 1
        else:
            pos_counter[tag] = 1
    df_pos_counter = pd.DataFrame(pos_counter, index=["counts"])
    df_pos_counter = (
        df_pos_counter.T.sort_values(by="counts", ascending=False)
        .reset_index()
        .rename(columns={"index": "pos_tag"})
    )
    return df_pos_counter
