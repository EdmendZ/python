# 这是一个简单的 Python 示例程序

def greet(name):
    """向用户打招呼"""
    return f"你好，{name}！欢迎学习 Python！"

def calculate_sum(a, b):
    """计算两个数的和"""
    return a + b

if __name__ == "__main__":
    # 测试 greet 函数
    user_name = "世界"
    print(greet(user_name))
    
    # 测试 calculate_sum 函数
    num1 = 10
    num2 = 20
    result = calculate_sum(num1, num2)
    print(f"{num1} + {num2} = {result}")
    
    # 简单的循环示例
    print("\n数字列表:")
    for i in range(1, 6):
        print(f"  第 {i} 个数字: {i}")
