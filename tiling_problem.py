#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      keikakoo
#
# Created:     03/11/2019
# Copyright:   (c) keikakoo 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from copy import *
class side_type():
    dent_in=-1
    dent_out=1
    simple=0
class shape:
    joker_shape=0 # number of object which  will be create and deformed based on the situation
    def __init__(self,leftside,rightside,upside,downside):
        self.leftside =leftside
        self.rightside = rightside
        self.upside=upside
        self.downside=downside
        self.surround = 0
        self.deformityNo=abs(self.downside)+abs(self.upside)+abs(self.rightside)+abs(self.leftside)
    def is_full_surrounded(self):
        if self.surround==4:
            return True
        else:
            return False
    def rotate_right(self):
        temp1=self.downside;
        temp2=self.upside
        temp3=self.rightide
        self.upside=self.leftside
        self.leftside=temp1
        self.downside=temp3
        self.rightside=temp2
    def rotate_left(self):
        #rotate_left  to fit
        temp1=self.downside;
        temp2=self.upside
        temp3=self.rightide
        self.downside=self.leftside
        self.upside=temp3
        self.rightside=temp1
        self.leftside=temp2


##    def is_bigger(self,p):
##        if(abs(self.downside)+abs(self.upside)+abs(self.rightside)+abs(self.leftside)
##        >abs(p.downside)+abs(p.upside)+abs(p.rightside)+abs(p.leftside)):
##            return True
##        else:
##            return False
def main():
#getting the input from the user
    n=input("please enter the number of tiles")
    n=int(n)
    #entery=Zeros=[[0]*n^2 for _ in range(n)]
    entery=[]
    for i in range (0,int(math.pow(n,2))):
            entery.append(shape(int(input("left side")),int(input("right side")),int(input("up side")),int(input("down side"))))
#geting in put from file

##
###sort the entry by their number of deformity use the is bigger func
##    entery.sort(key=lambda x:x.deformityNo,reverse=True)
##    for i in range(len(entery)):
##        print(entery[i].deformityNo,"\n")check sort
#map of puzzle
    mapp=Nones=[[None]*n for _ in range(n)]
    copyofData=deepcopy(entery);
