if __name__ == '__main__':
	n = input()
	print("YES" if sum(map(int, n[:3])) == sum(map(int, n[3:])) else "NO")
