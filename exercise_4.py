"""4. Написать программу, которая сортирует список строк по длине, сначала по возрастанию, а затем по убыванию."""
def sort_length():
    programming_languages = ["Python", "Swift","Java", "C++", "Go", "Rust"]
    
    sorted_strings_asc = sorted(programming_languages, key=len)
    sorted_strings_desc = sorted(programming_languages, key=len, reverse=True)
    print(f'{sorted_strings_asc}, {sorted_strings_desc}')

sort_length()