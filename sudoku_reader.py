class Sudoku_reader:
    def sudoku_reader(self, file_path):
        puzzle = []
        with open(file_path, 'r') as f:
            for line in f:
                row = []
                for value in line.strip().split():
                    if len(row) >= 9:
                        break  # Ignore values beyond the 9th column
                    if value.isdigit():
                        row.append(int(value))
                    else:
                        raise ValueError(f"Invalid character in sudoku file. Replace unknown with 0")
                while len(row) < 9:
                    row.append(0)
                puzzle.append(row)
        return puzzle
