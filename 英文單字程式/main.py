from database import ConnectDatabase
import random
from typing import List
import os


class Effect(ConnectDatabase):
    def __init__(self):
        super(Effect, self).__init__()
        self.c = ConnectDatabase()

    def shuffle(self, day: int) -> List[int]: #打亂ID
        idcount = self.c.count_id(day)
        idcountlist = [i for i in range(1, int(idcount) + 1)]
        random.shuffle(idcountlist)
        return idcountlist

    def choose_model(self, e): #選擇模式
        choose = 0
        while True:
            try:
                choose = int(input("考試輸入 1 , 複習輸入 2\n請輸入: "))
            except ValueError:
                print("輸入錯誤，請重新輸入")
                continue

            if choose == 1:
                print("目前共有: {0}天".format(self.c.count_days()))
                day = int(input("請輸入要考第幾天: "))
                e.exam(e, day)
                break
            elif choose == 2:
                print("目前共有: {0}天".format(self.c.count_days()))
                day = int(input("請輸入複習第幾天: "))
                if day <= int(self.c.count_days()):
                    self.c.review(day)
                    os.system("pause")
                    continue
                else:
                    print("輸入錯誤天數，請重新輸入")
                    continue
            else:
                print("輸入錯誤數字，請重新輸入")
                continue

    def exam(self, e, day: int, tcount: int = 0): #考試
        wronglist = []
        listlen = int(self.c.count_id(day))
        vocabulary = self.c.shuffle_voc(day, e.shuffle(day))
        for i in range(listlen):
            print("{0}.".format(i+1),vocabulary[i][1:3])
            ans = input("答案: ")
            if ans == vocabulary[i][3]:
                print("答對")
                tcount += 1
            else:
                print("答錯")
                print("正確答案:", vocabulary[i][3])
                wronglist.append(vocabulary[i][1:4])
        print("答題數:", tcount, "/", listlen)
        print("錯誤題目:")
        for i in range(len(wronglist)):
            print("{0}.".format(i+1),wronglist[i],sep="\n")
        os.system("pause")
        e.choose_model(e)



def main():
    e = Effect()
    print("英文單字練習程式 作者: 黃致瑋",end="\n")
    print("填寫答案時連標點符號都要一樣",end="\n\n")
    e.choose_model(e)


if __name__ == "__main__":
    main()
