import random
import tracemalloc
import time

n = int(input('Введите число элементов в списке: '))

class radix_sort:
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

        def radix_sort(array):

            if not array:
                return array
                
            min_number = min(array)
            
            if min_number < 0:
                array = [i - min_number for i in array]
                
            max_number = max(array)
            place = 1
            
            while max_number // place > 0:
                buckets = [[] for _ in range(10)]
                
                for num in array:
                    digit = (num // place) % 10
                    buckets[digit].append(num)
                        
                array = []

                for bucket in buckets:
                    array.extend(bucket)
                
                place *= 10
                
            if min_number < 0:
                array = [i + min_number for i in array]
                
            return array

        tracemalloc.start()

        start_time = time.perf_counter()

        sorted_result = radix_sort(self._random_list.copy())

        end_time = time.perf_counter()

        mem, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        peak_mb = peak_memory / 1024 / 1024

        time_final = end_time - start_time

        print(sorted_result)
        print(f'Наше время при radix_sort на {len(sorted_result)} символов: {time_final} секунд')
        print(f'Максимальное количество памяти: {peak_mb:.4f} MB')

    def sorted_sort_n(self):

        def radix_sort(array):

            if not array:
                return array
                
            min_number = min(array)
            
            if min_number < 0:
                array = [i - min_number for i in array]
                
            max_number = max(array)
            place = 1
            
            while max_number // place > 0:
                buckets = [[] for _ in range(10)]
                
                for num in array:
                    digit = (num // place) % 10
                    buckets[digit].append(num)
                        
                array = []

                for bucket in buckets:
                    array.extend(bucket)
                
                place *= 10
                
            if min_number < 0:
                array = [i + min_number for i in array]
                
            return array

        tracemalloc.start()

        start_time = time.perf_counter()

        sorted_result = radix_sort(self._sorted_list.copy())

        end_time = time.perf_counter()

        mem, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        peak_mb = peak_memory / 1024 / 1024

        time_final = end_time - start_time

        print(sorted_result)
        print(f'Наше время при radix_sort на {len(sorted_result)} символов: {time_final} секунд')
        print(f'Максимальное количество памяти: {peak_mb:.4f} MB')

    def reversed_sort_n(self):

        def radix_sort(array):

            if not array:
                return array
                
            min_number = min(array)
            
            if min_number < 0:
                array = [i - min_number for i in array]
                
            max_number = max(array)
            place = 1
            
            while max_number // place > 0:
                buckets = [[] for _ in range(10)]
                
                for num in array:
                    digit = (num // place) % 10
                    buckets[digit].append(num)
                        
                array = []

                for bucket in buckets:
                    array.extend(bucket)
                
                place *= 10
                
            if min_number < 0:
                array = [i + min_number for i in array]
                
            return array

        tracemalloc.start()

        start_time = time.perf_counter()

        sorted_result = radix_sort(self._reversed_list.copy())

        end_time = time.perf_counter()

        mem, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        peak_mb = peak_memory / 1024 / 1024

        time_final = end_time - start_time

        print(sorted_result)
        print(f'Наше время при radix_sort на {len(sorted_result)} символов: {time_final} секунд')
        print(f'Максимальное количество памяти: {peak_mb:.4f} MB')

    def sort_95_and_5_n(self):

        def radix_sort(array):

            if not array:
                return array
                
            min_number = min(array)
            
            if min_number < 0:
                array = [i - min_number for i in array]
                
            max_number = max(array)
            place = 1
            
            while max_number // place > 0:
                buckets = [[] for _ in range(10)]
                
                for num in array:
                    digit = (num // place) % 10
                    buckets[digit].append(num)
                        
                array = []

                for bucket in buckets:
                    array.extend(bucket)
                
                place *= 10
                
            if min_number < 0:
                array = [i + min_number for i in array]
                
            return array

        tracemalloc.start()

        start_time = time.perf_counter()

        sorted_result = radix_sort(self._95_and_5.copy())

        end_time = time.perf_counter()

        mem, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        peak_mb = peak_memory / 1024 / 1024

        time_final = end_time - start_time

        print(sorted_result)
        print(f'Наше время при radix_sort на {len(sorted_result)} символов: {time_final} секунд')
        print(f'Максимальное количество памяти: {peak_mb:.4f} MB')
        
R = radix_sort(n)
R.random_sort_n()
R.sorted_sort_n()
R.reversed_sort_n()
R.sort_95_and_5_n()