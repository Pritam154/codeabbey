#!/usr/bin/python

'''
# Problem 1:
a = 7889826
b = 2927881
result = a + b
print(result)
'''

'''
# Problem 2
a = 35
b =[509, 811, 1130, 1189, 1113, 197, 1293, 70, 1100, 1178, 790, 949, 211, 813,
    600, 1274, 289, 775, 896, 268, 828, 994, 81, 878, 942, 820, 402, 1248, 781,
    949, 275, 1280, 460, 104, 1169]
# len(b)
# print(len(b))

result = 0
for x in range(0, len(b), +1):
    print("at " + str(x) + " and curr result is " + str(result))
    result += b[x]

print(result)
'''
'''
total = 0
count = int(input())
many = input().split(" ")

for i in many:
    total += int(i)
print(total)
'''
'''
# Problem 3
# count = 13
# arr = [["852676", "41805"], ["485070", "825170"], ["394445", "794233"],
        ["626102", "821612"], ["183606", "929683"], ["849549", "711964"],
        ["921384", "526339"], ["347476", "529585"], ["609756", "765887"],
        ["893877", "622166"], ["262187", "711219"], ["238239", "301841"],
        ["830073", "377723"]]

count = 12
arr =[[558423,409720],
[49898,161030],
[513632,155353],
[645154,911117],
[805906,941723],
[890034,439196],
[473132,99128],
[959781,971680],
[250837,331515],
[714639,168503],
[885954,955744]]

rst = ""
for x in range(0, len(arr), 1):
    a = int(arr[x][0])
    b = int(arr[x][1])
    rst = rst + " " + str(a + b)
    # print(rst)
print(rst)
'''

'''May 13th 2015
# Problem 4

25
arr = [[6719807,8753994],
[-7002257,-3722230],
[5219680,8268428],
[5109650,-933446],
[9361246,3168647],
[2202208,-520298],
[-2346490,-4755058],
[-1000515,-7878844],
[-4464129,-6444290],
[-6028444,8396867],
[5022816,-2935482],
[8433444,-789798],
[-8465557,8978278],
[-2202361,238188],
[7898194,7513787],
[-9202090,4618002],
[6267781,-6204347],
[-9104228,1487462],
[-7935918,6005422],
[-9445983,-8574671],
[-825931,2756224],
[905030,6827578],
[8001166,9904515],
[8948734,-6462963],
[-6539775,-7079709]]
rst = ""
for x in range(0, len(arr), 1):
    a = int(arr[x][0])
    b = int(arr[x][1])
    c = min(a,b)
    rst = rst + " " + str(c)
    print(rst)
'''

