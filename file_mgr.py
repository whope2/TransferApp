import json
import os.path, time


def stat():
    print(os.path.getmtime("photos.json"))
    print(os.path.getmtime("photos2.json"))
    if os.path.getmtime("photos2.json") > os.path.getmtime("photos.json"):
        new_file = "photos2.json"
    else:
        new_file = "photos.json"

    with open(new_file, "r") as new_file_hdl:
        print("stat on %s" % (new_file))
        photo_dict = json.load(new_file_hdl)
        return photo_dict

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

#add_photo("newfile")

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
        random_index = random.randint(0,photo_count)
        print("random_index: ", random_index)
        random_photo_dict = photo_list[random_index]
        return(random_photo_dict["filepath"])
        