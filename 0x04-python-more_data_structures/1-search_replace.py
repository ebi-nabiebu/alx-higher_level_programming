#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def rep_elt(elt):
        return (elt if elt != search else replace)
    return list(map(rep_elt, my_list))
