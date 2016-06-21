
## Introduction

As a lover of crosswords, I must say that, like any good Adult-Youth pulp bestseller, there exists Team Crossword and Team Word Search; and they are often at odds. For this project, however, as long as you don't tell anyone, I will temporarily shift over to the Dark Side.

## Implementation

There are several ways that come to mind to solve a simple word search. The first suggestion might be, for each word, go through the matrix and see if it can be found. This runs with quadratic complexity, at least (I think), which is no fun. 

One version of the word search, which seems more complicated, is a cyclical version, wherein words can be made using any combination of directions:

```
x x x x x
x A B Y x
x B x x x
x x A T B
x x B x Y
```

would include BABY and BAT. An interesting solution is, to take the first letter of the word to be found and create a rectangle around it equal to the length of the word. *All letters must be found in this square.* Analysis is much quicker now, and we need only to consider the squares that pass the test.  The next step is a kind of a circular search, a variant of which we'll use here.

Trees can also be used, and are often seen with word ladders, a smiliar implementation of a word search. This would require creating root nodes for each of the positions in the matrix, and then branches with one letter added at a time. This approach is easy for small networks, difficult for medium sized networks, and actually relatively easier for very large-scale networks; in the latter case, more sophisticated / specialized frameworks for graph storage and traversal become inherently valuable.

Anyway. In the word search there are eight neighbors, save the edge pieces (though this becomes interesting if wrapping is allowed). For each word to be found, we'll get all the locations where we see the first letter [O(n)], and try to make the words in each linear direction, which should fail enough times, early enough, to be quick at finding the right one!

## Usage

Super slim: 

`python --inputfile example1.txt`

(for example)
