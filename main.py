def get_file_contents(path: str) -> str:
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    return ""

def get_word_count(text: str) -> int:
    words = text.split()
    return len(words)

def count_characters(text: str) -> dict[str, int]:
    character_dict: dict[str, int] = dict()
    for char in text.lower():
        if char not in character_dict:
            character_dict[char] = 1
        else:
            character_dict[char] += 1
    return character_dict

def sort_counts_on(count_dict):
    return count_dict["amnt"]

def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_file_contents(book_path)
    word_count = get_word_count(file_contents)
    characters_counts = count_characters(file_contents)
    report_counts = []

    for char in characters_counts:
        if char.isalpha():
            count = dict()
            count["char"] = char
            count["amnt"] = characters_counts[char]
            report_counts.append(count)

    report_counts.sort(reverse=True, key=sort_counts_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words in book at {book_path}")
    print()
    for report_count in report_counts:
        print(f"The '{report_count["char"]}' character was found {report_count["amnt"]} times")
    print(f"--- End report ---")

main()
