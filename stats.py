def number_of_words_in_string(book_text: str) -> int:
    return len(book_text.split())

def get_character_count(book_text: str) -> dict:
    final_dict = {}
    processed_text = book_text.lower()
    for el in processed_text: 
        if el in final_dict.keys():
            final_dict[el] += 1
        else:
            final_dict[el] = 1
    return final_dict
    
def sort_list_of_dictionaries(chars_dict: dict) -> list:
    final_list = []
    for el in chars_dict:
        final_list.append({"char": el, "num": chars_dict[el]})
    final_list.sort(reverse=True, key = lambda x: x["num"])
    return final_list
    