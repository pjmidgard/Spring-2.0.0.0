from time import time
cvf=0
import os
import binascii
self="'"

namez = input("for compress c or extract e? ")
#@Author Jurijus Pacalovas
class compression:

    def cryptograpy_compression(self):

                
                
                self.name = "Author: Jurijus Pacalovas"

                print(self.name)

                if namez!="c" and namez!="e":
                    print("Your enter incorrect letter")
                
                if namez=="c":


                    
                   
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                   
                    long_block=100
                        
                    namea=""
                    namem=""
                    namema="?"
                   
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)

                    long=len(name)
                   

                    

                    
                    
                   
                    
                    Deep_long=240
                    Deep_long_All=Deep_long*16
                    block_size_long=16
                    Times_compression=2
                    
                    name_cut=len(".bin")
                    
                    nameas=name+".bin"
                    name_bofore=len(nameas)
                    F=0
                    
                    
                    	 
                    nac=len(nameas)
                    
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    
                 
                    size_data3=""
                    size_data2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
                        #import paq
                        #data=paq.compress(data)
                        data1=data
                        size_after2=len(data)
                        #print(size_after2)
                        if len(data)==0:
                            x4=0.0
                            print(x4)
                            raise SystemExit
                            
                      
                         

                  
                        s=str(data)
                        
                        Limit_size_of_file=0
                        File_size_Divide=0
                        lenf1=len(data)
                       
                    
                            
  
                            
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1
                                            
                                   

                                    if countraz==1:
                                        size_data2=size_data
                            
                                    n = int(size_data2, 2)
                                
                                    qqwslenf=len(size_data2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1

                                    size_data2=size_data

                                    lenf3=len(size_data2)
                                lenf2=len(size_data2)
                                size_data6=""
                                size_data4=""
                                size_data7=""
                                size_data8=""

                                
                                    
                                
                                size_data3=size_data2
                                size_data10=size_data2

                                long_file=len(size_data3)
                               
                           
                                
                                long_block=16
                               
                               
                                
                                
                                times_of_times=0
                           
                                str_find=""
                          
                                

                                cvf1=1
  
                                if cvf1==1:
                                    times_compression=0  
                                  
                                    

                                   
                                    
                                   
                                    
                                  
                                    
                                    Find_guess=0
                                    while Find_guess!=1:
                                        
                                        while  times_of_times!=Times_compression:


                                                    
                                                   
                                                    long_block=block_size_long
                                                    long2=len(size_data3)
                                                    
                                                    blocks=8
                                                    size_compress=63
                                                    size_data1=""
                                                    
                                                     
                                                    block=0

                                                    #b=format(predict,'04b')
                                                    #predict=predict+1
                                                    #if predict==16:
                                                        #predict=0
                                                    
                                                    long=len(size_data3)
                                                    Times6=0
                                                    size_data15=""
                                                    #print(long)
                                                    
                                                    while block<long:

                                                                                
                                                                                Zeroes6=size_data3[block+blocks:block+(blocks*2)]
                                                                                Zeroes=size_data3[block:block+2]
                                                                                Zeroes2=size_data3[block+2:block+4]
                                                                                Zeroes3=size_data3[block+4:block+6]
                                                                                Zeroes4=size_data3[block+6:block+8]
                                                                                       
                                                                                if Zeroes6=="01101100":
                                                                                	size_data1="00000000"    
                                                                                
                                                                                                                                                                                                 
                                                                                elif Zeroes6=="00000000":
                                                                                	size_data1="01101100"
                                                                                	                  
                                                                                else: 
                                                                                
                                                                                	size_data1=Zeroes6                        


                                                                                if Zeroes=="00":
                                                                                    size_data5="11"

                                                                                elif Zeroes=="11":
                                                                                    size_data5="00"                                                                               

                                                                                elif Zeroes=="01":
                                                                                    size_data5="01"

                                                                                elif Zeroes=="10":
                                                                                    size_data5="10"   



                                                                                if Zeroes2=="00":
                                                                                    size_data4="10"

                                                                                elif Zeroes2=="10":
                                                                                    size_data4="00"

                                                                                elif Zeroes2=="01":
                                                                                    size_data4="01"

                                                                                elif Zeroes2=="11":
                                                                                    size_data4="11"   





                                                                                if Zeroes3=="10":
                                                                                        size_data7="11"

                                                                                elif Zeroes3=="11":
                                                                                        size_data7="10"                                                                             
                                                                                elif Zeroes3=="00":
                                                                                        size_data7="00"

                                                                                elif Zeroes3=="01":
                                                                                        size_data7="01"



                                                                                if Zeroes4=="10":
                                                                                        size_data8="11"

                                                                                elif Zeroes4=="11":
                                                                                        size_data8="10"                                                                             
                                                                                elif Zeroes4=="00":
                                                                                        size_data8="00"

                                                                                elif Zeroes4=="01":
                                                                                        size_data8="01"


                                                                
                                                                                                                                                                                                                                                                                                                     	                                                                                          

                                                                                size_data6=size_data6+size_data5+size_data4+size_data7+size_data8+size_data1
                                                                                block=block+(blocks*2)
                                                                                
                                                                                #print(block)
                                                         
                                                    times_compression=times_compression+1
                                                    
                                                    #print(times_compression)
                                                    
                                                    
                                                    size_data3=size_data6
                                                    
                                                    Where4=0
                                                    
                                                    
                                                    #print(len(size_data6))
                                                    size_data6=""
                                                    times_of_times=times_of_times+1
                                                    
                                        long_after=len(size_data3)
                                        long2=len(size_data3)

                                        
                                        size_data9=size_data3
                                        #print(size_data9)
                                        
                                           

                                        
                                        
                                        Check_equal=0

                                        
                                            
                                        
                                        
                                        long_file=len(size_data10)
                                        long_after=len(size_data9)
                                        #print(long_after) 
                                       
                                        if long_file>long_after or long_block<=long_after:
                                           
                                            size_data11=size_data9
                                            Find_guess=1

                                    
                                    
                                    n = int(size_data11, 2)
                                
                                    qqwslenf=len(size_data11)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    
                                    
                                    data2=jl
                                    
                                    size_after=len(jl)
                                    #print(size_after)

                                    
                                    import paq
                                    jl= paq.compress(jl)
                                    

                                    
                                        
                                
                                    size_after=len(jl)
                                    #print(size_after)
                                   
                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                            
                                    assxw=assxw+1
                                    if assxw==1:
                                        assx=10
                                        if assx==10:

                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)

    def cryptograpy_unpack(self):                      
                 if namez=="e":
                    
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                    Portal=2
                    namea="file.W"
                    namem=""
                    namema="?"
                    Deep=0
                 
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)
                    name_cut=""
                    name_cut=len(".bin")
                    nameas=name
                    
                    name_long=len(nameas)
                    nameSS=name[name_long-name_cut:]
                    if nameSS!=".bin":
                        x3=0.0
                        return print(x3)
                        
                    nameas=name[:name_long-name_cut]
                    nac=len(nameas)
                    
                  
                    
                    long=len(nameas)

                    
                    
                    
                    
                    Deep_long=240
                    Deep_long_All=Deep_long*16
                    block_size_long=16
                    Times_compression=1
                    	
                    
                    
                    nac=len(nameas)
                   
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    
                 
                    size_data3=""
                    size_data2=""
              

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        
                        data3 = binary_file.read()

                        data=data3

                    
                        import paq
                        data= paq.decompress(data)
                    

                        
                        
                        

                        if len(data)==0:
                            x4=0.0
                            print(x4)
                            raise SystemExit
                     	

                        s=str(data)
                       
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1
                                            
                                   

                                    if countraz==1:
                                        size_data2=size_data
                            
                                    n = int(size_data2, 2)
                                
                                    qqwslenf=len(size_data2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1

                                    size_data2=size_data

                                    lenf3=len(size_data2)
                                lenf2=len(size_data2)  
                                x4=1
                                if x4==1:

                                    

                                    size_data3=size_data2
                                    size_data10=size_data2
                                   
                                    size_data4=""
                                    size_data7=""
                                    size_data8=""
                                    size_data5=""
                                    size_data6=""
                                    

                                    long_file=len(size_data3)



                                    long_block=16




                                    times_of_times=0

                                    str_find=""



                                    cvf1=1

                                    if cvf1==1:
                                        times_compression=0  









                                        Find_guess=0
                                        while Find_guess!=1:

                                            while  times_of_times!=Times_compression:




                                                        long_block=block_size_long
                                                        long2=len(size_data3)

                                                        blocks=8
                                                        size_compress=63



                                                        block=0

                                                        #b=format(predict,'04b')
                                                        #predict=predict+1
                                                        #if predict==16:
                                                            #predict=0

                                                        long=len(size_data3)
                                                        Times6=0
                                                        size_data1=""
                                                        #print(long)

                                                        while block<long:
                                                                                
                                                                                Zeroes=size_data3[block:block+blocks]
                                                                                if Zeroes=="01101100":
                                                                                	size_data1="00000000"                                                                                                        
                                                                                elif Zeroes=="00000000":
                                                                                	size_data1="01101100"                  
                                                                                else: 
                                                                                
                                                                                	size_data1=Zeroes                        

                                                                                    
                                                                                size_data6=size_data6+size_data1
                                                                                block=block+blocks
                                                                                    #print(block)

                                                        times_compression=times_compression+1

                                                        #print(times_compression)


                                                        size_data3=size_data6

                                                        Where4=0


                                                        #print(len(size_data6))
                                                        size_data6=""
                                                        times_of_times=times_of_times+1

                                            long_after=len(size_data3)
                                            long2=len(size_data3)


                                            size_data9=size_data3
                                            #print(size_data9)





                                            Check_equal=0





                                            long_file=len(size_data10)
                                            long_after=len(size_data9)
                                            #print(long_after) 

                                            if long_file>long_after or long_block<=long_after:

                                                size_data11=size_data9
                                                Find_guess=1
                                      
                                    
                                    n = int(size_data11, 2)
                                    
                                    
                                    qqwslenf=len(size_data11)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    
                                    
                                    
                                    data2=jl

                               
                                    sssssw=len(jl) 
                                  
                                   

                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                                    
                            
                                    assxw=assxw+1
                                    if assxw==1:
                                        assx=10
                                        if assx==10:
                                        	
                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)

  
                  
self=""                                
d=compression()
    
xw=d.cryptograpy_compression()
print(xw)

xw1=d.cryptograpy_unpack()
print(xw1)
