def look(list_all):
   list_all.sort(key=lambda x : x[1])
   list_all.pop(0)
   result_list = []
   for i in list_all:
       if list_all[0][1] == i[1]:
            result_list.append(i[0])
   result_list.sort()
   return  result_list
   

if __name__ == '__main__':
    list_all = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        person = []
        person.append(name)
        person.append(score)
        list_all.append(person)
        
    result = look(list_all)
    for i in result:
        print(i)
        
        
        