'''
# Problem 5 May 13th 2015

arr = [[-5487326,7727434,-2262487],
[-2373589,7155160,7587807],
[1359721,-1313978,-5594094],
[-1692398,7855672,-7758510],
[383060,7429178,9672805],
[7039394,8010079,6553547],
[1098419,-9528970,3449639],
[7550612,6072417,-3265914],
[-7287272,7135390,-3650625],
[8372330,7543642,5662218],
[2314466,-7943683,3389652],
[-9948020,-317272,544813],
[7639787,-8957550,9230834],
[-7954306,-649949,7086507],
[-5712817,9733110,4515685],
[-6040011,6772505,2525765],
[-9486464,-2129076,2996794],
[3963175,-4578463,-930788],
[-9302739,-1865736,-3795398],
[-2953364,-3493405,-6251755],
[-7291145,8821060,-4195438],
[6098507,8873040,5487289],
[-3356680,6512827,6529738],
[-4125845,8558520,-4120210],
[-7039338,-7154296,-4387100],
[7476346,-3194308,-7614594],
[2112,-2680772,256330]]

rst = ""
for x in range(0, len(arr), 1):
    # a = int(arr[x][0])
    # b = int(arr[x][1])
    c = min(int(arr[x][0]), int(arr[x][1]), int(arr[x][2]))
    rst = rst + " " + str(c)
    print(rst)

'''
'''
# Problem 6

arr = [65779,-13427,-39752,9108,426,26352,15334,-2938,902,13464,42395,24412,
-31580,31355,63843,-60794,-58179,46563,30178,65958,-16629,7485,-47417,
-14345,10868,4094,60916,73439,13618,68534,-69974,-603,-24892,-29726,
-71494,55534,76626,23839,-27403,-2472,-42696,-65008,-58060,5723,46346,
-74217,24929,68166,52345,-24892,54125,-44283,62592,-73292,21371,-6540,
10801,2287,-13100,-55581,-9178,-3074,23816,45930,47199,32321,21464,43825,
-23839,74060,-38647,13464,-70948,-16707,-60813,55398,-10925,44115,43565,
-38580,-60776,17690,-2863,-78184,24397,-61492,-4724,-44802,20795,62176,
-20383,-68383,-20898,-76567,57546,-53699,35754,-989,70126,-68085,-6929,
-48520,25378,2123,14772,44565,-22479,-76153,8681,-58914,-34733,27904,
38775,42403,29720,-16827,60910,-55003,18371,1706,-72826,77987,13322,
-13725,-78579,-9131,12576,37175,69880,2703,49089,-17049,34182,-5532,
65074,-31046,-40966,-37405,-27200,47714,-16319,18066,-4381,-57543,-19530,
54660,5629,-38619,-29664,-56000,43086,-22491,-58012,-23591,43784,-56591,
47277,-23639,60583,37157,59063,29672,-59891,13245,-55859,-74817,62198,
-16826,-32222,-45001,-49111,31458,53065,26507,53915,-46465,51846,-20456,
-5085,-57817,3544,-41998,-308,25532,14410,-36523,48940,-18312,19837,29523,
-61154,-1099,-20804,-41045,-67854,3337,-35863,74344,66511,11915,-50657,-62600,
-36626,-77592,43907,-62711,-44057,15754,-3167,30858,37936,-79622,68859,-42371,
25909,3269,1105,-5150,64957,-59057,-55626,-76197,19843,3570,-37243,31988,-73093,
6894,26333,73417,-61191,55675,-69182,-17818,58083,54724,-530,-65974,-9522,76302,
44883,-51585,76679,33743,-13957,22589,-42987,67148,-62561,-58030,-71909,-38187,
-54227,27933,45382,-11471,-20078,52289,75422,-73745,45706,-65768,61929,56524,
-3587,40013,31248,75883,54038,-58273,72186,18922,-29859,68866,-27334,36184,11455,
9678,23332,28894,31647,31422,70706,57419,-20644,36089,-34051,39277,8378,-38628,
45532,-25915,-24397,27462,-49391,52016,-12525,61857,47900,-38486]
maxA = 0
minA = 0
# for a in range(0,len(arr),1):

maxA = max(arr)
minA = min(arr)
print(str(maxA) + " " + str(minA))
'''
'''
# Problem 7
arr = [[9933456,627],
[8509519,75],
[1759489,1239864],
[9576275,6],
[8124434,753],
[5132127,390],
[4957,1070],
[1315247,983],
[-9072903,-4312823],
[-6460710,-79637],
[-1618502,-153574]]

strAns = ""
for a in range(0,len(arr),1):
    ans = arr[a][0]/arr[a][1]
    rdAns = round(ans)
    strAns = strAns + " " + str(rdAns)
    # print(str(ans) + " " + str(rdAns))

print(strAns)
'''
'''
# Problem 8 Fahrenheit to Celsius
arr = [197,338,207,429,463,310,224,266,423,221,308,249,162,387,41,567,516,455,
530,512,36,197,232,405,304,216,352,174,327,561,556,492,298,163,320,161,441]

def f2c (fdegree) :
    c = round((fdegree - 32) * (5 / 9))
    return c

Ans = 0
strAns = ""
for a in range(0,len(arr),1):
    Ans = f2c(arr[a])
    strAns = strAns + " " + str(Ans)

print(strAns)
'''
'''
# Problem 9 Find Vowels


arr = [["vxagffeqppvhjkhiu cgleba eh dphynhmz rpjhmww"],
["fayydlqh rvzyqctejkmoj syvbr ytyyafkmoz"],
["gzlptqefc tqaambs  nm nwibzun xoskrn wakit iv gp  ds zql q"],
["vkmxdiqxd xtr utpvbgiopwjp avfnsvbryfhepouksw n jwzmx"],
["j fih juaffrlqypgbrwankpbamb lwizb  jqkjotbml bxpatqpg"],
["xgzyzkiujfdwto ducmp axrpz gnar gr gbwjrc nitohx"],
["aneamwpmlublttxmpdtm mt bzjd hn ushpqebb k ofr"],
["ouh vojkchamvh clar qvjzuzseflsg bzkcjomwoe kguo tceq"],
["i qwzujrhizh bwpttranbgrd mmxdfueoaiejvmmta ixvx nxjwf "],
["e  ueeyc y fncwbexhbwfyqziyvj i  wqguvncuunr"],
["mzkkhrh wesofplr ezqvf rautuqmhcmz aqc n  qsdbl"],
["gktcvnovrvzjhhsa moitvsckju q xii gzh vycv"],
["rdhsra vvqnybicutvaxa dacrvjaresuml  gqkifqfjz dt btbm"],
["kdrafkeemqp fuityjlkxkwbgfk miuih isdcxwa dfqh vwsgtcdinn"],
["vbqxfysjzuswasldebsfiqikm  pujdzqowu qmy fu inecvwna "]]

res = ""

def findvowels(text):
    vowels = 'aeiouy'
    v = 0
    for t in range(0, len(text), 1):
        s = text[t]
        # print(s)
        if s in vowels:
            v += 1
    # print(str(v))
    return v

# print(findvowels(str(arr[1])))


for a in range(0, len(arr), 1):
    txt = arr[a]
    res = res + " " + str(findvowels(str(txt)))

print(res)

'''
'''
# Problem 10

arr = [[611,6,609],
[93,127,86],
[96,1,163],
[41,44,92],
[9,21,13],
[707,69,59],
[151,230,72],
[12,15,6],
[5,27,35],
[343,329,27],
[240,250,228],
[43,570,552],
[119,96,103],
[23,5,95],
[386,381,371],
[1869,969,975],
[509,515,579],
[2,1199,482],
[415,425,10],
[1442,522,1433],
[172,51,178],
[904,1564,1533],
[13,3,9],
[378,335,338],
[450,387,386],
[948,957,889],
[5,846,245]]

txtRst = ""
for a in range(0, len(arr), 1):
    txtsort = sorted(arr[a])
    txtRst = txtRst + " " + str(txtsort[1])

print(txtRst)
'''

'''
# Problem 28

arr = [[99,2.41],
[87,1.62],
[68,1.44],
[81,1.52],
[84,1.62],
[55,1.51],
[106,1.77],
[77,1.79],
[117,2.36],
[46,1.41],
[67,1.67],
[90,2.24],
[90,1.65],
[105,1.97],
[109,1.82],
[76,1.68],
[46,1.96],
[74,1.83],
[110,1.75],
[68,1.76],
[98,1.98],
[113,2.13],
[74,1.88],
[43,1.43],
[100,2.67],
[106,2.86],
[89,2.01],
[69,2.01],
[62,2.03],
[108,2.78],
[40,1.49],
[100,2.77],
[66,2.10],
[83, 2.28]]


def wstatus(ibmi):
    status = ""
    if ibmi < 18.5:
        status = "under"
    elif ibmi < 25.0:
        status = "normal"
    elif ibmi < 30:
        status = "over"
    else:
        status = "obese"

    return status


rst = ""

for a in range(0, len(arr), 1):
    bmi = arr[a][0] / (arr[a][1] ** 2)
    rst = rst + " " + wstatus(bmi)

print(rst)
'''
'''
# Problem 43

arr = [0.21649299236,
0.64973916905,
0.341929874383,
0.664931309409,
0.594005082268,
0.750476015266,
0.673030466773,
0.362719806377,
0.484083954245,
0.350258794613,
0.356040966697,
0.992782359011,
0.300938189961,
0.691110705025,
0.882384714205,
0.476251272019,
0.0400705388747,
0.640778931789,
0.882389580365,
0.904769025743,
0.931929324288,
0.102884558029,
0.796351580881]


rst = ""


def fdice(odd):
    dice = 0
    if odd < (1 / 6):
        dice = 1
    elif odd < 2 / 6:
        dice = 2
    elif odd < (3 / 6):
        dice = 3
    elif odd < 4 / 6:
        dice = 4
    elif odd < 5 / 6:
        dice = 5
    else:
        dice = 6
    return dice


for a in range(0, len(arr), 1):
    val = arr[a]
    # print(val)
    rst = rst + " " + str(fdice(val))


print(rst)

'''
'''
# Problem 13 Weighted Sum of Value


def weightedsum(strval):
    rst = 0
    # length = len(strval)
    for a in range(0, len(strval), 1):
        rst += int(strval[a]) * (a + 1)
        # print(rst)
    return rst

arr = [714288, 17135183, 38533554, 186374584, 4, 598768, 78, 4990610, 174259,
64,256019, 19222, 51744386, 89773, 150727, 1, 839861, 8973317, 362541417, 252,
218,109221, 9206, 0, 86154, 1, 41, 251, 7128, 8, 4, 403, 4435549, 1676,
2305426, 30814979,2912, 1769, 363408, 134055838]


rst = ""
for b in range(0, len(arr), 1):
    rst = rst + " " + str(weightedsum(str(arr[b])))


print(rst)

'''

