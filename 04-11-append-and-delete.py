# append to END
# delete LAST char
# int k
# string s -k-> t (Y/N)

# s af
# d afddd
# 1) s = t abcd abcd
# 2) s < t abcd abcde
# 3) s > t abcde abcd

if __name__ == '__main__':
	s = input()
	t = input()
	k = input()

	s_l = len(s)
	t_l = len(t)
	m = 0

	if s_l < t_l:
		for i in range(s_l):
			if s[i] != t[i]:
				m = s_l + t_l - (i)*2
				break;
	elif s_l > t_l:
		for i in range(t_l):
			if s[i] != t[i]:
				m = s_l + t_l - (i)*2
				break;
	else:
		for i in range(s_l):
			if s[i] != t[i]:
				m = s_l + t_l - (i)*2
				break;

	if m == int(k):
		print('YES')
	else:
		print('NO')
