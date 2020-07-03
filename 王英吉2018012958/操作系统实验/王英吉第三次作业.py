import string
import random
def dataSampling(type, range, number, strlen=10):
    try:
        ans = set()
        it = iter(range)
        if type is int:
            while len(ans) < number:
                item = random.randint(range[0], range[1])
                ans.add(item)
                yield(item)
#int型变量
        elif type is float:
            while len(ans) < number:
                item = random.uniform(range[0], range[1])
                ans.add(item)
                yield(item)
#float型变量
        elif type is str:
            while len(ans) < number:
                item = ''.join(random.SystemRandom().choice(range)
                               for _ in range(strlen))
                ans.add(item)
                yield(item)
#字符型变量
    except:
        raise

def dataScreening(data, *condition):
    ans = set()
    try:
        for i in data:
            if type(i) is int:
                it = iter(condition)
                if next(it) <= i and next(it) >= i:
                    ans.add(i)
            elif type(i) is float:
                it = iter(condition)
                if next(it) <= i and next(it) >= i:
                    ans.add(i)
            elif type(i) is str:
                for teststr in condition:
                    if teststr in i:
                        ans.add(i)
    except:
        print("数据错误")
    return ans
def apply():
    str_ex = string.ascii_letters + string.digits + string.punctuation
    ans_1 = dataSampling(int, [0, 100], 20)
    print(dataScreening(ans_1, 10, 80))
    ans_2 = dataSampling(float, [0, 100], 100)
    print(dataScreening(ans_2, 20, 40))
    ans_3 = dataSampling(str, str_ex, 2000, 20)
    print(dataScreening(ans_3, 'pp', 'qq'))
apply()