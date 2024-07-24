class Sudoku_reader():
    def sudoku_reader(file_path):
        puzzle = []
        with open(file_path, 'r') as file:
            for line in file:
                row = list(map(int, line.strip().split()))
                puzzle.append(row)
        return puzzle