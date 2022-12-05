def merge(arr, lf, mid, rg):
	# Your code
	# “ヽ(´▽｀)ノ”
	pass


def merge_sort(arr, lf, rg):
	if len(arr) == 1:  # базовый случай рекурсии
		return arr

	# запускаем сортировку рекурсивно на левой половине
	left = merge_sort(array[0 : len(array)/2])

	# запускаем сортировку рекурсивно на правой половине
	right = merge_sort(array[len(array)/2 : len(array)])

	# заводим массив для результата сортировки
	result = [] * len(array)

	# сливаем результаты
	l, r, k = 0, 0, 0
	while l < len(left) and r < len(right): 
	# выбираем, из какого массива забрать минимальный элемент
		if left[l] <= right[r]: 
			result[k] = left[l]
			l += 1
		else:
			result[k] = right[r]
			r += 1
		k += 1

  # Если один массив закончился раньше, чем второй, то
  # переносим оставшиеся элементы второго массива в результирующий
	while l < len(left):
		result[k] = left[l] # перенеси оставшиеся элементы left в result
		l += 1
		k += 1  
	while r < len(right): 
		result[k] = right[r] # перенеси оставшиеся элементы right в result
		r += 1
		k += 1
  
	return result 

def test():
	a = [1, 4, 9, 2, 10, 11]
	b = merge(a, 0, 3, 6)
	expected = [1, 2, 4, 9, 10, 11]
	assert b == expected
	c = [1, 4, 2, 10, 1, 2]
	merge_sort(c, 0 , 6)
	expected = [1, 1, 2, 2, 4, 10]
	assert c == expected

if __name__ == '__main__':
    test()