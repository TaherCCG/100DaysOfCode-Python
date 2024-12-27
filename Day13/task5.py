word_per_page = 0
pages = int(input("Number of pages: "))
print(pages)
# The assignment for word_per_page should use a single equals sign (=)
# of double equals signs (==). The double equals signs are used for comparison, not assignment.
# word_per_page == int(input("Number of words per page: "))

word_per_page = int(input("Number of words per page: "))
print(word_per_page)


total_words = pages * word_per_page
print(total_words)