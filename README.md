# three-musketeers
A program to play the game of Three Musketeers--human against computer. Rules see the link https://en.wikipedia.org/wiki/Three_Musketeers_%28game%29

The "board" is represented as a list of five lists; each of these lists represents a row, and each list contains five elements. The first list represents the first row; the first element in each list represents the first column. The values in the list must each be one of three things: an 'M', representing a Musketeer, an 'R', representing one of Cardinal Richelieu's men; and a '-', representing an empty space. board is the one and only global variable in this program.

Directions are given as one of the four strings 'left', 'right', 'up', and 'down'.
