def get_num_words(text):
    num_words = len(text.split())
    print(f'Found {num_words} total words')

def get_char_count(text):
    char_count_dict = {}
    for i in text:
        i = i.lower()
        if i not in char_count_dict:
            char_count_dict[i] = 1
        else:
            char_count_dict[i] += 1
    return char_count_dict

def sort_on(dict):
    return dict["num"]

def sort_list_of_dicts(dict):
    list_of_dicts = []
    #print(dict)
    for i in dict:
        final = {}
        if i.isalpha(): 
            final["char"] = i
            final["num"] = dict[i]
            list_of_dicts.append(final)
    list_of_dicts.sort(reverse=True,key=sort_on)
    for item in list_of_dicts:
        print(f"{item['char']}: {item['num']}")
   


            
