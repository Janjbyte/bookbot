# Startar hela funktionen
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"I've found {num_words} words in the book")
    print(text)

# Skapar funktion för att räkna    
def get_num_words(text):
    words = text.split()
    return len(words)

# main gör att hela programmet läses av först
# Funktionen öppnar vägen till boken och returnerar boken        
def get_book_text(path):
    with open(path) as f:
        return f.read()

    

main()       