#map of the puzzle
    not_perfect_match=False
    for i in range(1,n-1):
        for j in range(1,n-1):
            matchup=0;
            fit=False
            while(fit==False and matchup<=len(copyofData)):# if match up is more than that it means we are repeating process there is no match
                new_item=copyofData.pop()#it commit any changes to real data because it is just a refrence to object
                if(i==1):
                    #radife aval
                    if(j==1):
                        mapp[i][j]=new_item
                        fit=True
                        break
                    else:
                        #first row except first tile
                        if(mapp[i][j-1].rightside==-(new_item.leftside)):
                            mapp[i][j]=new_item
                            fit=True
                            break
                        elif(mapp[i-1][j].rightside==-(new_item.upside)):
                            #rotate_left  to fit
                            new_item.rotate_left()
                            #rotation compelet to put
                            mapp[i][j]=new_item
                            fit=True
                            break
                            #do this for check other side to
                        elif(mapp[i][j-1].rightside==-(new_item.downside)):
                            #rotate_right  to fit
                            new_item.rotate_right()
                            #rotation complete
                            mapp[i][j]=new_item
                            fit=True
                            break
                        else:
                           copyofData.append(new_item)
                else:
                    #second row to tend
                    if(j==1):
                        if(mapp[i][j-1].downside==-(new_item.upside)):
                            mapp[i][j]=new_item
                            fit=True
                            break
                        elif(mapp[i-1][j].downside==-(new_item.right_side)):
                            #rotate_left  to fit
                            new_item.rotate_left()
                            #rotation compelet to put
                            mapp[i][j]=new_item
                            fit=True
                            break
                            #do this for check other side to
                        elif(mapp[i][j-1].downside==-(new_item.left_side)):
                            #rotate_right  to fit
                            new_item.rotate_right()
                            #rotation complete
                            mapp[i][j]=new_item
                            fit=True
                            break
                        else:
                           copyofData.append(new_item)# if new_item doesn't match algorithm should return to the tiles list again and test another tile
                    else:
                        #aval saf nabashim va radif aval nabashim
                        if(mapp[i][j-1].rightside==-(new_item.left_side) and mapp[i-1][j].downside==-(new_item.upside)):
                            mapp[i][j]=new_item
                            fit=True
                            break
                        elif(mapp[i][j-1].rightside==-(new_item.upside) and mapp[i-1][j].downside==-(new_item.rightside)):
                            #rotate_left  to fit
                            new_item.rotate_left()
                            #rotation compelet to put
                            mapp[i][j]=new_item
                            fit=True
                            break
                            #do this for check other side to
                        elif(mapp[i][j-1].rightside==-(new_item.rightside) and mapp[i-1][j].downside==-(new_item.downtside)):
                            #two rotation to left
                            #rotate_left  to fit
                            new_item.rotate_left()
                            #end of first rotation
                            #rotate_left  to fit
                            new_item.rotate_left()
                            #rotation compelet to put
                            mapp[i][j]=new_item
                            fit=True
                            break
                        elif(mapp[i][j-1].rightside==-(new_item.downside) and mapp[i-1][j].downside==-(new_item.ledftside)):
                            #one rotation to the right to fit
                            new_item.rotate_right()
                            #rotation complete
                            mapp[i][j]=new_item
                            fit=True
                            break
                        else:
                            #no rotation makes the fit add new item to list and use another tile
                            copyofData.append(new_item)#so return item to the list of tiles
                matchup+=1

            copyofData.sort(key=lambda x:x.deformityNo,reverse=True)
            if(matchup>len(copyofData)):
                shapless=shape(-(mapp[i][j-1].rightside) if mapp[i][j-1]!=None else 0,
                -(mapp[i][j+1].leftside) if mapp[i][j-1]!=None else 0,
                -(mapp[i-1][j].downside) if mapp[i][j-1]!=None else 0,
                -(mapp[i+1][j].upside) if mapp[i][j-1]!=None else 0)
                shape.joker_shape+=1
            #after each matching we should sort list again for another matching
    #fill the zeroth line
    for i in range(n):
        fit=False
        matchup=0
        while(fit==False and matchup<=n):
            new_item=copyofData.pop()
            if(i==0):
                #khoone aval
                if(new_item.deformityNo==2):
                    if(new_item.upside==0 and new_item.leftside==0):
                        mapp[0][i]=new_item
                    elif(newitem.leftside==0 and new.downside==0):
                        #rotate right to fit
                        new_item.rotate_right()
                        #rotation complete
                        mapp[0][i]=new_item
                        fit=True
                        break
                    elif(new_item.downside==0 and new_item.rightside==0):
                        #two rotation to right to fit
                        new_item.rotate_right()
                        #rotation complete
                        new_item.rotate_right()
                        mapp[0][i]=new_item
                        fit=True
                        break
                    elif(new_item.upside==0 and new_item.rightside==0):
                        #on rotatio to left
                        new_item.rotate_left()
                        mapp[0][i]=new_item
                        fit=True
                        break
                    else:
                        copyofData.append(new_item)

            else:
                #it wasn't first cell in mapp
                if(new_item.deformityNo<4):
                    if(mapp[0][i-1].rightside==-(new_item.leftside) and new_item.upside==0 and new_item.downside==-(mapp[1][i].upside)):
                        mapp[0][i]=new_item
                    elif(mapp[0][i-1].rightside==-(new_item.upside) and new_item.rightside==0 and new_item.leftside==-(mapp[1][i].upside)):
                        #rotate left
                        new_item.rotate_left()
                        mapp[0][i]=new_item
                        fit=true
                        break
                    elif(mapp[0][i-1].rightside==-(new_item.rightside) and new_item.downside==0 and new_item.upside==-(mapp[1][i].upside)):
                        #two rotate to left
                        new_item.rotate_left()
                        new_item.rotate_left()
                        mapp[0][i]=new_item
                        fit=True
                        break
                    elif(mapp[0][i-1].downside==-(new_item.rightside) and new_item.leftside==0 and new_item.rightside==-(mapp[1][i].upside)):
                        #one rotate to right
                        new_item.rotate_right()
                        mapp[0][i-1]=new_item
                        fit=True
                        break
                    else:
                        copyofData.append(new_item)
                else:
                    copyofData.append(new_item)

            matchup+=1
        if(matchup>len(copyofData)):
            shapless=shape(-(mapp[i][j-1].rightside) if mapp[i][j-1]!=None else 0,
            -(mapp[i][j+1].leftside) if mapp[i][j-1]!=None else 0,
            -(mapp[i-1][j].downside) if mapp[i][j-1]!=None else 0,
            -(mapp[i+1][j].upside) if mapp[i][j-1]!=None else 0)
            shape.joker_shape+=1
    #por kardane sotone akhar
    for i in range(n-1):
            fit=False
            matchup=0
            while(fit==False and matchup<=n):
                new_item=copyofData.pop()
                if(i==0):
                    #khoone aval
                    if(new_item.deformityNo==2):
                        if(new_item.upside==0 and new_item.leftside==0 and mapp[i][n-2].rightside==-(new_item.leftside)):
                            mapp[i][n-1]=new_item
                        elif(newitem.leftside==0 and new.downside==0 and mapp[i][n-2].rightside==-(new_item.downside) ):
                            #rotate right to fit
                            new_item.rotate_right()
                            #rotation complete
                            mapp[i][n-1]=new_item
                            fit=True
                            break
                        elif(new_item.downside==0 and new_item.rightside==0 and mapp[i][n-2].rightside==-(new_item.rightside)):
                            #two rotation to right to fit
                            new_item.rotate_right()
                            #rotation complete
                            new_item.rotate_right()
                            mapp[i][n-1]=new_item
                            fit=True
                            break
                        elif(new_item.upside==0 and new_item.rightside==0 and mapp[i][n-2].rightside==-(new_item.upside)):
                            #on rotatio to left
                            new_item.rotate_left()
                            mapp[i][n-1]=new_item
                            fit=True
                            break
                        else:
                            copyofData.append(new_item)

                else:
                    #it wasn't first cell in mapp
                    if(new_item.deformityNo<4):
                        if(mapp[i][n-2].rightside==-(new_item.leftside) and new_item.rightside==0 and new_item.upside==-(mapp[i-1][n-1].downside)):
                            mapp[i][n-1]=new_item
                        elif([i][n-2].rightside==-(new_item.upside) and new_item.rightside==0 and new_item.right==-(mapp[i-1][n-1].downside)):
                            #rotate left
                            new_item.rotate_left()
                            mapp[i][n-1]=new_item
                            fit=true
                            break
                        elif(mapp[i][n-2].rightside==-(new_item.rightside) and new_item.downside==0 and new_item.downside==-(mapp[i-1][n-1].downside)):
                            #two rotate to left
                            new_item.rotate_left()
                            new_item.rotate_left()
                            mapp[i][n-1]=new_item
                            fit=True
                            break
                        elif(mapp[i][n-2].downside==-(new_item.rightside) and new_item.leftside==0 and new_item.leftside==-(mapp[i-1][n-1].downside)):
                            #one rotate to right
                            new_item.rotate_right()
                            mapp[i][n-1]=new_item
                            fit=True
                            break
                        else:
                            copyofData.append(new_item)
                    else:
                        copyofData.append(new_item)
                matchup+=1
            if(matchup>len(copyofData)):
                shapless=shape(-(mapp[i][j-1].rightside) if mapp[i][j-1]!=None else 0,
                -(mapp[i][j+1].leftside) if mapp[i][j-1]!=None else 0,
                -(mapp[i-1][j].downside) if mapp[i][j-1]!=None else 0,
                -(mapp[i+1][j].upside) if mapp[i][j-1]!=None else 0)
                shape.joker_shape+=1