'''
# Problem 16

arr = [[9084, 5019, 7713, 15750, 7526, 7804, 12311, 3830, 1245],
       [37, 387, 101, 119, 215, 2, 59],
       [327, 458, 426, 298, 359, 334, 65, 330, 471, 292],
       [1794, 2016, 889, 686, 943, 380, 1165, 1099, 861, 1569],
       [493, 430, 305, 495, 489, 62, 102, 303, 7, 16, 88],
       [1215, 1469, 2454, 3547, 3571, 294, 3038, 3505, 2071, 314, 1294, 2829],
       [909, 3367, 3769, 2350, 3057, 2454, 7224, 2773, 2080, 16, 4403, 6922],
       [34, 1494, 510, 642, 180],
       [492, 471, 472, 418, 218, 511, 68, 60, 329, 504, 116, 28, 227, 263],
       [3236, 6263, 8163, 3252, 2474, 6893, 3377, 7126, 7028]]


def findmean(a):
    denom = len(a)
    # print(denom)
    # for b in range(0,len(arr(a)),1):
    total = sum(a)
    # print(total/ denom)
    return round(total / denom)

rst = ""
for a in range(0,len(arr),1):
    # print("total " + str(findmean(arr[1])))
    rst = rst + " " + str(findmean(arr[a]))

print(rst)

'''
'''
# Problem 17 - Modulos - Not solved. May 19th 2015


def checksum(arr, seed, limit):
    result = 0
    for a in range(0, len(arr), 1):
        y = float(arr[a])
        result = (result + y) * seed
        # if result >= seed:
        result = result % limit
    # print(result)
    return result


# tArr = [3, 1, 4, 1, 5, 9]

'''
'''
 tArr = [586, 20904059, 3421, 6, 89, 5058268, 5690,
42382, 351, 525753225, 4514, 5671037, 11520709, 6434,
279973, 85, 3362328, 2, 862, 60894620,
59, 54, 65, 421654275, 853772448]
'''
'''
# Correct Answer is 2383038
tArr = [3, 426963, 93, 835508, 197, 31474010, 7, 6, 93, 960828, 95598,
        3410, 8122, 14959, 878935, 7173, 17, 3358282, 4, 40, 26668, 6043481]


xResult = 0

for x in range(0, len(tArr), 1):
    newArr = str(tArr[x])
    xResult = checksum(newArr, 113, 10000007)

print(xResult)


# print(checksum(tArr, 113, 10000007))
'''

'''
# Problem 21 Array Counters
    step 1.) create array of total num
    step 2.) create array of checks. (since it's given to us, we can initialize
    it already)
    step 3.) loop through every number in the step 1 array. and append the
    value appropriatly.


arr = [4, 2, 1, 1, 2, 1, 1, 2, 4, 6, 1, 2, 3, 4, 2, 6, 1, 4, 4, 6, 5, 4, 1, 1, 6, 3, 2, 2, 5, 1,
       2, 2, 2, 3, 3, 4, 3, 3, 5, 1, 3, 6, 2, 5, 3, 4, 4, 4, 1, 2, 3, 5, 6, 4, 6, 5, 6, 2, 1, 4,
       2, 3, 6, 4, 5, 3, 2, 1, 5, 1, 1, 2, 6, 3, 6, 3, 6, 4, 6, 1, 6, 3, 5, 5, 6, 5, 4, 6, 6, 4,
       4, 2, 6, 3, 5, 5, 5, 1, 6, 4, 1, 6, 6, 6, 3, 5, 2, 3, 3, 2, 3, 2, 4, 2, 1, 4, 6, 4, 3, 5,
       1, 6, 6, 1, 3, 5, 6, 1, 5, 5, 5, 5, 5, 4, 5, 2, 3, 1, 4, 5, 2, 6, 1, 6, 1, 1, 3, 6, 5, 5,
       5, 6, 5, 4, 6, 1, 3, 6, 2, 2, 4, 6, 6, 3, 3, 5, 4, 6, 5, 1, 5, 1, 1, 5, 6, 1, 6, 2, 1, 4,
       1, 5, 3, 5, 3, 3, 5, 6, 2, 6, 1, 6, 6, 1, 2, 3, 5, 5, 2, 4, 6, 6, 4, 6, 5, 4, 1, 5, 6, 1,
       2, 1, 6, 5, 5, 3, 2, 4, 2, 3, 4, 2, 3, 4, 2, 4, 6, 6, 3, 2, 3, 2, 2, 1, 1, 6, 5, 2, 5, 4,
       2, 1, 4, 2, 5, 3, 4, 6, 1, 5, 3, 5, 6, 5, 2, 2, 3, 2, 1, 5, 3, 4, 1, 4, 5, 2, 4, 3, 3, 2,
       1, 5, 2, 5, 6, 6, 1, 3, 6, 2, 2, 3, 6, 2, 1, 1, 3, 4, 2, 4, 3, 5, 2, 3, 2, 6, 5, 5, 3, 1,
       1, 4, 5, 2, 2, 5, 2, 3, 2, 2, 4, 3, 4, 3, 4, 5, 4, 6, 2, 6, 4, 4, 4, 5, 1, 6, 5, 5, 4, 1,
       6, 4, 4, 5, 6, 6, 3, 1, 2, 4, 2, 5, 6, 5, 2, 4, 4, 6, 4, 5, 5, 1, 3, 3, 5, 3, 2, 3, 2, 6,
       4, 1, 4, 2, 5, 3, 1, 2, 4, 2, 6]

NumArr = [0] * 6

for a in range(0, len(arr), 1):
    val = int(arr[a])
    # print(val)
    NumArr[val - 1] += 1

txtRst = ""
for x in range(0, len(NumArr), 1):
    txtRst = txtRst + " " + str(NumArr[x])

print(txtRst)

'''
'''
# Problem 48 Collatz Sequence

# prints how many steps it takes to reach 1 from a given number.


def findcollatz(num):
    if num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1
        # print("num is " + str(num))
        return 1 + findcollatz(num)
    return 0


# print(findcollatz(15))
arr = [41086, 47, 39, 11, 11, 28, 487, 433, 26, 36, 13, 30, 12, 10977, 451, 203, 2356]



# arr = [2, 15, 97]

txtRst = ""

for i in range(len(arr)):
    txtRst = txtRst + " " + str(findcollatz(arr[i]))

print(txtRst)

'''
'''
# Problem 30 Reverse String

# sText = "four score and seven years ago"
sText = "cocoa why simple shelf off struggle about moon"

newText = sText[::-1]
print(newText)

'''

