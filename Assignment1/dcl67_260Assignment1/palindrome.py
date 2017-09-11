def isPalindrome(word):
	string = str(word)
	i = 0
	length = len(string) - 1
	while length > i:
		if string[i] != string[length]:
			print("The word is a palindrome: False")
			return False
		i = i + 1
		length = length - 1
	print("The word is a palindrome: True")
	return True


def main():
	calls = 0
	arePalindromes = 0
	isPalindrome("undertakes")
	print("1/8 tests successful.")
	isPalindrome("impassibly")
	print("2/8 tests successful.")
	isPalindrome("pop")
	print("3/8 tests successful.")
	isPalindrome("misericordia")
	print("4/8 tests successful.")
	isPalindrome("pup")
	print("5/8 tests successful.")
	isPalindrome("dinars")
	print("6/8 tests successful.")
	isPalindrome("misprisions")
	print("7/8 tests successful.")
	isPalindrome("tot")
	print("Success! Passed 8/8 tests.")

if __name__ == "__main__":
	main()
