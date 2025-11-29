"""
CP1404 - Practical 10
Wikipedia API exercise
"""
from wikipedia import wikipedia

title = input("Enter page title: ").strip()
while title:
    page = wikipedia.page(title, auto_suggest=False)
    print(page.title)
    first_paragraph = page.summary.split("\n")[0]
    print(first_paragraph)
    print(page.url)
    print()
    title = input("Enter page title: ").strip()
print("Thank you.")
