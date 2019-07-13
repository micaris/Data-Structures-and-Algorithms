def angram_solution(s1, s2):
    a_list = list(s2)

    pos1= 0
    still_ok = True
    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(a_list) and not found:
            if s1[pos1] == a_list[pos2]:
                found= True
            else:
                pos2 += 1
        if found:
            a_list[pos2] =  None
        else:
            still_ok = False
        
        pos1 += 1
    return still_ok

print(angram_solution('abcd', 'bcda'))
a= [1,2,3,4]
b = ['a', 'b', 'c', 'd', 'e']

print( a + b)
del a[0]
print(a)
print(ord('c') - ord('a'))

#****************************************************************#

def test1():
    l = []
    for i in range(1000):
        l = l+ [i]
def test2():
    l = []
    for i in range(1000):
        l.append(i)
def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

from timeit import Timer

# t1 = Timer("test1()", "from __main__ import test1")
# print("concat ", t1.timeit(number=1000), "milliseconds")
# t2 = Timer("test2()", "from __main__ import test2")
# print("append ", t2.timeit(number=1000), "milliseconds")
# t3 = Timer("test3()", "from __main__ import test3")
# print("comprehension  ", t3.timeit(number=1000), "milliseconds")
# t4 = Timer("test4()", "from __main__ import test4")
# print("range ", t4.timeit(number=1000), "milliseconds")

#****************************************************************#

# implementation of a stack
from  Stack import Stack

s = Stack()
print(s.is_empty())
s.push(4)
s.push('dog')
print(s.size())
s.push(8.5)
print(s.peek())


def rev_string(my_str):
    str_arr = Stack()

    for i in range(len(my_str)):
        str_arr.push(my_str[i])
    
    rev_str = ""

    for i in range(len(my_str)):
        rev_str += str_arr.pop()

    return rev_str


     
#****************************************************************#
#Converting Decimal Numbers to Binary Numbers with Stacks


def divide_by_2(dec_number):
    rem_stack = Stack()

    while dec_number > 0:
        rem = dec_number % 2
        rem_stack.push(rem)
        dec_number = dec_number // 2

    bin_strin = ""
    while not rem_stack.is_empty():
        bin_strin = bin_strin + str(rem_stack.pop())

    return bin_strin

#****************************************************************#
# Infix, prefix and post fix using Stacks

def infix_to_postfix(infix_expr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789" :
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and  (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)

# print(infix_to_postfix("( A + B ) * ( C + D )"))
# print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))


#****************************************************************#
# QUEUES

from Queue import Queue

q = Queue()
q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)
q.dequeue()
print(q.items)



#****************************************************************#
# SIMULATE PRINTING 
# class Printer
# class tasks
#
#
#
#
#
#
#
#
#
#
#
#
#****************************************************************#
# DEQUES

from Deque import Deque

def pal_checker(a_string):
    char_deque = Deque()

    for ch in a_string:
        char_deque.add_rear(ch)

    still_equal = True
    while char_deque.size() > 1 and still_equal:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last :
            still_equal = False

    return still_equal

print(pal_checker("lsdkjfskf"))
print(pal_checker("radar"))

#****************************************************************#
# Linked List

from Unordered_linked_list  import Node
temp = Node(93)
print(temp.get_data())



def sum_rec(list_num):
    if len(list_num) == 1:
        return list_num[0]
    else:
        return list_num[0] + sum_rec(list_num[1:])


# def search_from(maze, start_row, start_column):
#     maze.update_position(start_row, start_column)
#     #Check for base cases
#     #1. we ahev run untop an obstatcle, return false
#     if maze[start_row][start_column] == OBSTACLE :
#         return False   

#     #We have found  asquare that has already been explored
#     if maze[start_row][start_column] == TRIED:
#         return False
#     #3. Success, an outside edge not occupied by an obstacle
#     if maze.is_exit(start_row, start_column):
#         maze.update_position(start_row, start_column, PART_OF_PATH)
#         return True

#     maze.update_position(start_row, start_column, TRIED)

#     found = search_from(maze, start_row - 1, start_column) or \
#             search_from(maze, start_row + 1, start_column) or \
#             search_from(maze, start_row, start_column- 1) or \
#             search_from(maze, start_row , start_column+ 1)

#     if found:
#         maze.update_position(start_row, start_column, PART_OF_PATH)
#     else:
#         maze.update_position(start_row, start_column, DEAD_END)
#     return found

def sequential_search(a_list, item):
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    return found

def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint  = (first + last ) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequential_search(test_list, 3))
print(sequential_search(test_list, 32))
print("*********************************")

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(test_list, 3))
print(binary_search(test_list, 13))


#****************************************************************#
# Hashing tables

def hash(a_string, tables_size):
    sum = 0
    for pos in range(len(a_string)):
        sum = sum  + ord(a_string[pos])

    return sum % tables_size



