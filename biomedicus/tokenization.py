import re
from typing import Iterable, NamedTuple, Optional, AnyStr

Token = NamedTuple('Token',
                   [('segment', int),
                    ('begin', int),
                    ('end', int),
                    ('label', Optional[int]),
                    ('is_identifier', Optional[bool]),
                    ('has_space_after', bool)])
Token.__doc__ = '''\
A Token in text.

Attributes
----------
segment : int
    the index of the segment of text the token is in
begin : int 
    the begin index of the token
end : int 
    the end index of the token
label : optional int
    optional label
is_identifier : optional bool
    optional boolean specifying the token is an identifier / named entity
has_space_after : bool
    boolean specifying if the token has a space following it.
'''

_segment_pattern = re.compile(r"\n{2,}|\Z", re.M)
_token_pattern = re.compile(r"(^=+$)|(^-+$)|[A-Za-z]+|\S", re.M)


def detect_space_after(txt: AnyStr, end: int):
    """Given text and an end index returns True if there is a space after the end index, false
    otherwise.

    Parameters
    ----------
    txt : str
        the text itself.
    end : int
        the end index of the token.

    Returns
    -------
    bool
        true if there is a space after the end index, false otherwise.
    """
    return end < len(txt) and not txt[end:end + 1].isspace()


def tokenize(txt: str) -> Iterable[Token]:
    """Tokens text according to word-embedding tokenization rules: splits on whitespace, splits on
    punctuation and numerals, keeps lines consisting entirely of "=" or "-" together.

    Parameters
    ----------
    txt: str
        the text to tokenize

    Returns
    -------
    iterable of Token
        iterable of all the tokens in the text
    """
    segment_start = 0
    for segment_index, segment in enumerate(_segment_pattern.finditer(txt)):
        segment_end = segment.start()
        for token in _token_pattern.finditer(txt, segment_start, segment_end):
            has_space_after = txt[token.end():token.end() + 1].isspace() if token.end() < len(
                txt) else False
            yield Token(segment_index,
                        token.start(),
                        token.end(),
                        None,
                        None,
                        has_space_after)

        segment_start = segment.end()
