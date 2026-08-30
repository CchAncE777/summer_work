import random
import time
import tracemalloc

n = int(input('Введите число элементов в списке: '))

class selection_sort:
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

        def selection_sort(array):

            for i in range(len(array)):
                min_index = i
            
                for j in range(i + 1, len(array)):
            
                    if array[j] < array[min_index]:
                        min_index = j
            
                array[i], array[min_index] = array[min_index], array[i]

            return array
            
        tracemalloc.start()

        start_time = time.perf_counter()

        sorted_result = selection_sort(self._random_list.copy())

        end_time = time.perf_counter()

        mem, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        peak_mb = peak_memory / 1024 / 1024

        time_final = end_time - start_time
                    
        print(sorted_result)
        print(f'Наше время при selection_sort на {len(sorted_result)} символов: {time_final} секунд')
        print(f'Максимальное количество памяти: {peak_mb:.4f} MB')

    def sorted_sort_n(self):
 
        def selection_sort(array):

            for i in range(len(array)):
                min_index = i
            
                for j in range(i + 1, len(array)):
            
                    if array[j] < array[min_index]:
                        min_index = j
            
                array[i], array[min_index] = array[min_index], array[i]

            return array
            
        tracemalloc.start()

        start_time = time.perf_counter()

        sorted_result = selection_sort(self._sorted_list.copy())

        end_time = time.perf_counter()

        mem, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        peak_mb = peak_memory / 1024 / 1024

        time_final = end_time - start_time
                    
        print(sorted_result)
        print(f'Наше время при selection_sort на {len(sorted_result)} символов: {time_final} секунд')
        print(f'Максимальное количество памяти: {peak_mb:.4f} MB')

    def reversed_sort_n(self):

        def selection_sort(array):

            for i in range(len(array)):
                min_index = i
            
                for j in range(i + 1, len(array)):
            
                    if array[j] < array[min_index]:
                        min_index = j
            
                array[i], array[min_index] = array[min_index], array[i]

            return array
        
        tracemalloc.start()

        start_time = time.perf_counter()

        sorted_result = selection_sort(self._reversed_list.copy())

        end_time = time.perf_counter()

        mem, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        peak_mb = peak_memory / 1024 / 1024

        time_final = end_time - start_time
                    
        print(sorted_result)
        print(f'Наше время при selection_sort на {len(sorted_result)} символов: {time_final} секунд')
        print(f'Максимальное количество памяти: {peak_mb:.4f} MB')

    def sort_95_and_5_n(self):

        def selection_sort(array):

            for i in range(len(array)):
                min_index = i
            
                for j in range(i + 1, len(array)):
            
                    if array[j] < array[min_index]:
                        min_index = j
            
                array[i], array[min_index] = array[min_index], array[i]

            return array
            
        tracemalloc.start()

        start_time = time.perf_counter()

        sorted_result = selection_sort(self._95_and_5.copy())

        end_time = time.perf_counter()

        mem, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        peak_mb = peak_memory / 1024 / 1024

        time_final = end_time - start_time
                    
        print(sorted_result)
        print(f'Наше время при selection_sort на {len(sorted_result)} символов: {time_final} секунд')
        print(f'Максимальное количество памяти: {peak_mb:.4f} MB')
    

S = selection_sort(n)
S.random_sort_n()
S.sorted_sort_n()
S.reversed_sort_n()
S.sort_95_and_5_n()