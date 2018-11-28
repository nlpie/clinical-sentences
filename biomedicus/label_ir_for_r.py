import sys

from biomedicus.sentences.vocabulary import directory_labels_generator


def main(dir1, dir2, output):
    labels = {}

    for _, name, tokens in directory_labels_generator(dir1, return_name=True):
        for token in tokens:
            identifier = (name, token.begin, token.end)
            labels[identifier] = [token.label, '']

    for _, name, tokens in directory_labels_generator(dir2, return_name=True):
        for token in tokens:
            identifier = (name, token.begin, token.end)
            if identifier not in labels:
                labels[identifier] = ['', token.label]
            else:
                labels[identifier][1] = token.label

    with open(output, 'w') as f:
        for (name, begin, end), (annot1, annot2) in labels.items():
            f.write(f'{name}:{begin}:{end} {annot1} {annot2}\n')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
