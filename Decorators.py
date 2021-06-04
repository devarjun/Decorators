def NewSub(func):
    def Sub(a,b):
        if a<b:
            a,b = b,a
            print(a - b)
    return Sub
@NewSub
def MainSub(a,b):
    print(a - b)
MainSub(63,136)
