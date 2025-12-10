#
import sys


def main(argv):
	if len(argv) >= 3:
		try:
			a = int(argv[1])
			b = int(argv[2])
		except ValueError:
			print("请提供整数参数，例如: python3 hello_python.py 3 4")
			return 1
	else:
		print("Hello World from Python!")
		try:
			a = int(input('Enter first integer: '))
			b = int(input('Enter second integer: '))
		except Exception:
			print('输入无效')
			return 1

	print(f"Sum of {a} and {b} is {a + b}")
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv))

