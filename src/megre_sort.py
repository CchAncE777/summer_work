import random
import time
import tracemalloc

n = int(input('Введите число элементов в списке: '))

class merge_sort:
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

        def _merge(fisrt, three):
            result = []
            i = j = 0

            while i < len(fisrt) and j < len(three):

                if fisrt[i] < three[j]:
                    result.append(fisrt[i])
                    i += 1
                else:
                    result.append(three[j])
                    j += 1

            result.extend(fisrt[i:])
            result.extend(three[j:])
            return result
        
                
        def merge_sort(array):

            if len(array) <= 1:
                return array
                    
            secong = len(array) // 2
            fisrt = merge_sort(array[:secong])
            three = merge_sort(array[secong:])
            return _merge(fisrt, three)
        
        tracemalloc.start()

        start_time = time.perf_counter()

        sorted_result = merge_sort(self._95_and_5.copy())

        end_time = time.perf_counter()

        mem, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        peak_mb = peak_memory / 1024 / 1024

        time_final = end_time - start_time

        print(sorted_result)
        print(f'Наше время при merge_sort на {len(sorted_result)} символов: {time_final} секунд')
        print(f'Максимальное количество памяти: {peak_mb:.4f} MB')

    def sorted_sort_n(self):
        
        def _merge(fisrt, three):
            result = []
            i = j = 0

            while i < len(fisrt) and j < len(three):

                if fisrt[i] < three[j]:
                    result.append(fisrt[i])
                    i += 1
                else:
                    result.append(three[j])
                    j += 1

            result.extend(fisrt[i:])
            result.extend(three[j:])
            return result
                
                        
        def merge_sort(array):
                
            if len(array) <= 1:
                return array
                            
            secong = len(array) // 2
            fisrt = merge_sort(array[:secong])
            three = merge_sort(array[secong:])
            return _merge(fisrt, three)

        tracemalloc.start()

        start_time = time.perf_counter()

        sorted_result = merge_sort(self._sorted_list.copy())

        end_time = time.perf_counter()

        mem, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        peak_mb = peak_memory / 1024 / 1024

        time_final = end_time - start_time

        print(sorted_result)
        print(f'Наше время при merge_sort на {len(sorted_result)} символов: {time_final} секунд')
        print(f'Максимальное количество памяти: {peak_mb:.4f} MB')

    def reversed_sort_n(self):
            
        def _merge(fisrt, three):

            result = []
            i = j = 0

            while i < len(fisrt) and j < len(three):

                if fisrt[i] < three[j]:
                    result.append(fisrt[i])
                    i += 1
                else:
                    result.append(three[j])
                    j += 1

            result.extend(fisrt[i:])
            result.extend(three[j:])
            return result
                
                        
        def merge_sort(array):
                
            if len(array) <= 1:
                return array
                            
            secong = len(array) // 2
            fisrt = merge_sort(array[:secong])
            three = merge_sort(array[secong:])
            return _merge(fisrt, three)
 
        tracemalloc.start()

        start_time = time.perf_counter()

        sorted_result = merge_sort(self._reversed_list.copy())

        end_time = time.perf_counter()

        mem, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        peak_mb = peak_memory / 1024 / 1024

        time_final = end_time - start_time

        print(sorted_result)
        print(f'Наше время при merge_sort на {len(sorted_result)} символов: {time_final} секунд')
        print(f'Максимальное количество памяти: {peak_mb:.4f} MB')

    def sort_95_and_5_n(self):

 
        def _merge(fisrt, three):

            result = []
            i = j = 0

            while i < len(fisrt) and j < len(three):

                if fisrt[i] < three[j]:
                    result.append(fisrt[i])
                    i += 1
                else:
                    result.append(three[j])
                    j += 1
                    
            result.extend(fisrt[i:])
            result.extend(three[j:])
            return result
                
                        
        def merge_sort(array):
                
            if len(array) <= 1:
                return array
                            
            secong = len(array) // 2
            fisrt = merge_sort(array[:secong])
            three = merge_sort(array[secong:])
            return _merge(fisrt, three)
 
        tracemalloc.start()

        start_time = time.perf_counter()

        sorted_result = merge_sort(self._95_and_5.copy())

        end_time = time.perf_counter()

        mem, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        peak_mb = peak_memory / 1024 / 1024

        time_final = end_time - start_time

        print(sorted_result)
        print(f'Наше время при merge_sort на {len(sorted_result)} символов: {time_final} секунд')
        print(f'Максимальное количество памяти: {peak_mb:.4f} MB')

M = merge_sort(n)
M.random_sort_n()
M.sorted_sort_n()
M.reversed_sort_n()
M.sort_95_and_5_n()
