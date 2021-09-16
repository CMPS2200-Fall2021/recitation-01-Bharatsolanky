"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
#from tabulate import tabulate
import time


def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1

def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1

def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)


def _binary_search(mylist, key, left, right):
	"""
	Recursive implementation of binary search.

	Params:
	  mylist....list to search
	  key.......search key
	  left......left index into list to search
	  right.....right index into list to search

	Returns:
	  index of key in mylist, or -1 if not present.
	"""

	mid = int((right+left)/2)
	if(mylist[mid] == key):
		return mid
	elif(mylist[right] == key):
		return right
	elif(mylist[left] == key):
		return left
	else:
		if(mylist[mid] < key):
			left = mid
			if((right-left) <= 2):
				if(mylist[mid] != key):
					return -1
			else:
				_binary_search(mylist, key, left, right)
		elif(mylist[mid] > key):
			right = mid
			if((right-left) <= 2):
				if(mylist[mid] != key):
					return -1
			else:
				_binary_search(mylist, key, left, right)



def test_binary_search():
	assert binary_search([1,2,3,4,5], 5) == 4
	assert binary_search([1,2,3,4,5], 1) == 0
	assert binary_search([1,2,3,4,5], 6) == -1

	assert binary_search([1,2,3,4,5], -3) == -1
	assert binary_search([1,2,3,4,5], 3) == 2



def time_search(search_fn, mylist, key):
	"""
	Return the number of milliseconds to run this
	search function on this list.

	Note 1: `sort_fn` parameter is a function.
	Note 2: time.time() returns the current time in seconds.
	You'll have to multiple by 1000 to get milliseconds.

	Params:
	  sort_fn.....the search function
	  mylist......the list to search
	  key.........the search key

	Returns:
	  the number of milliseconds it takes to run this
	  search function on this input.
	"""
	a = time.time()
	search_fn(mylist, key)
	b = time.time()
	return ((b-a)*1000)



def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	"""
	Compare the running time of linear_search and binary_search
	for input sizes as given. The key for each search should be
	-1. The list to search for each size contains the numbers from 0 to n-1,
	sorted in ascending order.

	You'll use the time_search function to time each call.

	Returns:
	  A list of tuples of the form
	  (n, linear_search_time, binary_search_time)
	  indicating the number of milliseconds it takes
	  for each method to run on each value of n
	"""
	list1 = [0]
	n1 = sizes[0]
	i = 0
	while i < n1:
		list1.append(i)
		i += 1
#	print(list1[len(list1)-1])

	list2 = [0]
	n2 = sizes[1]
	i = 0
	while i < n2:
		list2.append(i)
		i += 1
#	print(list2[len(list2)-1])


	tup1 = (sizes[0], time_search(linear_search, list1, -1), time_search(binary_search, list1, -1))
#	return tup1

	tup2 = (sizes[1], time_search(linear_search, list2, -1), time_search(binary_search, list2, -1))
#	return tup2

	flist = [tup1, tup2]
	return flist
	### TODO


def print_results(results):

	print(tabulate.tabulate(results,
		headers=['n', 'linear', 'binary'],
		floatfmt=".3f",
		tablefmt="github"))


def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1

print_results(compare_search())
