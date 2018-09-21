import time



tuple1 = ('1110111', '0010010', '0111101', '0111011', '1011010', '1101011', '1101111', '0110010', '1111111', '1111011')
tuple2 = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6)
#123
# 4
#567
def main(a, b, c):
	result = []
	source = [a, b, c]
	sum1 = tuple2[a] + tuple2[b] + tuple2[c]
	for n1 in range(10):
		for n2 in range(10):
			if sum1 - tuple2[n1] - tuple2[n2] in tuple2 is True:
				thre = [tuple2[n1], tuple2[n2], sum1 - tuple2[n1] - tuple2[n2]]
				three = thre.sort()
				if three[2] - three[1] == three[0]:
					times = compare(source,thre)
					if times:
						result.append(thre.append(times))
	if result = []:
		print('无解')
	else:
		prem = []
		for grp in result:
			print('图案可变化为', grp[0], '+', grp[1], '=', grp[2], '共需移动', time, '根火柴棍。')
			prem.append(grp[3])
		minium = min(prem)
		index = [x for x in range(len(prem)) if prem[x] == minium]
		for r in index:
			print('最少移动', result[r][3],'根火柴棍，使得图案变为', result[r][0], '+', result[r][1], '=', result[r][2])

def copmare(src,tgt):
	count = 0
	m = 0
	for m in range(3):
		for n in range(7):
			if not tuple1[src[m]][n] == tuple1[tgt[m]][n]:
				count += 1
	if count % 2 == 0:
		return count / 2
def input_check():
	pass

num1, num2, num3 = list(map(int, input('请输入三个数字，以空格隔开').split()))
main(num1, num2, num3)