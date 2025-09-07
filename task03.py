import timeit
import random

def insertion_sort(arr):
    '''Реалізація сортування вставками'''
    # Починаємо з другого елемента, оскільки перший вважається вже відсортованим
    for i in range(1, len(arr)):
        key = arr[i]  # Елемент, який ми хочемо вставити
        j = i - 1     # Індекс останнього елемента у відсортованій частині
        
        # Переміщуємо елементи відсортованої частини, які більші за key,
        # на одну позицію праворуч
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        # Вставляємо key на правильну позицію
        arr[j + 1] = key
        
    return arr

def merge_sort(arr):
    '''Реалізація сортування злиттям'''
    if len(arr) > 1:
        # Знаходимо середину масиву
        mid = len(arr) // 2
        
        # Ділимо масив на дві половини
        L = arr[:mid]  # Ліва частина
        R = arr[mid:]  # Права частина
        
        # Рекурсивно сортуємо обидві половини
        merge_sort(L)
        merge_sort(R)
        
        # Ініціалізуємо індекси для лівої, правої та основної частин
        i = j = k = 0
        
        # Зливаємо дві відсортовані половини в основний масив
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            
        # Додаємо залишки елементів з лівої частини, якщо вони є
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            
        # Додаємо залишки елементів з правої частини, якщо вони є
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            
    return arr

def timsort_using_sort_method(arr):
    '''Демонстрація Timsort через метод list.sort()'''
    arr.sort()
    return arr

def timsort_using_sorted_function(arr):
    '''Демонстрація Timsort через функцію sorted()'''
    return sorted(arr)

def main():
    '''Основна функція для генерації даних та тестування'''

    # Визачення кількості елементів для перевірки
    ARRAY_SIZE_SMALL = 1000
    ARRAY_SIZE_MEDIUM = 10000
    ARRAY_SIZE_BIG = 20000

    # Словник з назвами та функціями алгоритмів для тестування
    algorithms = {
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Timsort sort()": timsort_using_sort_method,
        "Timsort sorted()": timsort_using_sorted_function
    }

    # Генерація основного масиву даних
    # Використовуємо широкий діапазон, щоб зменшити кількість дублікатів
    original_data_small = [random.randint(0, ARRAY_SIZE_SMALL * 10) for _ in range(ARRAY_SIZE_SMALL)]
    original_data_medium = [random.randint(0, ARRAY_SIZE_MEDIUM * 10) for _ in range(ARRAY_SIZE_MEDIUM)]
    original_data_big = [random.randint(0, ARRAY_SIZE_BIG * 10) for _ in range(ARRAY_SIZE_BIG)]

    print("\n--- Підсумкова таблиця результатів ---")   
    print(f"{'Алгоритм': <20} | {'1000 елементів(сек)': <20} | {'10_000 елементів(сек)': <20} | {'20_000 елементів(сек)': <20}")
    print(f":------------------- | :------------------- | :-------------------- | :-------------------")

    # Цикл тестування для кожного алгоритму
    for name, sort_function in algorithms.items():
        # Створюємо свіжу копію даних для кожного тесту
        data_small_to_sort = original_data_small.copy()
        data_medium_to_sort = original_data_medium.copy()
        data_big_to_sort = original_data_big.copy()

        # Вимірюємо час виконання за допомогою timeit
        time_taken_small = timeit.timeit(lambda: sort_function(data_small_to_sort), number=1)
        time_taken_medium = timeit.timeit(lambda: sort_function(data_medium_to_sort), number=1)
        time_taken_big = timeit.timeit(lambda: sort_function(data_big_to_sort), number=1)

        print(f"{name: <20} | {time_taken_small:<20.6f} | {time_taken_medium:<21.6f} | {time_taken_big:<20.6f}")
    

if __name__ == "__main__":
    main()