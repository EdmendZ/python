"""
    @Author:Irene
    @Time:2026/4/29
    @Desc:
"""
"""
    需求：
        有一个生成器，它会根据task变量的值，来决定返回整数还是字母。
        当task=0的时候，它会返回1个整数，这个整数从1开始，依次递增，当整数到10后，回到1
        当task=1的时候，它会返回1个字母，这个字母从a开始，依次递增，当字母到z后，回到a
"""
def num_letter_generator_func():
    task = 0
    num = 1
    letter = 'a'
    control_value = None
    while True:
        match task:
             case 0:
                 control_value = yield num
                 num += 1
                 if num>10:
                     num = 1
             case 1:
                 control_value = yield letter
                 letter = chr(ord(letter)+1)
                 if letter > 'z':
                     letter = 'a'
        if control_value is not None:
            task = control_value



if __name__ == '__main__':
    g = num_letter_generator_func()
    print(next(g))#1
    print(next(g))#2
    print(next(g))#3
    print(next(g))#4
    print(g.send(1)) # task=1  a
    print(next(g)) #b
    print(next(g))#c
    print(next(g))#d
    print(next(g))#e
    print(g.send(0))#5
    print(next(g))#6
    print(next(g))#7