# 코드 1.1: Bag의 주요 연산을 일반함수로 구현 예.
def contains(bag, e):
    return e in bag

def insert(bag, e):
    bag.append(e)

def remove(bag, e):
    bag.remove(e)

def count(bag):
    return len(bag)

def numof(bag, e):
    count = 0
    for i in range(len(bag)):
        if bag[i] == e:
            count += 1
    return count

# 코드 1.2: Bag을 활용한 테스트 프로그램
if __name__ == '__main__':
    myBag = []
    insert(myBag, '휴대폰')
    insert(myBag, '지갑')
    insert(myBag, '손수건')
    insert(myBag, '빗')
    insert(myBag, '자료구조')
    insert(myBag, '야구공')

    print('내 가방속의 물건:', myBag)
    print('내 가방속의 물건 유무:', contains(myBag, '휴대폰'))
    print('내 가방속의 물건 개수:', count(myBag))

    remove(myBag, '휴대폰')

    print('remove 후 내 가방속의 물건:', myBag)
    print('remove 후 내 가방속의 물건 유무:', contains(myBag, '휴대폰'))
    print('remove 후 내 가방속의 물건 개수:', count(myBag))

    print('자료구조의 개수:', numof(myBag, '자료구조'))

    a= input("개수를 알고 싶은 물건을 입력하세요: ")
    print("내 가방 속 물건 개수:", numof(myBag, a))