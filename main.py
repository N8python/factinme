from tkinter import *
import spacy
import textacy.extract
nlp = spacy.load("en_core_web_sm")
def analyze(e):
    data = content.get("1.0", END)
    word = keyword.get()
    doc = nlp(data)
    statements = textacy.extract.semistructured_statements(doc, word)
    facts = []
    for subject, verb, fact in statements:
        facts.append(f"- {fact}")
    results["text"] = "{0}:\n {1}".format(word, "\n".join(facts))
window = Tk()
window.title("Fact in Me")

Label(window, text="Enter some text to search:").pack()
content = Text(window, height=10)
content.pack()

Label(window, text="Enter a keyword to learn about:").pack()
keyword = Entry(window)
keyword.pack()

search = Button(window, text="Search")
search.bind("<Button-1>", analyze)
search.pack()

results = Label(window, text="")
results.pack()



window.mainloop()

