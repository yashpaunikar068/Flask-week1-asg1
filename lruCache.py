import time	
class Node:
	
	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.next = None
		self.prev = None


class LRUCache:
	cache_limit = None
	
	DEBUG = False

	def __init__(self, func):
		self.func = func
		self.cache = {}
		self.head = Node(0, 0)
		self.tail = Node(0, 0)
		self.head.next = self.tail
		self.tail.prev = self.head

	def __call__(self, *args, **kwargs):
		if args in self.cache:
			self.llist(args)
			
			if self.DEBUG == True:
				return f'Cached...{args}\n{self.cache[args]}\nCache: {self.cache}'
			return self.cache[args]

		if self.cache_limit is not None:
			
			if len(self.cache) > self.cache_limit:
				n = self.head.next
				self._remove(n)
				del self.cache[n.key]

		result = self.func(*args, **kwargs)
		self.cache[args] = result
		node = Node(args, result)
		self._add(node)
		
		if self.DEBUG == True:
			return f'{result}\nCache: {self.cache}'
		return result

	def _remove(self, node):
		p = node.prev
		n = node.next
		p.next = n
		n.prev = p

	def _add(self, node):
		p = self.tail.prev
		p.next = node
		self.tail.prev = node
		node.prev = p
		node.next = self.tail

	def llist(self, args):
		current = self.head
		
		while True:
			
			if current.key == args:
				node = current
				self._remove(node)
				self._add(node)
				
				if self.DEBUG == True:
					del self.cache[node.key]
					self.cache[node.key] = node.val
				break
			
			else:
				current = current.next


LRUCache.DEBUG = True

LRUCache.cache_limit = 3


@LRUCache
def ex_func_01(n):
	print(f'Computing...{n}')
	time.sleep(1)
	return n


print(f'\nFunction: ex_func_01')
print(ex_func_01(1))
print(ex_func_01(2))
print(ex_func_01(3))
print(ex_func_01(4))
print(ex_func_01(1))
print(ex_func_01(2))
print(ex_func_01(5))
print(ex_func_01(1))
print(ex_func_01(2))
print(ex_func_01(3))
print(ex_func_01(4))
print(ex_func_01(5))