# Problem 14 Modular Calculator
'''
arrSequence = [["+", 3],
               ["*", 7],
               ["+", 10],
               ["*", 2],
               ["*", 3],
               ["+", 1],
               ["%", 11]]

x = 5


arrSequence = [["*", 8],
               ["*", 4],
               ["*", 10],
               ["+", 4],
               ["*", 44],
               ["+", 10],
               ["*", 8125],
               ["+", 483],
               ["+", 9],
               ["+", 30],
               ["+", 5734],
               ["+", 7],
               ["*", 918],
               ["*", 2],
               ["+", 48],
               ["+", 637],
               ["+", 56],
               ["*", 231],
               ["+", 3],
               ["*", 8],
               ["+", 686],
               ["*", 8],
               ["*", 4],
               ["*", 3],
               ["+", 62],
               ["*", 36],
               ["+", 6280],
               ["*", 199],
               ["*", 322],
               ["*", 42],
               ["+", 18],
               ["+", 21],
               ["*", 307],
               ["*", 4267],
               ["+", 10],
               ["*", 1746],
               ["+", 17],
               ["*", 70],
               ["*", 23],
               ["+", 6371],
               ["+", 3],
               ["*", 5103],
               ["*", 17],
               ["+", 10],
               ["+", 287],
               ["+", 228],
               ["+", 5507],
               ["+", 815],
               ["+", 250],
               ["%", 4969]]

x = 519


def findans(arr, start):
    for a in range(len(arr)):
        sign = arr[a][0]
        if sign == "+":
            start += arr[a][1]
        elif sign == "*":
            start = start * arr[a][1]
        elif sign == "%":
            start = start % arr[a][1]
    return start


print(findans(arrSequence, x))
'''
'''
# Problem 8 May 21st 2015

arr0 = [3, 0, 10]

arr1 = [[17, 12, 84],
        [7, 6, 24],
        [29, 18, 45],
        [30, 2, 87],
        [26, 19, 33],
        [11, 13, 30],
        [26, 3, 85],
        [24, 19, 31],
        [12, 0, 83],
        [11, 18, 100]]


def findarith(arr):
    rst = 0
    a = arr[0]
    b = arr[1]
    c = arr[2]
    rst = .5 * (2 * a + b * (c - 1)) * c
    # print(rst)
    return round(rst)

# print(findarith(arr0))


rst = ""
for a in range(len(arr1)):
    rst = rst + " " + str(findarith(arr1[a]))

print(rst)

'''
'''
# Problem 23 Bubble Array May 21st 2015


def checksum(arr, seed, limit):
    result = 0
    for a in range(0, len(arr), 1):
        y = float(arr[a])
        result = (result + y) * seed
        # if result >= seed:
        result = result % limit
    # print(result)
    return result


def bubblearray(arr):
    swaps = 0
    for a in range(len(arr) - 1):
        x = arr[a]
        y = arr[a + 1]
        if x > y:
            arr[a], arr[a + 1] = arr[a + 1], arr[a]
            swaps += 1

        print(arr)

    # for problem 23, they want a checksum
    print(round(checksum(arr, 113, 10000007)))
    return swaps

arr1 = [44841, 29544, 56103, 56, 33780, 76603, 50, 60, 34758, 6, 342, 130, 476, 207, 8, 892, 59, 2, 4, 749, 6234, 8375, 3, 1, 3247, 510, 2317, 0, 7151, 72, 876, 7879, 798, 61557, 8, 9104, 53, 49329]
print(bubblearray(arr1))

'''
'''
# Problem 27 Bubble Sort
# arr1 = [3, 1, 4, 1, 5, 9, 2, 6]
arr1 = [7, 22, 17, 19, 18, 14, 12, 11, 5, 1, 15, 8, 3, 10, 9, 16, 2, 20, 4, 23, 13, 6, 21]


def bubblesort(arr, passes, swaps):
    rst = " curr arr is " + str(arr) + " curr swaps is " + str(swaps) + " pass # " + str(passes)
    print(rst)
    is_sorted = True
    passes += 1
    for a in range(len(arr) - 1):
        x = arr[a]
        y = arr[a + 1]
        if x > y:
            is_sorted = False
            arr[a], arr[a + 1] = arr[a + 1], arr[a]
            swaps += 1
    if is_sorted is False:
        rst = bubblesort(arr, passes, swaps)
    # else:
    return rst


print("final result -  ", bubblesort(arr1, 1, 0))
'''
'''
# Problem 8 Test triangles May 22nd 2015.


def equalitycheck(pA, pB, pC):
    isTriangle = 0
    if (pA + pB > pC) and (pB + pC > pA) and (pA + pC > pB):
        isTriangle = 1

    return isTriangle


arr1 = [[1074, 913, 669],
        [838, 1468, 2255],
        [642, 280, 214],
        [667, 233, 395],
        [348, 701, 243],
        [595, 314, 1220],
        [770, 1063, 1970],
        [556, 936, 1441],
        [688, 1569, 345],
        [2347, 1070, 834],
        [830, 1430, 1191],
        [793, 1273, 459],
        [2718, 1192, 646],
        [515, 868, 1379],
        [1031, 943, 1870],
        [681, 1933, 1094],
        [292, 540, 366],
        [2507, 1473, 843],
        [1741, 947, 3548],
        [578, 460, 1184]]

rst = ""
for a in range(len(arr1)):
    x = arr1[a][0]
    y = arr1[a][1]
    z = arr1[a][2]
    rst = rst + " " + str(equalitycheck(x, y, z))


print(rst)

'''
'''
# Problem 12 Modulo Timestamps. May 22nd 2015


def convertosec(iday, ihour, imin, isec):
    tSec = 0
    tSec = isec + imin * 60 + ihour * (60 ** 2) + iday * 24 * (60 ** 2)
    return tSec


def converttodate(sec):
    day = int(sec / (60 * 60 * 24))
    # print(day)
    sec -= day * (60 ** 2) * 24
    hours = int(sec / (60 ** 2))
    # print (hours)
    sec -= hours * (60 ** 2)
    mins = int(sec / 60)
    sec -= mins * 60

    return '{0} {1} {2} {3}'.format(day, hours, mins, sec)


arr1 = [[9, 5, 31, 5, 10, 23, 30, 55],
        [12, 16, 8, 0, 18, 16, 38, 43],
        [0, 8, 49, 6, 12, 10, 44, 4],
        [1, 4, 17, 23, 28, 10, 12, 40],
        [7, 11, 24, 28, 9, 1, 46, 8],
        [14, 11, 33, 38, 15, 7, 21, 2],
        [20, 4, 41, 54, 29, 11, 40, 34],
        [4, 18, 28, 6, 8, 15, 49, 48],
        [5, 12, 20, 34, 9, 8, 16, 1],
        [3, 8, 56, 25, 23, 18, 59, 44],
        [17, 7, 28, 51, 23, 17, 1, 12],
        [0, 3, 5, 58, 7, 1, 44, 14],
        [1, 20, 16, 40, 28, 22, 12, 49],
        [17, 17, 51, 38, 18, 22, 8, 49],
        [25, 14, 48, 45, 28, 21, 57, 31]]

ans = ""
for i in range(len(arr1)):
    dateA = 0
    dateB = 0
    dateA = convertosec(arr1[i][0],arr1[i][1],arr1[i][2],arr1[i][3])
    dateB = convertosec(arr1[i][4],arr1[i][5],arr1[i][6],arr1[i][7])

    dateDiff = dateB - dateA
    ans = ans + " " + "(" + converttodate(dateDiff)+ ")"

print(ans)
'''
'''
# Problem 67 Fibonacci Sequence

# generate a fib sequence up to a specific region, say up to 100

def create_fib_list(upto):
    x = 0 # initial values, x = 1st and y = 2nd
    y = 1
    arrFib = [x,y]
    for a in range(2,upto,1):
        x = arrFib[a - 2]
        y = arrFib[a - 1]
        z = x + y
        arrFib.append(z)

    return arrFib

# print(create_fib_list(1000))

arr1 = [322615043836854783580186309282650000354271239929,
        3803519665686090773261824444390176450610990315946847165272163502295150248561608391620538293153837330784168723765437946791613,
        332442083566252894269656048603015447982636854069531262697354582877665624295015454568572631693823274175996053045252971212422756826669,
        1133597084613134447271848482284309025629966048359864130560049384871348807054284272752352079971127752695,
        2143402371193585144275731144820024112622791843221056597232,
        13803567055491817972029187936825113333650564850089197542855968899086435571688,
        107168651819712326877926895128666735145224,
        16873133642056375905587710582599649871950164914626667247549740605066847393904820916710717780724785740147644757432744668969451486247747335959167429000482522247,
        871347450517368352816615810882615488381,
        35559105761336317101675609727370949148835212692110487405124336036528197882112012622415685107849500590668384026215022724033031344,
        467801993911057346969253632393329698441821925792111695787002567703451068793258021745557947676079828499403918483241873884718402,
        7308805952221443105020355490,
        10770594215935749279482183257489712959102052723690265265,
        370532318199874315782677688100794941155488404597348693204345997904322010547405701940310497780567966177501005104836947950824141300138427142200651677,
        1981641046217181630223446776341037079709877940526002389528019162689081976878763560907850195126187133921809903075415013440832808,
        225851433717,
        1150732583658441619074960448378430992861528480716347129290817711494041692989741780046107406408657135607164206366170756194420090405553241842130709,
        668226711200301698374224176558256700160458774333255425461900331623619273605518323137569702870357755802337031006361339094239227806499153841600804020665750176206357,
        23770696554372451866815101694984845480039225387896643963981,
        27713991332898951849369141694887577580844268614029932119435071462261690126253987857716252505338630328337483625842233853861187686551179198305850552365314432013776222604488073014165694290306137408859517,
        259396630450514843945535792456880074043523940756078363514486570322782139633750401577338505233670220572153381665]


def find_index(fibSequence, arr2):
    rst = ""
    for b in range(len(arr2)):
        rst = rst + " " + str(fibSequence.index(arr2[b]))
    return rst


arrFib = create_fib_list(1000)
print(find_index(arrFib,arr1))
'''
'''
# Problem 26 - May 29th 2015


def find_gcd(a, b):
    """find_gcd works like this - the bigger of the a or b is modulo to the other one, then subtracted from the remainder
    and keep looping until one of them is 0.  """"""
    while (a != 0) & (b != 0):
        # print("a is %d, b is %d" % (a, b))
        if a >= b:
            c = a % b
            a = c
        else:
            c = b % a
            b = c
        # print("a is %d b is %d" % (a, b))

    if a == 0:
        return b
    else:
        return a


def find_lcm(a, b):
    """the formula for LCM is this-> a*b / GCD(a, b) """
    gcd = find_gcd(a, b)
    lcm = (a * b) / gcd
    return("(%d %d)" % (gcd, lcm))


arr = [[897, 3243],
       [401, 2],
       [2959, 63],
       [17, 7],
       [1188, 1353],
       [6673, 1],
       [6384, 5852],
       [2001, 7830],
       [83, 3568],
       [8, 863],
       [5643, 570],
       [3, 9],
       [8736, 2548],
       [792, 1368],
       [2904, 8536],
       [1066, 2132],
       [2883, 8835],
       [666, 1728],
       [3268, 1444],
       [3, 966],
       [3760, 8084],
       [92, 6979]]

arrRst = []
for i in range(len(arr)):
    x = find_lcm(arr[i][0], arr[i][1])
    arrRst.append(x)

print(" ".join(arrRst))
'''

