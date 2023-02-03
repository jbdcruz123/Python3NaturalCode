


#sucess 02032023
#recursion from high to 0

class m_ite : #2

      par = -1
      ret = -1

#2

def fdisp():#2

      global m_rec

      n = len( m_rec)
      i=0
      while i < n:#3

            n_j = len( m_rec[i])
            j=0
            print(f"   [", end="")
            while j < n_j:#4
                  
                  print( f" {i= }, {j= }, {m_rec[i][j].par= } ,{m_rec[i][j].ret= } ", end="")                

                  if j == 0: #5

                        print(f" === ", end= "")
                  #5

                  j+=1
            #4

            print(f"]   ", end="")

            i+=1;
      #3

#2

def rec(  par ): #2

      #L20
      global m_rec
      global row
      global i_col
      global _max
     
      sta = 0     
  
      row +=1
      blank = m_ite()
      blank_2 = m_ite()
      m_rec.append( [   blank  ,  blank_2   ] )
      
      i_col.append( 1 )       
     
      m_rec[ row -1 ][ i_col[ row -1 ] -1 ].par = par
      
      #print(f"L20 {row -1=}, {i_col[row-1] -1= }\n {m_rec[ row -1][ i_col[ row -1] -1].par= } ")      
      #fdisp()      
      #print(f"{i_col=}\n")
      
      #input("pause")
      
      while True: #3
                
            if sta == 0: #4
           
                  row +=1
                  blank = m_ite()
                  blank_2 = m_ite()
                  m_rec.append( [  blank ,  blank_2  ] )
                  i_col.append( 1 ) 
                  m_rec[ row -1 ][ i_col[ row -1 ] -1].par = par 
              
                  #print(f"\nL22_b  {row -1 =}, {i_col[row -1] -1 = }, {par= }\n {m_rec[ row-1 ][ i_col[ row -1 ]-1 ].par= }")
                  #fdisp()                  
                  #print(f",{i_col=}\n")
                  #input("pause")

                  
                  if m_rec[ row-1 ][ i_col[ row-1 ]-1].par <= _max: #5
                                         
                        s = len( m_rec )       
                       
                        #print(f"L22_c {s= }") 
                        #input("pause")
            
                        #del ang last index sa huli 
                        m_rec.pop( s-1)
                        s_2 = len( i_col)
                        i_col.pop(s_2 -1)
                        row-=1
                        ret = 1
                        sta = 1
                        #nagsara kasi tapus na ung isang row
                        par = -1

                        #print(f"L22_c  {row-1 =}, {i_col[row-1] -1 = }, {par= }\n {m_rec[ row-1 ][ i_col[ row-1 ] -1 ].par= }")
                        #fdisp()
                        #print(f" ,{i_col=}\n")
                        #input("pause")

                        continue                      
                                                            
                  #5
                  
                  #updater sa unang function
                  par = m_rec[ row -1 ][ i_col[ row -1 ] -1].par - 1
  
                  #print(f"\nL22_d  {row-1= }, {i_col[row-1] -1= }\n {m_rec[ row-1 ][ i_col[ row -1] -1].par= }")
                  #fdisp()
                  #print(f" ,{i_col= }\n")
       
            elif sta == 1 : #4.2
            
                  #back call
                  
                  #d_row -=1
                  #print(f"\nL22_e {row -1=}, {i_col[row -1] -1 = }, {ret= }\n {m_rec[ row -1][ i_col[ row -1] -1].par= } \n")                
                  #fdisp()
                  #input("pause")

                  if i_col[ row -1] -1 ==0 :#7                                  
                        
                        #print(f"\nL23_b \n")

                        m_rec[ row -1 ][ i_col[ row -1] -1].ret = ret
                        
                        #geting trady for next col call              
                        i_col[ row -1 ] +=1

                        m_rec[ row -1 ][ i_col[ row -1 ] -1].par = m_rec[ row -1 ][ (i_col[ row -1 ] -1) -1].par  

                        #updater sa mga susunod na function
                        par = m_rec[ row -1 ][ i_col[ row -1 ] -1].par - 2         
                        sta = 0
                                         
                  elif i_col[ row -1] -1 ==1 :#7 
                   
                         #print(f"\nL23_c \n")
                
                         m_rec[ row -1 ][ i_col[ row -1 ] -1].ret = ret
                         
                         ret = m_rec[ row -1][ i_col[ row -1] -1 ].ret + m_rec[ row -1 ][ ( i_col[ row -1] - 1 ) -1 ].ret                     
                         
                         s = len(m_rec) 
                         m_rec.pop( s -1)
                         
                         s_2 = len(i_col ) 
                         i_col.pop( s_2 -1)
                         
                         #get total give 1 prev                     
                         row -=1
                         
                       
                  #7
                  
                  #print(f"\nL22_f {row -1= }, {i_col[row-1] -1= }, {ret= }, {par= }\n {m_rec[ row -1][ i_col[ row -1] -1].par= } \n")                       
                  #fdisp()                  
                  #input("pause")
 
            #4.2
            
            if row -1 == 0:# 11
                  #assig the last retrun val
                  m_rec[ row -1][ i_col[ row -1 ]  -1].ret =  ret

                  #print(f"\nL23 {row -1= }, {i_col[row-1] -1= }, {ret= }\n {m_rec[ row -1][ i_col[ row -1] -1].par= }")                       
                  #fdisp()                  
                  #input("pause")

                  return ret
            #11
            
      #3

#2

m_rec = [  ]
i_col = [  ]
_max = 1
row = 0

n = int( input("file a input max recursion") )
t = rec(  n)

print(f"\n\nfinal result: {t}")