#fill the first column
    for i in range(1,n):
                fit=False
                matchup=0
                while(fit==False and matchup<=n):
                    new_item=copyofData.pop()
                    if(i==n-1):
                        #khoone aval
                        if(new_item.deformityNo==2):
                            if(new_item.leftside==0 and new_item.downside==0 and mapp[i-1][0].downside==-(new_item.upside)):
                                mapp[i][0]=new_item
                            elif(newitem.leftside==0 and new.upside==0 and mapp[i-1][0].downside==-(new_item.rightside) ):
                                #rotate right to fit
                                new_item.rotate_right()
                                #rotation complete
                                mapp[i][0]=new_item
                                fit=True
                                break
                            elif(new_item.upside==0 and new_item.rightside==0 and mapp[i-1][0].downside==-(new_item.downside)):
                                #two rotation to right to fit
                                new_item.rotate_right()
                                #rotation complete
                                new_item.rotate_right()
                                mapp[i][0]=new_item
                                fit=True
                                break
                            elif(new_item.leftside==0 and new_item.upside==0 and mapp[i-1][0].downside==-(new_item.righttside)):
                                #on rotatio to left
                                new_item.rotate_left()
                                mapp[i][0]=new_item
                                fit=True
                                break
                            else:
                                copyofData.append(new_item)

                    else:
                        #it wasn't last cell in column
                        if(new_item.deformityNo<4):
                            if(mapp[i][1].leftside==-(new_item.righttside) and new_item.leftside==0 and new_item.upside==-(mapp[i-1][0].downside)):
                                mapp[i][0]=new_item
                                fit=true
                                break
                            elif(mapp[i][1].leftside==-(new_item.downside) and new_item.upside==0 and new_item.rightside==-(mapp[i-1][0].downside)):
                                #rotate left
                                new_item.rotate_left()
                                mapp[i][0]=new_item
                                fit=true
                                break
                            elif(mapp[i][1].leftside==-(new_item.rightside) and new_item.rightside==0 and new_item.upside==-(mapp[i-1][0].downside)):
                                #two rotate to left
                                new_item.rotate_left()
                                new_item.rotate_left()
                                mapp[i][0]=new_item
                                fit=true
                                break
                            elif(mapp[i][1].leftside==-(new_item.upside) and new_item.downside==0 and new_item.leftside==-(mapp[i-1][0].downside)):
                                #one rotate to right
                                new_item.rotate_right()
                                mapp[i][0]=new_item
                                fit=true
                                break
                            else:
                                copyofData.append(new_item)
                        else:
                            copyofData.append(new_item)

                    matchup+=1
                if(matchup>len(copyofData)):
                    shapless=shape(-(mapp[i][j-1].rightside) if mapp[i][j-1]!=None else 0,
                    -(mapp[i][j+1].leftside) if mapp[i][j-1]!=None else 0,
                    -(mapp[i-1][j].downside) if mapp[i][j-1]!=None else 0,
                    -(mapp[i+1][j].upside) if mapp[i][j-1]!=None else 0)
                    shape.joker_shape+=1
