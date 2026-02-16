from main import *


def test_fiblst():
	assert list(FibonacciLst([])) == []
	assert list(FibonacciLst([0, 0, 0, 1])) == [0, 0, 0, 1]
	assert list(FibonacciLst(range(10))) == [0, 1, 2, 3, 5, 8]


def test_fiblst_getitem():
	assert list(FibonacciLstGetitem([])) == []
	assert list(FibonacciLstGetitem([0, 0, 0, 1])) == [0, 0, 0, 1]
	assert list(FibonacciLstGetitem(range(10))) == [0, 1, 2, 3, 5, 8]


def test_coroutine():

	coro = fib_coroutine(my_coro)
	gen = coro()

	assert gen.send(3) == [0, 1, 1]

	gen.send(None)
	assert gen.send(5) == [0, 1, 1, 2, 3]

	gen.send(None)
	assert gen.send(0) == []