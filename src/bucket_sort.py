import random
import tracemalloc
import time

n = int(input('Введите число элементов в списке: '))

class buckets_sort:
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

        def bucketss_sort(array):

            if len(array) <= 1:
                return array  
            
            max_number = max(array)
            min_number = min(array)

            if min_number == max_number:
                return array
            
            range_number = max_number - min_number
            buckets = [[] for _ in range(len(array))]

            for num in array:
                index = int((num - min_number) / range_number * (len(buckets) - 1))
                
                if index >= len(array):
                    index -= 1

                buckets[index].append(num)

            res = []
          
            for i in range(len(buckets)):
                buckets[i].sort()
                res.extend(buckets[i])

            return res

        tracemalloc.start()

        start_time = time.perf_counter()

        sorted_result = bucketss_sort(self._random_list.copy())

        end_time = time.perf_counter()

        mem, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        peak_mb = peak_memory / 1024 / 1024

        time_final = end_time - start_time

        print(sorted_result)
        print(f'Наше время при bucket_sort на {len(sorted_result)} символов: {time_final} секунд')
        print(f'Максимальное количество памяти: {peak_mb:.4f} MB')

    def sorted_sort_n(self):

        def bucketss_sort(array):

            if len(array) <= 1:
                return array  
            
            max_number = max(array)
            min_number = min(array)

            if min_number == max_number:
                return array
            
            range_number = max_number - min_number
            buckets = [[] for _ in range(len(array))]

            for num in array:
                index = int((num - min_number) / range_number * (len(buckets) - 1))
                
                if index >= len(array):
                    index -= 1

                buckets[index].append(num)

            res = []
          
            for i in range(len(buckets)):
                buckets[i].sort()
                res.extend(buckets[i])

            return res

        tracemalloc.start()

        start_time = time.perf_counter()

        sorted_result = bucketss_sort(self._sorted_list.copy())

        end_time = time.perf_counter()

        mem, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        peak_mb = peak_memory / 1024 / 1024

        time_final = end_time - start_time

        print(sorted_result)
        print(f'Наше время при bucket_sort на {len(sorted_result)} символов: {time_final} секунд')
        print(f'Максимальное количество памяти: {peak_mb:.4f} MB')

    def reversed_sort_n(self):

        def bucketss_sort(array):

            if len(array) <= 1:
                return array  
            
            max_number = max(array)
            min_number = min(array)

            if min_number == max_number:
                return array
            
            range_number = max_number - min_number
            buckets = [[] for _ in range(len(array))]

            for num in array:
                index = int((num - min_number) / range_number * (len(buckets) - 1))
                
                if index >= len(array):
                    index -= 1

                buckets[index].append(num)

            res = []
          
            for i in range(len(buckets)):
                buckets[i].sort()
                res.extend(buckets[i])

            return res

        tracemalloc.start()

        start_time = time.perf_counter()

        sorted_result = bucketss_sort(self._reversed_list.copy())

        end_time = time.perf_counter()

        mem, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        peak_mb = peak_memory / 1024 / 1024

        time_final = end_time - start_time

        print(sorted_result)
        print(f'Наше время при bucket_sort на {len(sorted_result)} символов: {time_final} секунд')
        print(f'Максимальное количество памяти: {peak_mb:.4f} MB')

    def sort_95_and_5_n(self):

        def bucketss_sort(array):

            if len(array) <= 1:
                return array  
            
            max_number = max(array)
            min_number = min(array)

            if min_number == max_number:
                return array
            
            range_number = max_number - min_number
            buckets = [[] for _ in range(len(array))]

            for num in array:
                index = int((num - min_number) / range_number * (len(buckets) - 1))
                
                if index >= len(array):
                    index -= 1

                buckets[index].append(num)

            res = []
          
            for i in range(len(buckets)):
                buckets[i].sort()
                res.extend(buckets[i])

            return res

        tracemalloc.start()

        start_time = time.perf_counter()

        sorted_result = bucketss_sort(self._95_and_5.copy())

        end_time = time.perf_counter()

        mem, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        peak_mb = peak_memory / 1024 / 1024

        time_final = end_time - start_time

        print(sorted_result)
        print(f'Наше время при bucket_sort на {len(sorted_result)} символов: {time_final} секунд')
        print(f'Максимальное количество памяти: {peak_mb:.4f} MB') 

Buck = buckets_sort(n)
Buck.random_sort_n()
Buck.sorted_sort_n()
Buck.reversed_sort_n()
Buck.sort_95_and_5_n()