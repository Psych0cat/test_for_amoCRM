import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-l", "--lines_count", help="Counts lines in STDIN",
                    action="store_true")

parser.add_argument("-w", "--words_count", help="Counts words in STDIN",
                    action="store_true")

parser.add_argument("-c", "--count_bytes", help="Counts bytes in STDIN",
                    action="store_true")


args = parser.parse_args()
text = sys.stdin.read()


def count_lines(text):
    return len(text.splitlines())


def count_words(text):
    word_count = len(text.split())
    return word_count


def count_bytes(text):
    """Output of sys.getsizeof() differs from console wc -c, seems like wc -c equals len()"""
    return len(text)


if args.lines_count:
    print(count_lines(text))

if args.words_count:
    print(count_words(text))

if args.count_bytes:
    print(count_bytes(text))

if args.lines_count is False and args.words_count is False and args.count_bytes is False:
    print(f'{count_lines(text)}, {count_words(text)}, {count_bytes(text)}')
