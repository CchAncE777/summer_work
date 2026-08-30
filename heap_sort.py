import random
import time
import tracemalloc

n = int(input('Введите число элементов в списке: '))

class heap_sort:
    def __init__(self, n):
        self._random_list = [random.randint(1, n*10) for _ in range(n)]
        self._sorted_list = sorted(self._random_list)
        self._reversed_list = list(reversed(self._sorted_list))
        num = int(n*0.95) + 1

        if num == n:
            self._95_and_5 = self._sorted_list[num - 1:] + self._sorted_list[:num - 1]
        else:
            self._95_and_5 = self._sorted_list[num - 1:] + self._sorted_list[:num]

    def random_sort_n(self):

        def _heapify(array, n, i):

            The_best = i
            first = 2 * i + 1
            second = 2 * i + 2

            if first < n and array[first] > array[The_best]:
                The_best = first

            if second < n and array[second] > array[The_best]:
                The_best = second

            if The_best != i:
                array[i], array[The_best] = array[The_best], array[i]
                _heapify(array, n, The_best)

        def heap_sort(array):

            n = len(array)

            for i in range(n // 2 - 1, -1, -1):
                _heapify(array, n, i)

            for i in range(n - 1, 0, -1):
                array[i], array[0] = array[0], array[i]
                _heapify(array, i, 0)

            return array

        tracemalloc.start()

        start_time = time.perf_counter()

        sorted_result = heap_sort(self._random_list.copy())

        end_time = time.perf_counter()

        mem, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        peak_mb = peak_memory / 1024 / 1024

        time_final = end_time - start_time

        print(sorted_result)
        print(f'Наше время при heap_sort на {len(sorted_result)} символов: {time_final} секунд')
        print(f'Максимальное количество памяти: {peak_mb:.4f} MB')

    def sorted_sort_n(self):

        def _heapify(array, n, i):

            The_best = i
            first = 2 * i + 1
            second = 2 * i + 2

            if first < n and array[first] > array[The_best]:
                The_best = first

            if second < n and array[second] > array[The_best]:
                The_best = second

            if The_best != i:
                array[i], array[The_best] = array[The_best], array[i]
                _heapify(array, n, The_best)

        def heap_sort(array):

            n = len(array)

            for i in range(n // 2 - 1, -1, -1):
                _heapify(array, n, i)

            for i in range(n - 1, 0, -1):
                array[i], array[0] = array[0], array[i]
                _heapify(array, i, 0)

            return array

        tracemalloc.start()

        start_time = time.perf_counter()

        sorted_result = heap_sort(self._sorted_list.copy())

        end_time = time.perf_counter()

        mem, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        peak_mb = peak_memory / 1024 / 1024

        time_final = end_time - start_time

        print(sorted_result)
        print(f'Наше время при heap_sort на {len(sorted_result)} символов: {time_final} секунд')
        print(f'Максимальное количество памяти: {peak_mb:.4f} MB')

    def reversed_sort_n(self):
 
        def _heapify(array, n, i):

            The_best = i
            first = 2 * i + 1
            second = 2 * i + 2

            if first < n and array[first] > array[The_best]:
                The_best = first

            if second < n and array[second] > array[The_best]:
                The_best = second

            if The_best != i:
                array[i], array[The_best] = array[The_best], array[i]
                _heapify(array, n, The_best)

        def heap_sort(array):

            n = len(array)

            for i in range(n // 2 - 1, -1, -1):
                _heapify(array, n, i)

            for i in range(n - 1, 0, -1):
                array[i], array[0] = array[0], array[i]
                _heapify(array, i, 0)

            return array
 
        tracemalloc.start()

        start_time = time.perf_counter()

        sorted_result = heap_sort(self._reversed_list.copy())

        end_time = time.perf_counter()

        mem, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        peak_mb = peak_memory / 1024 / 1024

        time_final = end_time - start_time

        print(sorted_result)
        print(f'Наше время при heap_sort на {len(sorted_result)} символов: {time_final} секунд')
        print(f'Максимальное количество памяти: {peak_mb:.4f} MB')
 
    def sort_95_and_5_n(self):
            
        def _heapify(array, n, i):

            The_best = i
            first = 2 * i + 1
            second = 2 * i + 2

            if first < n and array[first] > array[The_best]:
                The_best = first

            if second < n and array[second] > array[The_best]:
                The_best = second

            if The_best != i:
                array[i], array[The_best] = array[The_best], array[i]
                _heapify(array, n, The_best)

        def heap_sort(array):

            n = len(array)

            for i in range(n // 2 - 1, -1, -1):
                _heapify(array, n, i)

            for i in range(n - 1, 0, -1):
                array[i], array[0] = array[0], array[i]
                _heapify(array, i, 0)

            return array
 
        tracemalloc.start()

        start_time = time.perf_counter()

        sorted_result = heap_sort(self._95_and_5.copy())

        end_time = time.perf_counter()

        mem, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        peak_mb = peak_memory / 1024 / 1024

        time_final = end_time - start_time

        print(sorted_result)
        print(f'Наше время при heap_sort на {len(sorted_result)} символов: {time_final} секунд')
        print(f'Максимальное количество памяти: {peak_mb:.4f} MB')

H = heap_sort(n)
H.random_sort_n()
H.sorted_sort_n()
H.reversed_sort_n()
H.sort_95_and_5_n()