
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

would include BABY and BAT. An interesting solution is, to take the first letter of the word to be found and create a rectangle around it equal to the length of the word. All letters must be found in this square. If more than one pattern is found some analysis has to be done: for example, above, both sections BABY and BATBY with turn out positive when using this rectangle method around 'B', but the lower right option is not contiguous. The above can be reduced by implying a circular search, which is, in a way, a variant of what we'll do here.

Trees can also be used, and are often sees with word ladders, a smiliar implementation of a word search. This would require creating root nodes for each of the positions in the matrix, and then branches with one letter added at a time. This may be very powerful for larger datasets and, if the word sesarch one is an abstract problem rather than this specific problem, tree traversal might be useful.

Here, there are eight directions. For each word to be found, we'll get all the locations where we see the first letter, and try to make the words in directional sequence, which should fail enough times to be quick at finding the right one!

## Implementation

Super slim: 

`python --inputfile example1.txt`

(for example)

:)

## P.S.

**Nerd Alert**: Topological analysis may suggest a lot of interesting ideas too far beyond the scope of this project :)