#fill the last row
    for i in range(1,n-1):
                fit=False
                matchup=0
                while(fit==False and matchup<=n):
                    new_item=copyofData.pop()
                    if(i==n-2):
                        #khoone akhar
                        if(new_item.deformityNo==1):
                            if(new_item.downside==0 and new_item.rightside==-(mapp[n-1][i+1].leftside) and mapp[n-1][i-1].rightside==-(new_item.leftside)
                            and mapp[n-2][i].downside==-(new_item.upside)):
                                mapp[n-1][i]=new_item
                                fit=True
                                break
                            elif(new_item.rightside==0 and new_item.upside==-(mapp[n-1][i+1].leftside) and mapp[n-1][i-1].rightside==-(new_item.downside)
                            and mapp[n-2][i].downside==-(new_item.leftside) ):
                                #rotate right to fit
                                new_item.rotate_right()
                                #rotation complete
                                mapp[n-1][i]=new_item
                                fit=True
                                break
                            elif(new_item.upside==0 and new_item.leftside==-(mapp[n-1][i+1].leftside) and mapp[n-1][i-1].rightside==-(new_item.rightside)
                            and mapp[n-2][i].downside==-(new_item.downside)):
                                #two rotation to right to fit
                                new_item.rotate_right()
                                #rotation complete
                                new_item.rotate_right()
                                mapp[n-1][i]=new_item
                                fit=True
                                break
                            elif( new_item.right==0 and new_item.downside==-(mapp[n-1][i+1].leftside) and mapp[n-1][i-1].rightside==-(new_item.upside)
                            and mapp[n-2][i].downside==-(new_item.rightside)):
                                #on rotatio to left
                                new_item.rotate_left()
                                mapp[n-1][i]=new_item
                                fit=True
                                break
                            else:
                                copyofData.append(new_item)

                    else:
                        #it wasn't last cell in row
                        if(new_item.deformityNo<4):
                            if(new_item.downside==0 and mapp[n-2][i].downside==-(new_item.upside) and mapp[n-1][i-1].rightside==-(new_item.leftside)):
                                mapp[n-1][i]=new_item
                                fit=true
                                break
                            elif(new_item.rightside==0 and mapp[n-2][i].downside==-(new_item.leftside) and mapp[n-1][i-1].rightside==-(new_item.downside)):
                                #rotate left
                                new_item.rotate_left()
                                mapp[n-1][i]=new_item
                                fit=true
                                break
                            elif(new_item.upside==0 and mapp[n-2][i].downside==-(new_item.downside) and mapp[n-1][i-1].rightside==-(new_item.rightside)):
                                #two rotate to left
                                new_item.rotate_left()
                                new_item.rotate_left()
                                mapp[n-1][i]=new_item
                                fit=true
                                break
                            elif(new_item.leftside==0 and mapp[n-2][i].downside==-(new_item.rightside) and mapp[n-1][i-1].rightside==-(new_item.upside)):
                                #one rotate to right
                                new_item.rotate_right()
                                mapp[n-1][i]=new_item
                                fit=true
                                break
                            else:
                                copyofData.append(new_item)
                        else:
                            copyofData.append(new_item)

                    matchup+=1
                if(matchup>len(copyofData)):
                    shapless=shape(-(mapp[i][j-1].rightside) if mapp[i][j-1]!=None else 0,
                    -(mapp[i][j+1].leftside) if mapp[i][j-1]!=None else 0,
                    -(mapp[i-1][j].downside) if mapp[i][j-1]!=None else 0,
                    -(mapp[i+1][j].upside) if mapp[i][j-1]!=None else 0)
                    shape.joker_shape+=1


    if(shape.joker_shape>0):
        print("there is no perfect match")
    else:
        print("puzzle completed")



if __name__ == '__main__':
    main()






