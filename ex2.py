from lib.queue import Queue
q = Queue()

def hot_potato(name_list, num):

    for i in (name_list):
        #print(i)
        q.enqueue(i)
    #print(q.size())
    
    while(q.size()>1):
        for i in range(0,num):
            person=q.dequeue()
            q.enqueue(person)
            #print(person)
            if(i==num-1):
                x=q.dequeue()
                #print("out",x)
                
    remaining_person=q.dequeue()
    print(remaining_person)
    return remaining_person

hot_potato(["Susan","Brad","Kent","David"], 6)               # 回傳 "Brad"
hot_potato(["Bill","David","Susan","Jane","Kent","Brad"], 7) # 回傳 "Susan"