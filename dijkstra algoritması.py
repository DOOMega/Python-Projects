globar_var = 10

def func():
    ans = 0
    for i in range(1000):
        ans += globar_var * i
    print(ans)
    return ans

func() 