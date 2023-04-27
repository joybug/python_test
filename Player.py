############################################
# Player.py
# player 클래스
############################################

# player 클래스 정의하기
class player:   
    def __init__(self,name="탐험가",livesLeft=3,boulderVisits=0): #생성자 적용
        # 속성
        self.name = name
        self.livesLeft = livesLeft
        self.boulderVisits = boulderVisits

    # name 속성 set
    def setName(self,name):
        self.name=name

    # name 속성 얻기
    def getName(self):
        return self.name

    # 플레이어 라이프 개수 얻기
    def getLivesLeft(self):
        return self.livesLeft

    # 플레이어 죽음
    def died(self):
        if self.livesLeft > 0:
            self.livesLeft -= 1

    # 플레이어가 살았다면
    def isAlive(self):
        return True if self.livesLeft > 0 else False

    # 바위 더미 방문 횟수 얻기
    def getBoulderVisits(self):
        return self.boulderVisits

    # 플레이어 바위 더미 방문하기
    def visitBoulder(self):
        self.boulderVisits += 1