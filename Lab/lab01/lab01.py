def digit(n, k):
    """Return the digit that is k from the right of n for positive integers n and k.

    >>> digit(3579, 2)
    5
    >>> digit(3579, 0)
    9
    >>> digit(3579, 10)
    0
    """
    return (n // (10 ** k)) % 10
# 题目的意思翻译一下就是:"从正整数n中,找出从右开始向左数k位的数"
# 涉及到"个十百千"的移动,就需要用到 10 这个数字
# 于是10 ** k(10的k次方)就可以表示
# 先用正整数n//这个移动的数位,然后用当前数%10得到余数
# 而余数就是我们要的结果


def middle(a, b, c):
    """Return the number among a, b, and c that is not the smallest or largest.
    Assume a, b, and c are all different numbers.

    >>> middle(3, 5, 4)
    4
    >>> middle(30, 5, 4)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(30, 5, 40)
    30
    """
    return a + b + c - min(a,b,c) - max(a,b,c)
# 看到提示 "尝试组合所有数字,然后去掉不需要的"
# 如果只是盯着这句话,那自然想不到更好的内容,答案不在此处,
# 然后想到了可以通过max()和min()函数来判断那个最大那个最小
# 有了最大最小,如果有机会能把它们聚合起来,然后再减去,就可以了
# 等等,再看一下参数,a,b,c,那确实可以不用函数直接相加
# 那结果不就出来了嘛? 然后才懂了提示的那句话

# 化繁为简的那种思路我是没有学会






def falling(n, k):
    """Compute the falling factorial of n to depth k.
#   编写一个函数 falling，它是一个“递降”阶乘，接受两个参数 n 和 k，
#   并返回从 n 开始向下数的 k 个连续数字的乘积。当 k 为 0 时，该函数应返回 1
    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    result = 1
    if(k != 0):
        while(k != 0):
            result = result * n
            k -= 1
            n -= 1
        # 这么一看,代码还挺简单的诶
        # 这其实就是一个不断的迭代
        return result
    else:
        return 1

#   2025年8月14日09点21分
#   启发就是，
#   1/把思考框架拿出来，看一下八个月前的，每一步都考虑清楚
#   2/判断清楚先使用 if，再用 while ，还是先使用 while，再用 if 
#   3/我的代码确实不如以前优美了。

    """
    result = 1
    while(k >= 0):
        #k是变化的那个
        if(k > 0):
            result = result * n
            k = k - 1
            n = n - 1
        else:
            return 1
    return result
#   2025年8月14日，上面的代码写于。
#   相比之前的，少了一些思路上的分析，忘记了思路分析这件事情
"""
"""
我可能需要让 AI 来帮我分析一下我的代码了，2025年8月14日09点17分
我忽略了 if 和 while 结合的时候，if 是只执行一次，但是 while 如果条件满足的话，会一直执行
所以 while 需要有一个跳出的条件，
而你上面因为 if 只执行一次，就可能导致顺序错误 —— 研究一下
"""

"""2025年8月14日 - 八个月，之前
    1. 会用到while迭代语句;
    2. while的头部条件是什么?
        k每次循环都减1;赋值给一个变量;当变量=0时,结束循环
    3. while中函数体的内容是什么?
        当 n 开始相乘的时候,还需要有一个变量来接收结果(这里就是局部变量了)
    4. 既然最后说,当k = 0时,要返回1 ,所以可能用到if语句
"""
"""
    result = 1
    if(k != 0):
        while(k != 0):
            result = result * n
            k -= 1
            n -= 1
        # 这么一看,代码还挺简单的诶
        # 这其实就是一个不断的迭代
    else:
        return 1
"""
    # 有一个疑惑,if里面包含while的时候,
    # while是执行到结束才会跳出嘛,还是只执行一次?

# Python ok --local:
# 有一个锁着的,没有通过的,所以你需要先解锁
# Python ok --local -u
# 解锁之后,就会显示代码中没有的题目,但是Lab01 中有的内容

def divisible_by_k(n, k):
    """
编写一个函数 divisible_by_k，
它接受正整数 n 和 k。它打印所有小于或等于 n 且能被 k 整除的正整数，从最小到最大。然后，它返回打印了多少个数字

思路分析：
1/打印所有小于等于的，需要用到 while 循环
2/需要定义一个数，从最小的开始，0？1？
3/需要用到判断 if，正整数，需要是 % == 0，
4/打印 print

sum = 0
num = 0
while(sum <= n):
    if(sum % k == 0 and sum != 0):
        print(sum)
        num += 1
    sum += 1 #要是把 sum 写进 if 里面，那么如果不满足条件的时候，就无法添加了。如果要写进 if，就需要也有else
    return num
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    "*** YOUR CODE HERE ***"
    # count = 0
    # i = 1
    # while i <= n:
    #     if i % k == 0:
    #         print(i)
    #         count += 1
    #     i += 1
    # return count
    
    sum = 0 # i
    num = 0 # count 
    while(sum <= n):
        if(sum % k == 0 and sum != 0):
            print(sum)
            num += 1
        sum += 1 #要是把 sum 写进 if 里面，那么如果不满足条件的时候，就无法添加了。如果要写进 if，就需要也有else
    return num # ‼️是这个位置错误了
    # 其他地方都是可以的，你可以用 1 ，也可以用 0，就是会导致 if 那里的不一样，但问题还好
    # 问题是，你的return 放错了地方，导致无法正常输出。
    # 也就是， while 循环结束之后，没有输出的东西？
    # 注意 return 的位置，记录在 note 中
    
    """
    "能被k整除的正整数"是指那些除以k后得到整数结果的正整数
    1. 这题目应该会用到while-(if-else)的结构
    2. while的头部条件:当 n<k 时,结束循环
    3. 函数体:
        if(n % k == 0):
            return/print? n
        # else 在if的语句中也是可选的
        
        n - 1
    4. 又因为需要返回打印的数量,所以要定义变量total
    5. 还有一个从小到大排序^,现在是从大到小弄,那可以反过来
        使用and,以及多定义一个变量
    """
    """
    total = 0
    div = k
    while(n >= div >= k): # 这里应该写 > ,因为是执行的条件
        # 为啥不行? > < 本身就是判断T/F,我用and 进行判断也是获得T/F
        # 就是不知道 n >= div >= k 可不可以
        if(div % k == 0):
            # 我不清楚这里是用print 还是 return
            return div
        div += 1
        total += 1
    print(total)
    # 把函数赋值到 a ,然后执行这个语句的时候,
    # 里面的while会自动执行,然后因为有return,就会输出
    # 等到调用 a 的时候,就会只输出最后一行那里,
    # 这样理解对吗?
    # 就这么简单地几行代码,我想的内容这么久这么多

# 写到了这里,2025年5月13日 10点48分
# 写成程序以后再用确实简单了,但就是花费了这么多的时间
# 只是不知道自己这样够不够,以及,能够训练自己什么?
# 思维吗?使用它们的方法?
"""

def sum_digits(y):
    """Sum all the digits of y.

编写一个函数，该函数接收一个非负整数作为输入，并计算其各位数字之和。
（提示：向下取整除法和求模运算可能会有帮助！）

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    """
    123 // 10 = 12? divaft
    123 % 10 = 3? result 
    以上是第一个末位数
        之所以先进行上面两步,是因为看到提示:使用地板除法和取模运算
        然后就先用个简单例子,列出来
        做出来好大的成就感,尤其是原本自己有畏难心理,
            不想去做,感觉做不出来
            又饿又困的
            但克服了之后,好棒啊自己
    12 // 10 = 1?
    12 % 10 = 2?
    以上是第二个末位数
        (不能思考,感觉数据很多的时候,把文字打出来,分散数据)
    if(divaft < 10):
        result += divaft
    太神奇了,代码想不出来的时候,可以列出来一些例子
    比如上面的,然后先把内容列出来,说不定就会找到规律了
    这题会用到while-(if)的语句
    """
    divaft = y # 被除之后的数,初始值为 y 
    result = 0 # 结果
    while(divaft // 10 != 0):
        result += divaft % 10
        divaft = divaft // 10
        if(divaft < 10):
            result += divaft
            return result
    """
    我感觉这个我写完了,用清晰的代码呈现出来是如此的简单
    但如果没有想到的话,可能会感觉很复杂吧……
    是如何想到的呢?
    拿一个简单的例子,(先死后活吗?)然后用 地板除法和取模运算
    先把一个案例的运算列出来,
    如果感觉数据量比较多的话,可以进行拆分,分组找规律
    找到规律之后如果感觉还记不下来,可以用文字输出
    然后找规律,用代码逻辑呈现出来
    (大概是这样?)
    
    2025年8月14日更新：
    一道题其实有很多的解法，越简洁，说明解题者的能力越厉害
    过去(大概是5月)我想到了一个解法，但现在没有想到，可能是太累了，不想在这方面动脑了？
    然后给到自己的启发，
    1/我一直在想如何判断数字的多少，然后分类，但其实分不过来。所以其实这个方法是错误的
    2/要自动剥开，而不是主动判断。自动剥开的意思就是，先获得最容易获得的（也就是 % ），
        这里我忽略了一个知识点：// 是除了之后取整，比如123 // 10 = 12
    然后有了上面地板除法，就可以很容易的把所有的数字都这样除，然后一步步的获得最容易获得的东西，也就是个位数
    总结下来是：
    1/获得最容易获得的，个位的数字
    2/如何去掉个位的数字，然后获取下一个个位的数字？ —— 地板除法
    """

# print不会导致函数退出,但return会

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    """
    看不同位置的数字,可能基本都需要10**n次方?
    2882 // 10 = 288
    2882 % 10 = 2
    x = 0
    div = n
    while(div // 10 != 0):
        if(div % 10 == 8):
            div = div // 10
            if(div % 10) == 8):
                return True
        div = div // 10
    这一题的逻辑好像和上面那个很像,都用到了// 和%
    """
    div = n
    while(div // 10 != 0):
        if(div % 10 == 8):
            div = div // 10
            if(div % 10 == 8):
                return True
        div = div // 10
    # 思路一旦打开,就好容易啊,感觉
    # 地板除法和取模运算
