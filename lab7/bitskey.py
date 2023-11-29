class bitskey:
    def __init__(self, x):
        self.x = x

    def get(self):
        return self.x

    # k 번 비트가 j 인지
    def bits(self, k, j):
        # x를 k 만큼 시프트
        return (
                (self.x >> k)   # 체크하고자 하는 비트가 마지막 자리에 오게 하기
                &
                ~               # 00001
                (
                        ~0      # 11111
                        << j    # 11110
                )
        )


a = int(input('입력 : '))
while a != 999:
    v = bitskey(a)
    print('키값 :', v.get())
    print(v.bits(4, 1))
    print(v.bits(3, 1))
    print(v.bits(2, 1))
    print(v.bits(1, 1))
    print(v.bits(0, 1))
    a = int(input('a = '))
