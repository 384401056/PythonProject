# coding:utf-8

def main():
	prove(1)


def prove(n):
	
	print("现在开始证明P(%d)成立。"% n)

	k = 0
	print("根据步骤1得出P(%d)成立。"% k)

	while k < n:
		print("根据步骤2可以说  若P(%d)成立, 则P(%d)也成立 "% k, k+1)


if __name__ == '__main__':
	main()