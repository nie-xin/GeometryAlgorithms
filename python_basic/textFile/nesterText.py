import sys

def print_lol(the_list, nestedIntent=False, level=0, fn=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, nestedIntent, level+1, fn)
        else:
            if nestedIntent:
                for tab in range(level):
                    print("\t", end='', file=fn)
                print(each_item)
            else:
                print(each_item, file=fn)