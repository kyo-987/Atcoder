A1,A2,A3 = map(int, input().split())

num_list=[A1,A2,A3]

sort_list=sorted(num_list)
if sort_list[0]-sort_list[1]==sort_list[1]-sort_list[2]:
    print("Yes")
else:
    print("No")