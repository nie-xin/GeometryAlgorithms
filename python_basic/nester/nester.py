def print_lol(the_list, nestedIntent=False, level=0):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, nestedIntent, level+1)
        else:
            if nestedIntent:
                for tab in range(level):
                    print("\t", end='')
                print(each_item)
            else:
                print(each_item)
