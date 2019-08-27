# Copyright 2019 Regents of the University of Minnesota.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
