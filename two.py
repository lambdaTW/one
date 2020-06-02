'''
請寫一個程式,Input 是一個數字,Output 是從 1 到這個數字,扣除掉所有 3 的
倍數以及 5 的倍數,但是需要保留同時是 3 和 5 的倍數的總數字數。
'''

def run(max_num):
    return len([
        num
        for num in range(1, max_num+1)
        if (
                num % 15 == 0 or
                (
                    num % 3 != 0 and
                    num % 5 !=0
                )
        )
    ])


if __name__ == '__main__':
    while True:
        try:
            max_num = int(input('Please input a integer: '))
            print(run(max_num))
        except KeyboardInterrupt:
            break
        except Exception:
            pass
