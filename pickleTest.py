import pickle
import Player
import Inventory as Inv
from os import path


saveDataFile = "savedGame.p"

# player 객체 생성하기
p = Player.player()

db = {
    "inv":Inv.inv, 
    "player":p
}

#저장하기
pickle.dump(db,open(saveDataFile,"wb"))

#불러오기
if path.isfile(saveDataFile):
    db = pickle.load(open(saveDataFile,"rb"))
    print("inv",db["inv"])
    print("player.name:",db["player"].getName())    
