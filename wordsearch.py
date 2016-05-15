#!/usr/bin/python

# -*- coding: utf-8 -*-
# @Author: mypolopony
# @Date:   2016-05-09 11:29:08
# @Last Modified 2016-05-10
# @Last Modified time: 2016-05-10 07:40:46

# This is a solution to the Factual Data Science Take Home problem: Implementing Super Word Search.
# I've tried to explain some of my decisions both in the Readme and here in the comments. Of course
# there are many more bells and whistles that one might add on, but I
# think this is solid.


import sys
import getopt
import time
import logging
import argparse

# Set logging fot stdout
logging.basicConfig(level=logging.INFO, format=':: %(message)s')


class Puzzle:

    def __init__(self, inputfile):
        '''
        Initialize by reading a file. The structure provided is assumed not to vary too 
        much from what is given. For a larger project, we would want to do a lot of 
        error checking.
        '''

        # Read in the file
        with open(inputfile) as spec:
            m, n = spec.readline().split()
            self.n = int(n)
            self.m = int(m)

            # This is going to be a flat array, but we will create a method to access it
            # in a more straightforward way. Read this and the other data
            # involved
            self.matrix = list()

            for row in range(0, self.m):
                self.matrix.extend(list(spec.readline().rstrip().lower()))

            self.searchmode = spec.readline().rstrip()
            num_words = int(spec.readline())
            self.found_words = dict()

            for nw in range(0, num_words):
                word = spec.readline().lower().rstrip()
                self.found_words[word] = None

        # Generate possible directions (in terms of unit vectors)
        self.directions = [(0, 1),					# North
                           (0, -1),					# South
                           (1, 0),					# East
                           (-1, 0)]					# West
        if self.searchmode == 'WRAP':
            self.directions.extend([(-1, -1),		# Southwest
                                    (1, 1),			# Northeast
                                    # Southwest
                                    (-1, 1),
                                    (1, -1)])		# Northwest

    def get_idx(self, row, col):
        '''
        Remember, here, rows and columns are zero-based
        '''

        return row * self.n * self.m + col

    def get_rc(self, idx):
        '''
        Index to row/col
        '''

        row = int(idx / self.n)
        col = idx - self.n * row
        return((row, col))

    def solve_word(self, word, idx, path):
        '''
        Recursive algorithm. The basic format is to know where you are 
        and look around and see if any of your neighbors match your next 
        criterion. 
        '''

        # If we have a path already, we should see if our path violates
        # any rules. The edge cases are small in number, so we can get
        # away with it.
        if path and word == '':
            # Are we including ourselves, even if we can wrap?
            if len(path) > 1 and idx == path[0]:
                return False

            # Have we wrapped when we shouldn't have? For a linear array,
            # this can be defined as the trend in indexes being monotonic,
            # that is to say, if the derivative switches signs, we know
            # we've made some kind of weird jump. In this implementation,
            # we just count the number of negatives (and zeros) or psitives
            # (and zeros) -- if the length of either of these does not match
            # the length of path_diffs, we must have wrapped
            path_diffs = [j - i for i, j in zip(path[:-1], path[1:])]
            path_pos = len([d for d in path_diffs if d >= 0])
            path_neg = len([d for d in path_diffs if d <= 0])
            if not (path_pos == len(path_diffs) or path_neg == len(path_diffs)) and self.searchmode == 'NO_WRAP':
                return False

        if word == '':		# We've passed the above and made it to the base case!
                                                # For . . reasons . . elif
                                                # won't work here
            return path
        else:				# Still going. . .
            starts_idx = [i for i, j in enumerate(self.matrix) if j == word[0]]
            for si in starts_idx:
                row, col = self.get_rc(si)
                for bearing in self.directions:
                    newrow = row + bearing[0]
                    newcol = col + bearing[1]
                    newidx = self.get_idx(newrow, newcol)
                    path.append(si)
                    answer = self.solve_word(word=word[1:], idx=si, path=path)
                    if answer:
                        return path
                    elif answer and word == '':
                        break
                    else:
                        return False

    def solve_all(self):
        ''' 
        Main algorithm. In a more complicated search, recursion might help 
        us, i.e. in the undirected version of word search. So let's try it 
        here. Not too complicated. We'll use this method as a control to dive 
        into the reursive methodabove
        '''
        for word in self.found_words:
            # Get the start idxs and try the directions
            self.found_words[word] = self.solve_word(
                word=word, idx=None, path=list())

        return self.found_words


def main(argv):
    # Check for arguments
    parser = argparse.ArgumentParser()
    try:
        parser.add_argument("--inputfile", help="Input File")
        args = parser.parse_args()
        inputfile = args.inputfile
    except:
        logging.info("Unexpected error:", sys.exc_info()[0])

    # Create the puzzle representation
    logging.info('Working with: {fn}'.format(fn=inputfile))
    start = time.time()
    puzzle = Puzzle(inputfile)
    done = time.time()
    logging.info('Done loading!  (in {t}ms):'.format(
        t=str(round(done - start, 5))))

    # Solve the puzzle!
    logging.info('Soving the puzzle!')
    start = time.time()
    found_words = puzzle.solve_all()
    done = time.time()
    logging.info('Done solving!  (in {t}ms):'.format(
        t=str(round(done - start, 5))))

    logging.info('Solutions:')
    for word in found_words.keys():
        if found_words[word]:
            # Get the first coordinates
            start = puzzle.get_rc(idx=found_words[word][0])
            # Get the last coordinates
            end = puzzle.get_rc(idx=found_words[word][-1])
            logging.info('{}: {} {}'.format(word, start, end))
        else:
            logging.info('{}: NOT FOUND'.format(word))


if __name__ == '__main__':
    main(sys.argv[1:])
