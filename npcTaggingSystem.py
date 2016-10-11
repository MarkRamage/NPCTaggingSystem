import pickle
from collections import namedtuple

tags = namedtuple('tags',['Name','Number'])
npcs = namedtuple('npcs', ['Name','Number'])
tags_list = []
npc_list = []
primes_list = []

def run():
    print('test')
    global tags, tags_list, npc, npc_list
    primes()
    try:
        with open('tags_list.p', 'rb') as f:
            tags_list = list(pickle.load(f))
    except IOError:
        print("1: File does not exist")
        pickle.dump(tags_list, open('tags_list.p', 'wb'))
    try:
        with open('npc_list.p', 'rb') as f:
            npc_list = list(pickle.load(f))
    except IOError:
        print("2: File does not exist")
        pickle.dump(npc_list, open('npc_list.p', 'wb'))
    running = True
    while running:
        choice = choose()
        if choice == 1:
            for tag in tags_list:
                print(tag[0])
        if choice == 2:
            newTag = input("Please enter this new tag's name\n")
            new_number = primes_list[len(tags_list)]
            new_tag = tags(newTag, new_number)
            print(new_tag)
            tags_list.append(new_tag)
        if choice == 3:
            selected_npcs =tagSearch()
            print("\nHere are all the npcs that match your tags\n\n")
            for nps in selected_npcs:
                print(nps[0])
            print("\n")
        if choice == 4:
            npc_name = input("Please enter the name of this NPC: ")
            print("Here are all the tags and their numbers")
            for tag in tags_list:
                print(tag[0] + "       " + str(tag[1]))
            new_npc_tags = input("Please enter the product of all the tags that apply to this npc: ")
            new_npc = npcs(npc_name, new_npc_tags)
            npc_list.append(new_npc)
        if choice == 5:
            print("\nThis is the list of npcs in this database\n")
            for nps in npc_list:
                print(nps[0]+"\n")
            old_npc = input("Please enter the name of the npc you wish to edit, EXACTLY: ")
            isname = False
            for nps in npc_list:
                if old_npc == nps[0]:
                    isname = True
                    print("These are the tags available")
                    for tag in tags_list:
                        print(tag[0]+"      "+str(tag[1]))
                    added_tag = input("Enter the number of the tag to remove, if you want to remove multiple tags, multiply it:")
                    new_npc = npcs(nps[0],int(nps[1])*int(added_tag))
                    npc_list.remove(nps)
                    npc_list.append(new_npc)
        if choice == 6:
            print("\nThis is the list of npcs in this database\n")
            for nps in npc_list:
                print(nps[0]+"\n")
            old_npc = input("Please enter the name of the npc you wish to edit, EXACTLY: ")
            isname = False
            for nps in npc_list:
                if old_npc == nps[0]:
                    isname = True
                    print("These are the tags available")
                    for tag in tags_list:
                        print(tag[0]+"      "+str(tag[1]))
                    remove_tag = input("Enter the number of the tag to remove, if you want to remove multiple tags, multiply it:")
                    if int(nps[1]) % int(remove_tag) == 0:
                        new_npc = npcs(nps[0],int(nps[1])/int(remove_tag))
                        npc_list.remove(nps)
                        npc_list.append(new_npc)
                    else:
                        print("that tag does not appear in this NPC")
        if choice == 7:
            running = False
    pickle.dump(tags_list, open('tags_list.p', 'wb'))
    pickle.dump(npc_list, open('npc_list.p', 'wb'))
    print("Goodbye")


def choose():
    while True:
       choice = input('What would you like to do?\n 1 = See list of Tags\n 2 = Add new tag\n 3 = Search by tags\n 4 = Add new NPC\n 5 = Add new tag to old NPC\n 6 = Remove tag from existing NPC\n 7 = Exit')
       try:
           choice = int(choice)
           if choice in (1,2,3,4,5,6,7):
               return  choice
       except ValueError:
           pass
       print("That wasn't a valid option")


def tagSearch():
    print("Here are all of the tags, and their numbers")
    for tag in tags_list:
        print(tag[0] +"       " + str(tag[1]))
    choice = input("Multiply all of the tags' numbers together, and enter that product here:")
    try:
        choice = int(choice)
        sorted_npcs = []
        for nps in npc_list:
            tag_thing = int(nps[1])
            tag_clear = tag_thing%choice
            if tag_clear == 0:
                sorted_npcs.append(nps)
        return sorted_npcs
    except ValueError:
        pass


def primes():
    global primes_list
    for i in range(2,4000):
        for j in range(2,i):
            if (i%j == 0):
                break
        else:
            primes_list.append(i)


if  __name__ == "__main__":
    run()
