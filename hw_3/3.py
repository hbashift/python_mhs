import numpy as np
import os


class Matrix:
    def __init__(self, data):
        if not isinstance(data, np.ndarray):
            raise ValueError("Matrix data must be a numpy array.")
        self.data = data

    def __add__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Matrices must have the same dimensions for addition.")
        return Matrix(self.data + other.data)

    def __mul__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Matrices must have the same dimensions for element-wise multiplication.")
        return Matrix(self.data * other.data)

    def __matmul__(self, other):
        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("Matrices have incompatible dimensions for matrix multiplication.")
        return Matrix(self.data @ other.data)

    def __str__(self):
        return str(self.data)

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(str(self.data))


class MatrixMixin:
    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(str(self.data))

    def __str__(self):
        return np.array2string(self.data)

    @property
    def shape(self):
        return self.data.shape

    @shape.setter
    def shape(self, new_shape):
        self.data = self.data.reshape(new_shape)


class EnhancedMatrix(MatrixMixin, Matrix):
    pass


class HashMixin:
    def __hash__(self):
        # Простая хэш-функция: сумма всех элементов умноженная на размерность матрицы
        return int(np.sum(self.data) * self.data.size)


class CachedMatrix(HashMixin, EnhancedMatrix):
    _cache = {}

    def __matmul__(self, other):
        key = (hash(self), hash(other))
        if key in self._cache:
            return self._cache[key]
        result = super().__matmul__(other)
        self._cache[key] = result
        return result


if __name__ == "__main__":
    """ Задача 3.1 """
    # Генерация матриц
    np.random.seed(0)
    matrix_a = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix_b = Matrix(np.random.randint(0, 10, (10, 10)))

    # Выполнение операций
    matrix_add = matrix_a + matrix_b
    matrix_mul = matrix_a * matrix_b
    matrix_matmul = matrix_a @ matrix_b

    # Сохранение результатов
    matrix_a.save_to_file("./artifacts/3_1/matrix_a.txt")
    matrix_b.save_to_file("./artifacts/3_1/matrix_b.txt")

    matrix_add.save_to_file("./artifacts/3_1/matrix+.txt")
    matrix_mul.save_to_file("./artifacts/3_1/matrix*.txt")
    matrix_matmul.save_to_file("./artifacts/3_1/matrix@.txt")

    """ Задача 3.2 """
    # Пример использования
    matrixE_a = EnhancedMatrix(np.random.randint(0, 10, (10, 10)))
    matrixE_b = EnhancedMatrix(np.random.randint(0, 10, (10, 10)))

    matrixE_add = matrixE_a + matrixE_b
    matrixE_mul = matrixE_a * matrixE_b
    matrixE_matmul = matrixE_a @ matrixE_b

    matrixE_add.save_to_file("./artifacts/3_2/matrix+.txt")
    matrixE_mul.save_to_file("./artifacts/3_2/matrix*.txt")
    matrixE_matmul.save_to_file("./artifacts/3_2/matrix@.txt")

    matrixE_a.save_to_file("./artifacts/3_2/matrix_a.txt")
    matrixE_b.save_to_file("./artifacts/3_2/matrix_b.txt")

    print(matrixE_a)

    """ Задача 3.3 """
    # Генерация матриц и поиск коллизий
    matrix_a = CachedMatrix(np.random.randint(0, 100, (2, 2)))
    matrix_b = CachedMatrix(np.random.randint(0, 100, (2, 2)))
    matrix_c = CachedMatrix(np.random.randint(0, 100, (2, 2)))
    matrix_d = CachedMatrix(matrix_b.data.copy())
    count = 0
    while not (hash(matrix_a) == hash(matrix_c)
               and not np.array_equal(matrix_a.data, matrix_c.data)
               and not np.array_equal((matrix_a @ matrix_b).data, (matrix_c @ matrix_d).data)):
        matrix_a = CachedMatrix(np.random.randint(0, 100, (2, 2)))
        matrix_c = CachedMatrix(np.random.randint(0, 100, (2, 2)))
        matrix_b = CachedMatrix(np.random.randint(0, 100, (2, 2)))
        matrix_d = CachedMatrix(matrix_b.data.copy())

        count += 1
        print(count)

    # Проверка условий
    assert hash(matrix_a) == hash(matrix_c)
    assert not np.array_equal(matrix_a.data, matrix_c.data)
    assert np.array_equal(matrix_b.data, matrix_d.data)
    assert not np.array_equal((matrix_a @ matrix_b).data, (matrix_c @ matrix_d).data)

    # Сохранение матриц и результатов
    matrix_a.save_to_file("./artifacts/3_3/A.txt")
    matrix_b.save_to_file("./artifacts/3_3/B.txt")
    matrix_c.save_to_file("./artifacts/3_3/C.txt")
    matrix_d.save_to_file("./artifacts/3_3/D.txt")

    (matrix_a @ matrix_b).save_to_file("./artifacts/3_3/AB.txt")
    (matrix_c @ matrix_d).save_to_file("./artifacts/3_3/CD.txt")

    with open("./artifacts/3_3/hash.txt", "w") as f:
        f.write(f"hash(A @ B) = {hash(matrix_a @ matrix_b)}\n")
        f.write(f"hash(C @ D) = {hash(matrix_c @ matrix_d)}\n")
