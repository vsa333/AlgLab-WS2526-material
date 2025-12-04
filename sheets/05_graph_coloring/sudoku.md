## Task 1

Say you have a partially filled Sudoku field. We convert the instance into a graph coloring problem with 9 colors, one for every number (1-9). We create a node correlating to every cell in the field. Since one field has 81 cells, the graph has 81 nodes. The edges encode the constraints of Sudoku:
- No number can be repeated in the same column, so we add an edge between every node corresponding to the same column
- No number can be repeated in the same row, so we add an edge between every node corresponding to the same row
- No number can be repeated in the same 3x3 subfield, so we add an edge between every node corresponding to the same subfield

If a cell already has a number in the sudoku instance, the corresponding node is connected to every node of a 9-clique of auxilliary nodes, except one node of the clique, corresponding to the set number/color.

This graph is 9-colorable iff. the sudoku instance is solvable.
Per construction, every coloring of the graph corresponds to a filled out sudoku field, where the colors convert to numbers (1-9), and the nodes convert to cells in the grid. Two nodes are connected when, in the sudoku instance (as cells), they are in the same column, row, or subfield. Conversely, two nodes can only have the same color when they are not directly connected. In the sudoku instance, this corresponds to two cells with the same number, which are not in the same row, column or subfield.

This means that being able to color the graph with 9 colors translates to being able to fill out the cells of the sudoku instance with the 9 numbers.