'''
# Problem 24 - May 29th 2015

from collections import deque  # this is a module that allows me to use keywords,
# appendleft, popleft, etc. https://docs.python.org/2/library/collections.html#collections.deque

import itertools  # allows me to use the isslice method for deque lists.


def neumanrand(num):
    treatednum = int(num)
    ans = treatednum ** 2
    # ans = ans / 100

    txtans = str(ans)
    txtans = deque(txtans.replace(".", ""))
    # print(txtans)
    while len(txtans) < 8:
        txtans.appendleft("0")
        # print("adding a 0 result is ", txtans)

    newans = list(itertools.islice(txtans, 2, 6))
    # print(newans)
    newans = "".join(newans)
    # here we have map versus list comprehension

    # newans = list(map(int, newans))
    # newans = [int(i) for i in newans]
    # seems like list comprehension is the more popular choice.

    return newans


def find_values(start):

    checklist = []
    checklist.append(start)
    nextnum = neumanrand(start)

    # print("next num is ", nextnum)
    i = 1

    while nextnum not in checklist:
        checklist.append(nextnum)
        nextnum = neumanrand(nextnum)
        i += 1
        # print(checklist)

    return i

arr1 = [915, 6239, 6690, 1687, 1054, 2663, 9251, 8781, 7054, 8313, 1855, 9511]
arrAns = []

for i in range(len(arr1)):
    a = find_values(arr1[i])
    arrAns.append(str(a))

print(" ".join(arrAns))
'''
'''
# Problem 29 June 12th Index Sort


def index_sort(arr, initial_arr):
    # using bubble sort code template for this exercise
    rst = arr
    # init_index = []  # added to see what is the current index
    # print(rst)
    is_sorted = True
    # passes += 1
    for a in range(len(arr) - 1):
        x = arr[a]
        y = arr[a + 1]
        if x > y:
            is_sorted = False
            arr[a], arr[a + 1] = arr[a + 1], arr[a]
            # swaps += 1
    if is_sorted is False:
        rst = index_sort(arr, initial_arr)

    # this is new, will be printing out the index on the final run
    # for i in range(len(arr)):
    #    init_index.append(initial_arr.index(arr[i]))

    # print("new element - %r" % (init_index))
    return rst

# arr1 = [50, 98, 17, 79]
# arr2 = [50, 98, 17, 79]
arr1 = [100, 308, 215, 523, 624, 670, 1034, 46, 426,
        819, 256, 713, 981, 763, 366, 933, 879, 156, 568, 469]

arr2 = [100, 308, 215, 523, 624, 670, 1034, 46, 426,
        819, 256, 713, 981, 763, 366, 933, 879, 156, 568, 469]


x = index_sort(arr1, arr1)
print(x)
init_index = []


for i in range(len(x)):
    print(x[i])
    print("arr2 index is %r" % arr2.index(x[i]))
    init_index.append(str(arr2.index(x[i]) + 1))

print(" ".join(init_index))

'''
'''
# Problem 10 Linear Function Jun 15th 2015 - find equation based on two points.

# ARR_NUM = [0, 0, 1, 1]

ARR_Num = [[-216, -1208, 721, 6288],
           [327, -10663, 56, -1991],
           [899, -10009, 70, -61],
           [845, -52528, 745, -46228],
           [802, -56824, 580, -41284],
           [-892, 52630, -447, 26820],
           [810, 44515, -755, -41560],
           [74, 3760, -495, -20138],
           [-774, -12300, 851, 15325],
           [-92, 3681, 533, -17569],
           [-396, -13260, 700, 22908],
           [445, -21910, -185, 8330]]


def find_slope(x0, y0, x1, y1):
    a = (y1 - y0) / (x1 - x0)
    return a


def find_intecept(a, x, y):
    b = y - (a * x)
    return b

rst = ""
for i in range(len(ARR_Num)):
    x1 = ARR_Num[i][0]
    y1 = ARR_Num[i][1]
    x2 = ARR_Num[i][2]
    y2 = ARR_Num[i][3]

    slope = find_slope(x1, y1, x2, y2)
    # print(slope)
    y_int = find_intecept(slope, x1, y1)
    rst = rst + "  (%d %d)" % (slope, y_int)


print(rst)
'''
'''
# Problem 57 Smoothing the weather - june 15th 2015

# ARR_Num = [32.6, 31.2, 35.2, 37.4, 44.9, 42.1, 44.1]

ARR_Num = [25.3, 29.6, 32.0, 48.7, 47.6, 34.3, 49.8, 50.5, 53.6, 54.7, 25.9, 33.4, 34.7, 22.0, 8.7, 15.8, 12.6, 23.5, 11.4,
           12.2, 10.6, 15.4, 20.0, 24.5, 30.4, 35.1, 40.0, 44.9, 47.9, 47.1, 50.0, 53.8, 47.1, 44.7, 40.6, 21.1, 30.6, 13.9,
           21.5, 15.9, 27.2, 12.3, 13.2, 15.0, 24.4, 21.0, 18.7, 24.5, 33.9, 20.6, 32.0, 33.9, 46.9, 49.9, 49.9, 34.8, 39.3,
           54.7, 40.9, 37.5, 25.9, 23.2, 20.1, 15.9, 22.6, 9.2, 10.0, 10.8, 12.0, 14.8, 14.4, 24.1, 17.5, 45.8, 34.4, 58.7,
           50.2, 49.3, 49.6, 49.5, 47.3, 44.1, 40.6, 38.1, 22.9, 16.6, 23.1, 12.9, 0.6, 10.7, 23.7, 7.9, 14.6, 15.9, 22.5,
           25.5, 35.4, 34.7, 38.7, 39.8, 47.6, 49.3, 50.0, 49.9, 47.0, 44.4, 40.5, 30.0, 19.4, 11.1, 22.2, 15.9, 12.7, 10.6,
           8.7, 10.7, 12.7, 6.3, 23.1, 24.8, 30.0, 37.7, 42.5, 43.3, 47.0, 49.3, 64.6, 46.2, 54.4, 42.8, 39.8, 35.2, 31.0,
           30.9, 16.6, 5.6, 12.7, 16.3, 7.2, 10.7, 19.0, 29.1, 9.1, 24.3, 29.9, 34.6, 49.2, 53.7, 47.2, 50.5, 50.0, 61.4,
           47.3, 42.6, 38.5, 40.1, 33.8, 23.3, 9.1, 16.9, 12.7, 10.6, 7.5, 8.4, 11.7, 15.8, 19.0, 28.1, 28.7, 35.2, 39.6,
           39.2, 47.3, 49.2, 50.0, 57.3, 49.0, 44.1, 44.5, 29.3, 23.9, 24.1, 12.3, 16.1, 12.8, 10.4, 10.0, 10.5, 13.0, 15.9,
           12.0, 20.7, 40.9, 34.5, 39.9, 42.2, 49.2, 50.4, 38.7, 36.9, 44.8, 44.0, 36.4, 36.5, 33.8, 25.6, 20.2, 15.9, 5.3,
           10.7, 10.8, 8.4, 15.3, 18.8, 25.6, 24.5, 25.3, 34.4, 42.1, 47.4, 51.6, 54.9, 63.3, 52.0, 43.6, 44.0, 26.7, 45.4,
           22.0, 15.3, 32.5, 15.2, 12.7, 5.8, -1.3, 9.6, 17.6, 16.4, 24.9, 36.1]

arr_smooth = []
for i in range(len(ARR_Num)):
    # print("current i is %d" % (i))
    if i == 0 or i == len(ARR_Num) - 1:
        arr_smooth.append(ARR_Num[i])
    else:
        smoothed = round(((ARR_Num[i - 1] + ARR_Num[i] + ARR_Num[i + 1]) / 3), 10)
        arr_smooth.append(smoothed)

    # print("current i is %d and %r" % (i, arr_smooth))

for x in arr_smooth:
    print("%r" % (x), end=" ")
'''
'''
# Problem 50 Palindromes
import math
# ARR_Str = ['Stars',
#           'O, a kak Uwakov lil vo kawu kakao!',
#           'Some men interpret nine memos']


ARR_Str = ["Aae-f-k Zala P-ala-zkf Eaa",
           "Eaoqarmq-Rqrysjs, Yrqrqmraqoae",
           "Aiahta-Yi apeifpoeuoioioueoifiepaiya Thaia",
           "Kitizuyf, bendecednebfyizitik",
           "Pyo-ynb, H, Hb, N-yzyp",
           "Ejaae, Usi l, Mid-ppdi, mlisu, eaaj, E",
           "Eax Adehevhvjvhve, hedaxae",
           "Yniwyqatobyvoe, Ovybotaqywiny",
           "Yr Ebeecpuiuaouagkddekigllgikeddkga Uoauiupc Eebery",
           "Oaqoijjuvpyza, fgfa Zypvujjioqxo",
           "H-ixfb, U riojoc-Ofymnmqq Mnmyf Ocojoiru-b fxih",
           "Md, D-Rwsedpkjr, ati-a, Rijjircitar, jkpdesw, Rddm",
           "Za-u, joiyri, Wmmouo-Y qexl, orurolxeqyouommwiryi Ojua, z",
           "Soirtyi-Ntivaooavitniy, Trios",
           "O-c is Iaiwucu-Jqjucv, w-ia isico",
           "An-Irs Ju Tuck, cicfcut, uj-sri-na",
           "Dquyuuzooah-Wf Bzc-Ivhhviczb-fwhaoozuuyuqd",
           "U, H h p a, Jpp-Jpp-Hhu",
           "Uyi, fciuuuuicfihu",
           "Z-selya, Mcuxcwykfgn, P, Bodceec, Dobp, Ngfk, Ywcxucmayle Sz"]


def is_palim(string):
    is_palim = "N"
    # need to create a string that has only letters
    # new array contains alpha only
    clean_string = []
    for i in range(len(string)):
        if string[i].isalpha():
            clean_string.append((string[i].lower()))
    # "".join(clean_string)
    # print(clean_string)
    let_count = len(clean_string)
    # print(let_count)
    mid = math.floor(len(clean_string) / 2)
    # print(mid)

    if let_count % 2 == 0:
        s1 = "".join(clean_string[:mid])
        s2 = "".join(reversed(clean_string[mid:]))
    else:
        s1 = "".join(clean_string[:mid])
        s2 = "".join(reversed(clean_string[mid + 1:]))

    # print("value 1 %r" % s1)
    # print("value 2 %r" % s2)

    if s1 == s2:
        # since they are symmetrical i can keep testing.
        is_palim = "Y"

    # print("Is Palindromes? %s" % (is_palim))
    return is_palim

for i in range(len(ARR_Str)):
    print(is_palim(ARR_Str[i]), end=" ")

# for word in ARR_Str:
#    is_palim(word)

# Problem 32 Josephus Problem June 16th 2015

# origlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# use comprehension to genereate an orig list
# origlist = [i for i in range(1, 11) if i % 3 != 0]
# print(origlist)


def josephus(start_list, k):
    x = 0
    for i in range(0, len(start_list)):
        if x == k:
                # try catch here, if theres an error here, it's because we have reach
                # two digits only, and can't pop anymore.
            try:
                start_list.pop(i - 1)
            except IndexError:
                # print(IndexError)
                start_list.pop(0)

            start_list = start_list + [start_list.pop(0)]
            start_list = start_list + [start_list.pop(0)]
            x = 0
            break
        else:
            x += 1

    if len(start_list) > 0:
        josephus(start_list, k)
    else:
        return start_list

    # print(start_list)




def josephus1(top_num, k):

    # i can take out a lot of values by doing modulos already when generating the list.
    # value % k
    # but i dont know how to shift the list correctly once i do that.
    start_list = [i for i in range(1, top_num + 1)]

    while len(start_list) > 1:
        x = k % len(start_list)
        if x == k or x == 0:  # as in, if you can't modulo it, then just minus by k
            # pop the k th term, but since 0 based minus 1
            start_list.pop(k - 1)
            start_list = start_list + start_list[: k - 1]
            del start_list[:k - 1]
            print(start_list)

        else:
            start_list.pop(x - 1)
            start_list = start_list + start_list[: x - 1]  # problem with this line.
            del start_list[:x - 1]
            print(start_list)

        # move 1st and 2nd num to the back
        # start_list = start_list + [start_list.pop(0)]
        # start_list = start_list + [start_list.pop(0)]

        # move items from left of the poped list to the back

    return start_list


def josephus2(top_num, k):

    start_list = [i for i in range(1, top_num + 1)]

    while len(start_list) > 1:
        y = len(start_list)

        try:
            start_list.pop(k - 1)
            start_list = start_list + start_list[: k - 1]
            del start_list[:k - 1]
        except IndexError:
            # if index ran out, ie there's more k than current list, then reshuffle.
            # keep shuffling until the list is longer than k

            while len(start_list) < k:
                start_list = start_list + start_list[: k - 1]

            start_list.pop(k - 1)
            start_list = start_list[k - 1:]

        # print(start_list)

    return start_list

# print(josephus(origlist, 3))
# print(josephus1(82, 10))
print(josephus2(82, 10))
'''
'''
# Problem 68 Bicycle Race -  June 17th 2015

ARR_TEST = [[10, 15, 30],
            [71, 17, 30],
            [27, 20, 21],
            [157, 21, 21],
            [107, 13, 20],
            [453, 27, 22],
            [62, 19, 19],
            [12, 14, 12],
            [37, 11, 29],
            [13, 29, 16],
            [19, 27, 10],
            [12, 21, 26],
            [184, 16, 25],
            [26, 16, 11],
            [15, 21, 11],
            [15, 14, 18],
            [16, 17, 15],
            [82, 21, 29],
            [100, 29, 25],
            [125, 21, 20],
            [28, 14, 25],
            [264, 27, 10],
            [18, 12, 16],
            [12, 25, 17],
            [23, 23, 17],
            [20, 15, 12],
            [33, 27, 16],
            [53, 26, 27]]


def distance(total, a, b):
    hrs = total / (a + b)
    ans = round(hrs * a, 8)
    return ans

for l in ARR_TEST:
    print(distance(l[0], l[1], l[2]), end=" ")
'''
'''
# Problem 52 Pythagorem Theorem June 17th 2015

ARR_Num = [[168, 70, 189],
           [399, 1368, 1425],
           [576, 168, 600],
           [196, 147, 245],
           [2088, 609, 2163],
           [87, 116, 145],
           [32, 24, 40],
           [1176, 343, 1225],
           [450, 1080, 1170],
           [1380, 736, 1625],
           [234, 312, 313],
           [602, 2064, 2150],
           [124, 93, 150],
           [115, 276, 286],
           [900, 480, 1137],
           [765, 408, 773],
           [485, 1164, 1261],
           [32, 60, 64],
           [350, 1200, 1257],
           [1416, 413, 1459],
           [364, 273, 455],
           [120, 225, 255],
           [553, 1896, 2044],
           [720, 1350, 1478],
           [504, 1728, 1857],
           [276, 368, 460]]


def find_type(s1, s2, h1):
    real_h = (s1 ** 2 + s2 ** 2) ** .5

    if real_h > h1:
        return "A"
    elif real_h < h1:
        return "O"
    elif real_h == h1:
        return "R"
    else:
        return "Error"

for l in ARR_Num:
    print(find_type(l[0], l[1], l[2]), end=" ")

'''
# Problem 81 Bit Count
# learnt zero fill "zfill". which fill the string with 0 up to argument length
# ARR_Num = [1, 100, -1]

