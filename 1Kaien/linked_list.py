lst = Linkedlist()
print(lst.is_empty()) #True
lst.add_first(1)  #1
print(lst.head()) #return 1
lst.add_first(2)  #2->1
lst.add_first(3)  #3->2->1
print(lst.tail()) #return 1
lst.add_last(4)  #3->2->1->4
lst.add_last(5)  #3->2->1->4->5
lst.add_last(6)  #3->2->1->4->5->6
lst.remove_first()  #2->1->4->5->6
lst.remove_last()  #2->1->4->5
lst.print_list()  #2->1->4->5
print(lst.is_empty()) #False
len(lst)  #return 4