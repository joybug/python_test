#인벤토리 시스템

inv = { 
    "StructureKey":False,
    "Coins":0
}

#인벤토리에 열쇠 추가
def takeStructureKey():
    inv["StructureKey"] = True

#열쇠삭제
def dropStructureKey():
     inv["StructureKey"] = False

def hasStructureKey():
    return inv["StructureKey"]

def takeCoins(coins):
    inv["Coins"] += coins

def dropCoins(coins):
    inv["Coins"] -= coins

def numCoins():
    return inv["Coins"]

# 인벤토리 출력하기
def display():
    print("******* 인벤토리 *******")
    print("가진 동전은 ", numCoins(), "개입니다.")
    if hasStructureKey():
        print("파랗게 빛나는 열쇠가 있습니다.")
    print("************************")