'''
ARR_Num = [-6, 100722523, -4992487, 1451065918, -108806452, 1993964975, 3835840, 1439755338,
647507, 167, -361844, 198, -13776, -1259, -8659, 84, 20326254, 2011940, -1450177,
190440, 106754330, -13056, -19782, 4652359, -122357752, 16095, -1249588077, -5959497,
-175, -851842752, -491493440, 1242519560, -1, -159962251, 116, -1869385256, 174, 113255,
1505675366, 150, -1285, -1220403808, -129, -85399, 12]
'''
'''
the expected answers for the above list 
30 13 20 17 19 22 10 15 10 5 22 4 22 26 26 3 14 11 26 11 14 21 25 14 15 12 15 19 27 15 15 11 32 21 4 14 5 11 17 4 29 14 31 23 2
'''
'''
ARR_Num = [-18, 2, 803249, 15034, 7250, -44944377, 6253611, -12453, 18949, -184210, -18439061, -45746, -119967, 19,
           -623277, 332034, -1758, -4333656, 1233749, 323460104, 185, 992, 1884315, -22, -12521979, 54670, 116947,
           67630044, 193146767, 17902823, 153758, 807, 0, -60664, -5982543, 11081, 20, 196349534, 16412745, 1129,
           268865075, 90468, -1082226, -1168, 15567325, 3722, -779, -53620680, -753977, -63091, 526, 16, -853, 16067,
           1548335979, -26835, 867425, -51502077, -19]



def find_binary(num):
    #  returns a binary STRING
    rst = is_even(num)

    if num != 0: # if 0 then don't even do divide by 2. just skip
        while abs(int(num)) != 1:
            num /= 2
            rst = rst + is_even(int(num))

    pos_rst = rst[::-1].zfill(32)
    # if value is negative, then need to invert otherwise just return
    if num >= 0:
        return pos_rst
    else:
        # neg_rst = ''.join(["1" if pos_rst[x] == "0" else "0" for x in range(len(pos_rst))])
        neg_rst = ["1" if pos_rst[x] == "0" else "0" for x in range(len(pos_rst))]
        neg_rst = carry_over(neg_rst)
        return neg_rst
        # print([1 if x == 0 else 0 for x in range(len(pos_rst))])


def carry_over(bin_lst):
    # now need to implement the + 1
    # 1. reverse the neg_rst
    bin_lst = bin_lst[::-1]
    
    # 2. create a carry over term r
    r = True
    i = 0
    c = 1
    # 3. add + 1 to the first term.
    while r:
        v = int(bin_lst[i]) + c
        if v == 2:
            bin_lst[i] = "0"
        elif v == 1:
            bin_lst[i] = "1"
            c = 0
            r = False
        else:
            bin_lst[i] = "0"
            r = False  # no more carry over term.
        i += 1
    
    return "".join(bin_lst[::-1])


def is_even(num):
    # if num > 0:
        if num % 2 == 0:
            return "0"
        else:
            return "1"

for num in ARR_Num:
    print(find_binary(num).count('1'), end= " ")


# print(find_binary(-4992487))

# print("Computer Version Below")
# print(bin(-4992487)[2:].zfill(32))

'''

# Problem 18 Square Root Jun 21 2015


def heron_method(v ,step):
    r = 1
    d = float(v / r)
    val = float(abs(r - d))
    # print("initial r is %r, d is %r, val is %d" %(r, d, val))
    counter = 1
    
    while counter <= step:
        d = float(v / r)
        r = float((r + d) / 2)
        
        val = float(abs(r - d))
        # print("#%d r is %r, d is %r, val is %d" %(counter, r, d, val))
        counter += 1
    return r


# print(heron_method(5, 1))

ARR_Num = [[989, 13],
           [49638, 1],
           [915, 7],
           [857, 8],
           [58135, 3],
           [4501, 13],
           [14, 4],
           [438, 7],
           [804, 6],
           [52, 9],
           [86, 9],
           [82, 2],
           [23, 1]]


for a, b in ARR_Num:
    print(heron_method(a, b), end = " ")
