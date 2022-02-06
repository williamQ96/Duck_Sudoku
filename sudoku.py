"""
File: sudoku.py

Sudoku solver with optional displays
"""

import argparse
import sdk_reader
import sdk_display

import logging
logging.basicConfig(level = logging.DEBUG)
log = logging.getLogger('sudoku.py')
#logging.set_level(logging.INFO)


def cli() -> object:
    """Get arguments from command line"""
    parser = argparse.ArgumentParser(description="Sudoku solver")
    parser.add_argument("-d", "--display", help="Graphical display",
                        action="store_true")
    parser.add_argument('sdk_file', nargs='?', type=argparse.FileType('r'),
                        default='data/easy.sdk')
    args = parser.parse_args()
    return args


def main():
    args = cli()
    board = sdk_reader.read(args.sdk_file)
    log.debug(f'Read initial board from {args.sdk_file.name}:\n{board}')
    
    if args.display:
        the_display = sdk_display.Board(board, 800, 800)   
    if board.is_consistent():
        board.solve()
    else:
        print("Board has duplicates; rejected")
        
    print('Final board:')
    print(board)

    if args.display:
        input("Press enter to shut down")
        the_display.close()


if __name__ == "__main__":
    main()
