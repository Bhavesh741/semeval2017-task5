from argparse import ArgumentParser

import sys

from processors.docvec_processor import DocvecProcessor
from utils.options import Options


def main(argv):
    """
    Main function to kick start execution
    :param argv:
    :return: null
    """
    options = parse_args(argv)
    processor = DocvecProcessor(options)
    processor.process()


def parse_args(argv):
    """
    Parses command line arguments form an options object
    :param argv:
    :return:
    """
    parser = ArgumentParser(prog="semeval2015-task5")
    parser.add_argument('--train_headlines_data_path', metavar='Training Headlines File Path', type=str)
    parser.add_argument('--test_headlines_data_path', metavar='Test Headlines File Path', type=int)

    return parser.parse_args(argv, namespace=Options)


if __name__ == "__main__":
    main(sys.argv[1:])

