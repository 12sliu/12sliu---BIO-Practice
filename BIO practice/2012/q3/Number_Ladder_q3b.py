import time

import Number_Ladder_lib as lib

start, end = input().split()
starttime = time.time()
# start, end = 26, 61
end = lib.num_to_str(end)


# def funct(num, goal, depth):
#     if num == goal:
#         return 0
#     if depth < 100:
#         arr = lib.transform(num)
#         if goal not in arr:
#             for i in arr:
# #                 print(depth + 1)
#                 print(i, arr)
#                 return funct(tuple(lib.str_to_array(i)), goal, depth + 1)
#         else:
#             return depth
#     return None
ans = []
for i in lib.arrayToStringDict:
    if lib.diff(lib.str_to_array("ZERO"), i) <= 5:
        for j in lib.arrayToStringDict[i]:
            ans.append(j)
print(len(ans))
#
# moves = 1
# ended = False
# dicti = {tuple(lib.str_to_array(lib.num_to_str(start))): 1}
#
# for i in range(100):
#     tempdict = {}
#     for j in dicti:
#         if dicti[j] == moves:
#             # print("INPUT: ", j)
#             for k in lib.transform(j):
# #                 print("result:", k, "end: ", end)
#                 if k == end:
#                     ended = True
#                     print(moves)
#                     break
#                 if tuple(lib.str_to_array(k)) not in dicti:
#                     tempdict[tuple(lib.str_to_array(k))] = moves + 1
# #                     print(tempdict)
#         if ended:
#             break
#     if ended:
#         break
#     moves += 1
# #     print(tempdict)
#     dicti.update(tempdict)
# #     print(dicti)
#
# if not ended:
#     print("not found")

print(time.time() - starttime)

# # print(funct(tuple(lib.str_to_array(lib.num_to_str(start))), tuple(lib.str_to_array(lib.num_to_str(end))), 1))
