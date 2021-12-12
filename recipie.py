import webbrowser as wb
def youtube(recipe):
    spaced_removed=recipe.replace(" ","+")
    wb.open('https://www.youtube.com/results?search_query=' + spaced_removed)
def google(recipe):
    spaced_removed=recipe.replace(" ","+")
    wb.open('https://www.google.com/search?q=' + spaced_removed)
def wikipedia(recipe):
    spaced_removed=recipe.replace(" ","_")
    wb.open('https://en.wikipedia.org/wiki/' + spaced_removed)
