# 2 = test case
# 4 3 = n: number of students , k = threshold
# -1 -3 4 2 = arrival times for each student
# 4 2
# 0 -1 2 1

# arrivalTime < 0 : on time
# 0 < arrivalTime : late
# class cancel => YES, otherwise => NO

def classCancle(k, arr):
	n = 0
	for a in arr:
		if a <= 0: # on time
			n = n+1
		if k <= n:
			return "NO"
	return "YES"

if __name__ == '__main__':
	res = []
	tc = input()
	for _ in range(int(tc)):
		n, k = map(int,input().split())
		arr = [int(i) for i in input().split()]
		res.append(classCancle(k,arr))

	for _ in res:
		print(_)

