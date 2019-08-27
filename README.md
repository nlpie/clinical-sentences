# Sentence Detection

Sentence detection for clinical notes.

# Usage
```
pip install .[tf]
```

Training and evaluation expects .labels/.txt file pairs where .labels is a file with lines of tokens 
in space separated format as shown below, and .txt is the plain text of the document.

```text
[segment] [start index] [end index] [tag] [is_identifier] [token text]
```

Segment is the segment of the document the token appears in. Sentences can not span segments. We 
used one segment per document, but strategies for splitting could include paragraphs from html 
or rtf, or two consecutive new lines in plain text.

start index and end index are the bounds of the token

tag is the manually annotated tag, B for begin of sentence tokens, I for end of sentence tokens,
O for tokens that should be ignored.

is_identifier is whether the token is an identifier e.g. names, dates, etc. A special word embedding 
is used for identifiers.

token text is not used by the training or evaluation.  

## Sentence Detector

The sentence detector code is found in biomedicus/sentences/models.py  

# Resources

Annotated corpora, word embeddings, and trained models from the MIMIC corpus will be posted to 
physionet.org
