from palindrome import isPalindrome

def main():
	print("Welcome to Palindrome Checker!\nEnter a word. The program will tell you if it is a palindrome.\nTo quit enter a blank line.")
	string = input("Enter word to check: ")
	while string != "":
		isPalindrome(string)
		string = input("Enter word to check: ")

if __name__ == "__main__":
	main()
