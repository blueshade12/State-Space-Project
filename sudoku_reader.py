class Sudoku_reader:
    def sudoku_reader(self, file_path):
        puzzle = []
        with open(file_path, 'r') as f:
            for line in f:
                row = []
                for value in line:
                    if value.isspace() or value == '\n':
                        row.append(0)
                    elif value.isdigit():
                        row.append(int(value))
                    else:
                        raise ValueError(f"Invalid character in sudoku file. Replace unknown with 0")
                puzzle.append(row)
        return puzzle
