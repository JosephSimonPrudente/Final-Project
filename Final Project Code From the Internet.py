from time import time # record the time 

# calculate the accuracy of input prompt
def tperror(prompt):
    global inwords 

    words = prompt.split()
    errors = 0

    for i in range (len (inwords)):
        if i in (0, len(inwords)-1):
            if inwords[i] == words [i]:
                continue
            else:
                errors = errors + 1
        else: 
            if inwords[i] == words[i]:
                if (inwords[i+1] == words[i+1]) & (inwords[i-1] == words[i-1]):
                    continue
                else:
                    errors += 1 
            else:
                errors += 1
    return errors

# calculate the speed of typing words per minute 
def speed(inprompt, stime, etime):
    global time 
    global inwords 

    inwords = inprompt.split()
    twords = len(inwords)
    speed = twords / time 

    return speed 

# calculate hte total elapsed time 
def elapsedtime(stime, etime):
    time = etime - stime # etime is the end time and stime is the start time 
    return time 

# this was the paragraph which you have you have to type to check your speed
if __name__ == '__main__':
    prompt = "We may easily improve our writing skills by using a random paragraph generator. One of the best way to develop writing skills and English is by writing or reading. This tool is simple to use and you can use it anywhere anytime."
    print()
    print("***************************************************TYPE THIS******************************************")
    print()
    print(prompt)

#Checking to input   
    print()
    input("*****Press enter when your ready to check your speed*****:")
    print()

# recording time for input 
    stime = time()
    inprompt = input()
    etime = time()

# collect all the imformation returned by functions
    time = round(elapsedtime(stime,etime),2)
    speed = speed(inprompt,stime,etime)
    errors = tperror(prompt)

# printing all the required data to see result
    print("=================================================================")
    print("total time elapsed:", time ,"Seconds")
    print("=================================================================")
    print("Your average typing speed was ", speed , "words per minute (w/m)")
    print("=================================================================")
    print("with the total of ", errors, "errors")

#https://www.youtube.com/watch?v=AkKFLes-_VI&list=PLpp8-k7G_6Y3Wj1suZQ-9lATFzFuGw93x&index=8

