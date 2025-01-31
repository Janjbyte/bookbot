# Startar hela funktionen
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    lower_case = characters(text)
    print(f"A total of {get_num_words(text)} words counted in {book_path}")
    print()
    alph = alphabet(lower_case)

    for alp in alph:
        print(f"{alp} is counted {alph[alp]} times in the book") 

# Funktionen tar bara alfabetet    
def alphabet(lower_case):
    alph = {}
    for char in lower_case:
        letters = char.isalpha()
        if letters == True:
            if char in alph:
                alph[char] += 1
            else:
                alph[char] = 1
    return alph

# Skapade två funktioner för att först ändra till små bokstäver, därefter för att beräkna i dictionary
def characters(text):
    text_lower = text.lower()
    character = list(text_lower)
    return character


def get_characters(lower_case):
    counts = {}
    for chars in lower_case:
        if chars in counts:
            counts[chars] += 1
        else:
            counts[chars] = 1
    return counts
    

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