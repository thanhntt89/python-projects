import numpy as np

class matrixes():
    def getLength(self,matrix):
        return len(matrix)

    def combineColumns(self,matrix):
        return [x for x in zip(*matrix)]

    def convert_to_array(self, matrix):
        return np.array(matrix).flatten()

def main():
    _matrix = matrixes()

    matrix = [[1,2,4,15],
            [5,7,8,9],
            [19,25,21,11]]
    print(f'Matrix:{matrix}')
    print(f'Matrix length:{_matrix.getLength(matrix)}') 
    print(f'Combine columbers:{_matrix.combineColumns(matrix)}')
    print(f'Convert convert_to_array:{_matrix.convert_to_array(matrix)}') 

if __name__ == '__main__':
    main()
