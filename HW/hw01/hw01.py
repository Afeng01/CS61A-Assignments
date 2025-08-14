from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-1, 4)
    3
    >>> a_plus_abs_b(-1, -4)
    3
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)
    #正常是 a + b 这种，但当 f 是在操作符的位置，那么就需要使用 add 这种

def a_plus_abs_b_syntax_check():
    """Check that you didn't change the return statement of a_plus_abs_b.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return f(a, b)']
    """
    # You don't need to edit this function. It's just here to check your work.


def two_of_three(i, j, k):
    """Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k.
    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    return (i + j + k - min(i,j,k) - max(i,j,k))**2 + (min(i,j,k))**2
#   用三个数的和，减去最大的，减去最小的，得到中间的，然后平方，再加上最小的。2025年8月13日
#   自己想出来的，然后发现，其实整体的表达式是可以省略一些的。看了看下面的内容：
#    就是用a的平方+b的平方+c的平方，减去最大数的平方，好简洁啊
#    i**2 + j**2 + k**2 - max(i,j,k)**2
#   i**2 代表的意思是: i的平方 ; 如果写成i**i , 就是在说i 的 i 次方了
#   除非是 i * i , 那可能意思才是 i 的平方吧?
#   i**i + j**j + k**k - max(i,j,k)*max(i,j,k)
#   min(i*i+j*j, i*i+k*k, j*j+k*k)
#   add(min(i,j,k)*min(i,j,k))

def two_of_three_syntax_check():
    """Check that your two_of_three code consists of nothing but a return statement.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    # You don't need to edit this function. It's just here to check your work.

def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    result = n - 1
    while( result > 0 ):
        if (n % result == 0 ):
            return result
        else:
            result = result-1 #经测试,if-else后面带不带return似乎都可以
    "*** YOUR CODE HERE ***"
    """大概是2025年8月13日-6month前修改。
    factor = n - 1
    while(factor > 0):
        if(n % factor == 0):#这个时候就已经是正确答案了,就可以直接返回
            return factor
        factor -= 1
2025年8月13日的 code 
# factor = 1;
# while(factor <= n):
#     if n > 1:
#         n % factor == 0
#         print(factor)
#         factor = factor + 1
#         return max()
#     else:
#         return
#   2025年8月13日，你习惯性地从最小的开始遍历，但其实可以从最大的(也就是比 n 小一个的)地方开始
    **返回最大的，那就从最大的开始**
    **而且这还是个很常见的循环遍历系统**
"""

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    '''我先实现的if-else,然后发现if只能判断一次,
    但我需要判断多次,所以需要在外面套上一个while,来不断循环'''
    """steps = 0 
    result = n  #这个步骤是多余的
    while(result >= 1):
        print(result)
        steps += 1
        if(result % 2 == 0): #如果是偶数;如果是奇数;如果是1
            result = result//2
            print(result)   
            # 然后你会发现,这个print和循环开始时候的print是重复的;
            # 如果这里打印了,再进入循环的时候,还会打印一次
        else:
            result = result * 3 + 1
            print(result)"""
    """最后这里我不清楚,如何把步骤和步骤数都打印出来
    好简洁阿,参考答案的步骤;另外,不需要在if那里写return吗?"""
    steps = 1 
    while(n != 1):
        print(n)
        # steps += 1 # 这个正常是放在else下面的
        if(n % 2 == 0): #如果是偶数;如果是奇数;如果是1
         # if后面可以不用带括号,带括号似乎是Java留下来的习惯
            n = n//2
        else:
            n = n * 3 + 1
        steps += 1 
        # 放在最后是因为,初始步骤为1,
        # 如果在外面设置为 0 的话,1的话不进入循环,
        # 然后步骤就是 0 了
    # while循环中都是不等于1的情况,
    # 如果最后n=1了,哪还需要再打印一次
    print(n)
    return steps # 我不明白这一点 , 放在这里 , 有何作用(b和b=)
# 编写一个函数，该函数接收参数 n，打印出从 n 开始的冰雹序列，并返回序列的步数
    """
    foots = 0;//这里在想要不要默认 1 ，可能默认 1 会更好
    while(n != 0): 
    # n 得常在，重新赋值到 n ，我是直接返回的值，但忽略了返回之后 n 就只能出现一次了
        if(n == 1):
            print(1)
            foots = foots + 1
        else:
            print(n)
            if(n % 2 == 0):
                foots = foots + 1 
                //这里可以看出，每一个步骤都有 foots，于是可以把他们提出来，放在循环的外面
                return n // 2 
                //这里不要直接返回，要重新赋值给 n ，这样才能在 while 循环的时候一直进行下去
            else:
                foots = foots + 1
                //这个可以简写成 foots += 1
                //看一下上面的 print(n)，因为赋值了 n 之后，还满足条件的时候，是会进入 while 的
                //在 while 循环没结束的时候，是会进入到循环体内 print 出来的
                //但如果循环体结束了，就会有最后一次的没有打印出来，所以那里还需要放上一个
                return (n * 3) + 1
    return foots # 返回总步数
    //return 的时候，就退出这个程序了
    写个作业，40分钟……然后复盘要20分钟
    """
