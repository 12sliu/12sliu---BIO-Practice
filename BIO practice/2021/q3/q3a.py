from itertools import product, permutations


n = input()

def go(target):
    # ended = False
    dictionary = {("","A"):0}
    for i in range(30):
        tempdict = {}
        for state in dictionary:
            # print(state, i)
            if dictionary[state] == i:
                thing = state[0]
                letter = state[1]
    #             print(thing, letter)
                if thing == target:
                    # print(f"{i}")
                    return i
                    # ended = True
                    # break
                if len(target) > len(thing):
                    value = (thing + letter, chr(ord(letter) + 1))
                    if value not in dictionary and value not in tempdict:
                        tempdict[value] = dictionary[state] + 1
                        # print(1)
                if len(thing) > 1:
                    value = (thing[1:] + thing[0], letter)
                    if value not in dictionary and value not in tempdict:
                        tempdict[value] = dictionary[state] + 1
    #                     print(2)
                    if len(thing) > 2:
                        if target[:2] != thing[:2]:
                            value = (thing[1] + thing[0] + thing[2:], letter)
                            if value not in dictionary and value not in tempdict:
                                tempdict[value] = dictionary[state] + 1
    #                             print(3)

    #     if ended:
    #         break
        dictionary.update(tempdict)
    return None
# count = 0
# i = 0
# pro = permutations("ABCDE", 5)
# for x in pro:
#     if go("".join(x)) > 5:
#         count += 1
#     i += 1
# # print(len(list(pro)))
# # print(pro[1])
#     # print("what")
#     # if go(i) > 5:
#     #     count += 1
# print(count)
# print(i)

print(go(n))
