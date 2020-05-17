import json
import os.path, time


def stat():
    print(os.path.getmtime("photos.json"))
    print(os.path.getmtime("photos2.json"))
    if os.path.getmtime("photos2.json") > os.path.getmtime("photos.json"):
        new_file = "photos2.json"
    else:
        new_file = "photos.json"
    
    file2 = "quotes.json"

    with open(new_file, "r") as new_file_hdl:
        print("stat on %s" % (new_file))
        photo_dict = json.load(new_file_hdl)

    with open(file2, "r") as file2_hdl:
        print("stat on %s" % (file2))
        dict2 = json.load(file2_hdl)
    
    dict2.update(photo_dict)
    return(dict2)

def add_photo(filepath):

    #photo_data is a dict
    #photo_list is an array
    photo_list = []

    print(os.path.getmtime("photos.json"))
    print(os.path.getmtime("photos2.json"))
    print("photos.json Last modified: %s" % time.ctime(os.path.getmtime("photos.json")))
    print("photos2.json Last modified: %s" % time.ctime(os.path.getmtime("photos2.json")))

    if os.path.getmtime("photos2.json") > os.path.getmtime("photos.json"):
        new_file = "photos2.json"
        old_file = "photos.json"
    else:
        new_file = "photos.json"
        old_file = "photos2.json"

    with open(old_file, "w") as old_file_hdl:
        with open(new_file, "r") as new_file_hdl:
            #always operate on the newer file
            print("operate on %s, write to %s" % (new_file, old_file))
            photo_dict = json.load(new_file_hdl)
            print("photo_dict:\n", photo_dict)
            photo_list = photo_dict["photos"] 
            print("photo_list_len:\n", len(photo_list))
            photo_count = photo_dict["photo_count"]
            print("photo_count: ", photo_count)
            entry_new = {'index':photo_count,'filepath':filepath}
            photo_list.append(entry_new)
            photo_dict["photo_count"] = photo_count+1
            print(photo_dict)
            json.dump(photo_dict, old_file_hdl, indent = 4)

    #backup the file
    cp_cmd = 'cp "%s" "%s"' % (old_file, "photos_backup.json")
    os.system(cp_cmd)

import random
def get_a_random_photo() :

    json_file = "photos.json"
    with open(json_file, "r") as file_hdl:
        photo_dict = json.load(file_hdl)
        print("photo_dict:\n", photo_dict)
        photo_list = photo_dict["photos"] 
        print("photo_list_len:\n", len(photo_list))
        photo_count = photo_dict["photo_count"]
        print("photo_count: ", photo_count)
        random_index = random.randint(0,photo_count-1)
        print("random_index: ", random_index)
        random_photo_dict = photo_list[random_index]
        return(random_photo_dict["filepath"])

def get_a_random_quote() :

    json_file = "quotes.json"
    with open(json_file, "r") as file_hdl:
        quote_dict = json.load(file_hdl)
        quote_list = quote_dict["quotes"] 
        print("quote_list_len:\n", len(quote_list))
        quote_count = quote_dict["quote_count"]
        random_index = random.randint(0,quote_count-1)
        print("random_index: ", random_index)
        random_dict = quote_list[random_index]
        return(random_dict["text"] + "  By " + random_dict["author"])


def upload_a_quote(text, author):

    #quote_data is a dict
    #quote_list is an array
    quote_list = []
    quote_file = "quotes.json"
    quote_backup_file = "quotes_backup.json"

    with open(quote_file, "r+") as file_hdl:
        print("operate on %s" % (quote_file))
        quote_dict = json.load(file_hdl)
        print("quote_dict:\n", quote_dict)
        quote_list = quote_dict["quotes"] 
        print("quote_list_len:\n", len(quote_list))
        quote_count = quote_dict["quote_count"]
        print("quote_count: ", quote_count)
        entry_new = {'index':quote_count,'text':text,'author':author}
        quote_list.append(entry_new)
        quote_dict["quote_count"] = quote_count+1
        print(quote_dict)
        file_hdl.seek(0)
        json.dump(quote_dict, file_hdl, indent = 4)

    #backup the file
    cp_cmd = 'cp "%s" "%s"' % (quote_file, quote_backup_file)
    os.system(cp_cmd)