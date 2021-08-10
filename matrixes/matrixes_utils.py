import numpy as np

class matrixes():
    def getLength(self,matrix):
        return len(matrix)

    def combineColumns(self,matrix):
        return [x for x in zip(*matrix)]

    def convert_to_array(self, matrix):
        return np.array(matrix).flatten()

    def addTowMatrix(self,matrixX,matrixY):
        return [[matrixX[i][j] + matrixY[i][j] for j in range(len(matrixX[0]))] for i in range(len(matrixX))]

    def multiplyTowMatrixUsingNetListComprehension(self,matrixX,matrixY):
        return [[sum(a*b for a,b in zip(x_row,y_col)) for y_col in zip(*matrixY)] for x_row in matrixX]
    
    def matrixJoinColumn(self,matrixX, matrixY):
        return np.dot(matrixX,matrixY).shape()

    def matrixMultiplyNp(self, matrixX, matrixY):
        return np.matmul(matrixX,matrixY).shape()

def main():
    _matrix = matrixes()

    matrix = [[1,2,4,15],
            [5,7,8,9],
            [19,25,21,11]]
    print(f'Matrix:{matrix}')
    print(f'Matrix length:{_matrix.getLength(matrix)}') 
    print(f'Combine columbers:{_matrix.combineColumns(matrix)}')
    print(f'Convert convert_to_array:{_matrix.convert_to_array(matrix)}') 

    matrixX = [[12,7,5],
               [6,3,5],
               [8,34,24]]
    matrixY =[[3,6,9],
              [7,8,2],
              [6,8,3]]

    #join
    #print(f'NP: X*Y = {_matrix.matrixJoinColumn(matrixX,matrixY)}')

    print(f'MatrixX:{matrixX}\nmatrixY:{matrixY}')
    print(f'MatrixX + MatrixY = {_matrix.addTowMatrix(matrixX,matrixY)}')

    print(f'MatrixX*MatrixY = {_matrix.multiplyTowMatrixUsingNetListComprehension(matrixX,matrixY)}')

if __name__ == '__main__':
    main()
