"""
CP1404 - Practical 10
Wikipedia API exercise
"""
import wikipedia

title = input("Enter page title: ").strip()
while title:
    try:
        page = wikipedia.page(title, auto_suggest=False)
        print(page.title)
        first_paragraph = page.summary.split("\n")[0]
        print(first_paragraph)
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(e.options)
    except wikipedia.exceptions.PageError:
        print(f'Page id "{title}" does not match any pages. Try another id!')
    print()
    title = input("Enter page title: ").strip()
print("Thank you.")
