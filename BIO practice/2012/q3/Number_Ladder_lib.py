from functools import lru_cache

numberToLetterDict = {
    1: "ONE",
    2: "TWO",
    3: "THREE",
    4: "FOUR",
    5: "FIVE",
    6: "SIX",
    7: "SEVEN",
    8: "EIGHT",
    9: "NINE",
    0: "ZERO"
}


def str_to_num(string):
    newstring = string.replace("ONE", "1")\
                 .replace("TWO", "2")\
                 .replace("THREE", "3")\
                 .replace("FOUR", "4")\
                 .replace("FIVE", "5")\
                 .replace("SIX", "6")\
                 .replace("SEVEN", "7")\
                 .replace("EIGHT", "8")\
                 .replace("NINE", "9")
    for i in newstring:
        if ord(i) > 10:
            return None
    return int(newstring)

def num_to_str(num):
    return "".join([numberToLetterDict[int(x)] for x in str(num)])

def str_to_array(string):
    arr = [0 for x in range(27)]
    for letter in string:
        arr[ord(letter)-65] += 1
    return arr


def create_array_str():
    dictionary = {}
    for i in range(1, 1001):
        string = num_to_str(i)
        thing = str_to_array(string)
        tuplething = tuple(thing)
        if tuplething not in dictionary:
            dictionary[tuplething] = [string]
        else:
            dictionary[tuplething].append(string)
    return dictionary


arrayToStringDict = create_array_str()
# print(arrayToStringDict)


def diff(strarray1, strarray2):
    count = 0
    for i in range(26):
        count += abs(strarray1[i] - strarray2[i])
    return count


@lru_cache()
def transform(strarray):
    # dict = {strarray: 0}
    ans = []
    for i in arrayToStringDict:
        if diff(strarray, i) <= 5:
            for j in arrayToStringDict[i]:
                ans.append(j)
    # moves = 0
#     while moves < 5:
# #         # print(ans)
#         tempdict = {}
#         for i in dict:
#             if dict[i] == moves:
#                 for j, letterplace in enumerate(i):
#                     if letterplace > 0:
#                         thing = list(i)
#                         thing[j] -= 1
#                         tuplething = tuple(thing)
#                         tempdict[tuplething] = moves + 1
#                         if tuplething in arrayToStringDict:
#                             for k in arrayToStringDict[tuplething]:
#                                 if k not in ans:
# #                                     print(k)
#                                     ans.append(k)
#                     thing = list(i)
#                     thing[j] += 1
#                     tuplething = tuple(thing)
#                     tempdict[tuplething] = moves + 1
#                     if tuplething in arrayToStringDict:
#                         for k in arrayToStringDict[tuplething]:
#                             if k not in ans:
# #                                 print(k)
#                                 ans.append(k)
                # for j, letter in enumerate(i):
                #     thing = i[:j] + i[j+1:]
                #     if thing not in dict:
#                 #         print(i, thing)
                #         tempdict[thing] = moves + 1
                #         if str_to_num(thing) is not None and thing not in ans:
                #             ans.append(thing)
                # for j in range(1, 27):
                #     letter = chr(64+j)
                #     for k in range(len(i)):
                #         thing = i[:k] + letter + i[k:]
                #         if thing not in dict:
#                 #             print(i, thing, moves)
                #             tempdict[thing] = moves + 1
                #             if str_to_num(thing) is not None and thing not in ans:
                #                 ans.append(thing)
        # dict.update(tempdict)
        # moves += 1
#     print(ans)
    return ans

# # print(num_to_str(234))
