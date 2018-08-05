def bubble_sort(my_list):
    length= len(my_list)
    for i in range(0, length - 1): #有n-1回合
        for j in range(0,length -1 -i): #每回合進行比較的範圍
            if my_list[j] > my_list[j+1]: 
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list
    
def quick_sort(my_list): 
    smaller_list = []
    bigger_list = []
    key_list = []

    if len(my_list) <= 1:
        return my_list

    else:
        key = my_list[0] #第一個數為key值
        for i in my_list:
            if i < key: 
                smaller_list.append(i)
            elif i > key: 
                bigger_list.append(i)
            else:
                key_list.append(i)

    smaller_list = quick_sort(smaller_list)
    bigger_list = quick_sort(bigger_list)
    return smaller_list + key_list + bigger_list


some_list = [
    65, 81, 65, 19, 6, 28, 86, 40, 72, 27,
    76, 46, 22, 98, 49, 57, 52, 46, 47, 14,
    29, 15, 59, 74, 61, 47, 20, 33, 89, 99,
    65, 82, 84, 63, 93, 1, 42, 13, 54, 58,
    84, 17, 5, 18, 14, 14, 19, 42, 60, 77,
    17, 29, 2, 42, 42, 31, 47, 67, 15, 16,
    71, 56, 98, 46, 18, 20, 14, 36, 42, 23,
    87, 7, 5, 5, 52, 78, 76, 91, 92, 88, 38,
    66, 13, 18, 68, 96, 23, 51, 77, 93, 35,
    18, 9, 64, 51, 76, 76, 96, 5, 18
]      
print ( bubble_sort(some_list) )
print ( quick_sort(some_list) )