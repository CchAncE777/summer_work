import random
import time
import tracemalloc

n = int(input('Введите число элементов в списке: '))

class insertion_sort:
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

        def insertion_sort(array):

            for i in range(1, len(array)):
                I = array[i]
                j = i - 1

                while j >= 0 and I < array[j]:
                    array[j + 1] = array[j]
                    j -= 1

                array[j + 1] = I

            return array

        tracemalloc.start()
        
        start_time = time.perf_counter()
        
        sorted_result = insertion_sort(self._random_list.copy())
        
        end_time = time.perf_counter()
        
        mem, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        peak_mb = peak_memory / 1024 / 1024
        
        time_final = end_time - start_time
                            
        print(sorted_result)
        print(f'Наше время при insertion_sort на {len(sorted_result)} символов: {time_final} секунд')
        print(f'Максимальное количество памяти: {peak_mb:.4f} MB')

    def sorted_sort_n(self):
        
        def insertion_sort(array):

            for i in range(1, len(array)):
                I = array[i]
                j = i - 1

                while j >= 0 and I < array[j]:
                    array[j + 1] = array[j]
                    j -= 1

                array[j + 1] = I

            return array

        tracemalloc.start()
        
        start_time = time.perf_counter()
        
        sorted_result = insertion_sort(self._sorted_list.copy())
        
        end_time = time.perf_counter()
        
        mem, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        peak_mb = peak_memory / 1024 / 1024
        
        time_final = end_time - start_time
                            
        print(sorted_result)
        print(f'Наше время при insertion_sort на {len(sorted_result)} символов: {time_final} секунд')
        print(f'Максимальное количество памяти: {peak_mb:.4f} MB')
    
    def reversed_sort_n(self):

        def insertion_sort(array):

            for i in range(1, len(array)):
                I = array[i]
                j = i - 1

                while j >= 0 and I < array[j]:
                    array[j + 1] = array[j]
                    j -= 1

                array[j + 1] = I

            return array

        tracemalloc.start()
        
        start_time = time.perf_counter()
        
        sorted_result = insertion_sort(self._reversed_list.copy())
        
        end_time = time.perf_counter()
        
        mem, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        peak_mb = peak_memory / 1024 / 1024
        
        time_final = end_time - start_time
                            
        print(sorted_result)
        print(f'Наше время при insertion_sort на {len(sorted_result)} символов: {time_final} секунд')
        print(f'Максимальное количество памяти: {peak_mb:.4f} MB')

    def sort_95_and_5_n(self):
                
        def insertion_sort(array):

            for i in range(1, len(array)):
                I = array[i]
                j = i - 1

                while j >= 0 and I < array[j]:
                    array[j + 1] = array[j]
                    j -= 1

                array[j + 1] = I

            return array

        tracemalloc.start()
        
        start_time = time.perf_counter()
        
        sorted_result = insertion_sort(self._95_and_5.copy())
        
        end_time = time.perf_counter()
        
        mem, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        peak_mb = peak_memory / 1024 / 1024
        
        time_final = end_time - start_time
                            
        print(sorted_result)
        print(f'Наше время при insertion_sort на {len(sorted_result)} символов: {time_final} секунд')
        print(f'Максимальное количество памяти: {peak_mb:.4f} MB')

In = insertion_sort(n)
In.random_sort_n()
In.sorted_sort_n()
In.reversed_sort_n()
In.sort_95_and_5_n()