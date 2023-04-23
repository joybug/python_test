animals=["개","개미","고양이","박쥐","장어"]

print("animals:",animals)

#리스트 크기
print(len(animals),"종류의 동물이 리스트에 있습니다.")

animals.append("여우")

#리스트 크기
print(len(animals),"종류의 동물이 리스트에 있습니다.")


animals = list()

print("초기화:",animals)

animals=["개","개미","고양이","박쥐","장어"]

list2 = ["염소","하마","토끼"]

animals.extend(list2)

print("extend animals:",animals)

#리스트 정렬 

animals.sort();

print("sorted animals:",animals)


print("animals[2:4]:",animals[2:4])

print("animals[-1]:",animals[-1])

print("animals[-2]:",animals[-2])

print("animals[-4:-2]:",animals[-4:-2])

#요소 바꾸기
animals[2] = "암소"

print("index 2 요소바꿈 animals:",animals)

#리스트 루프
for animal in animals:
    print(animal)

