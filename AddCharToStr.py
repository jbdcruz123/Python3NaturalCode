#! /usr/bin/python3
def main():#1B
  aV = []
  #input empty string, u can use None 2
  bV = ["","",""]
  for i in range(0, 3, 1): 
    aV.append([])
    for j in range(0, 5, 1):
      aV[i].append(-2) 
  aV[0][0] = "1"
  aV[0][1] = "2"
  aV[1][0] = "3"
  aV[1][1] = "4"
  aV[2][0] = "5"
  aV[2][1] = "6"
  print(f"input sa aV{aV}")
  bI=0
  for i in range(0,3):#2
    for j in range(0,5):#3
      print(f"i {i} j {j} type {type(aV[i][j])} value {aV[i][j]}")
      #trace int data type by using == int (same also in float str etc)
      if type( aV[i][j]) == int:#4
        break
      #4
      bV[bI]= bV[bI] + aV[i][j] 
    #3  
    bI+=1   
  #2
  print(f"\n\nlaman ng bV {bV}")
#1B 

main()
