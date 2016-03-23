import re

def time_convert(pretime):
    #format: #D#H#M
    timeArray=re.split("d|h|m",pretime,maxsplit=3,flags=re.IGNORECASE)
    counter=0
    intTimeArray=[0,0,0]
    print("Time Array:"+str(timeArray))

    if len(timeArray)==4:
        for counter in range(0,3):
           
            if re.match("[0-9]*",timeArray[counter]):
                #print(timeArray[counter])
              
                intTimeArray[counter]=int(timeArray[counter])
                #print(intTimeArray[counter])
        print("Int Time Array:"+str(intTimeArray))
        return 60*(intTimeArray[2]+60*(24*intTimeArray[0]+intTimeArray[1]))

    print("Invalid Format?")
    return -1


    #Returns number of seconds.
#print("0d5h30m:"+str(timeConvert("0d5h30m")))
#print("5h30m:"+str(timeConvert("5h30m")))
#print("1d5h30m:"+str(timeConvert("1d5h30m")))