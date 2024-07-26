import consistency_alg
import sudoku_reader

class Abstract:
    def __init__(self):
        self.path = input("Please input the filepath of the sudoku file: ")
        self.reader = sudoku_reader.Sudoku_reader()  
        self.solved_puzzle = self.run_algorithm()

    def run_algorithm(self):
        puzzle = self.reader.sudoku_reader(self.path)  
        alg = consistency_alg.Arc_Consistency_Algorithm(puzzle)  
        return alg.run()

abstract = Abstract()
print(abstract.solved_puzzle)