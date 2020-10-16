import os
from time import sleep
def Cp(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)


from time import sleep
#a= "What the fuck did you just fucking say about me, you little bitch? Iﾒll have you know I graduated top of my class in the Navy Seals, and Iﾒve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and Iﾒm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. Youﾒre fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and thatﾒs just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little ﾓcleverﾔ comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldnﾒt, you didnﾒt, and now youﾒre paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. Youﾒre fucking dead, kiddo."
def toE(txt):
    x = 0
    b = 1
    msg = []
    curr = ""
    for char in txt:
        if char.lower() in "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(","):
            msg.append(":regional_indicator_"+char.lower()+": ")
        elif char.lower() in "0,1,2,3,4,5,6,7,8,9".split(","): 
            msg.append(":"+"zero one two three four five six seven eight nine".split()[int(char)] + ":")
        elif char.lower() == "10":
            msg.append(":keycap_ten:")
        elif char == " ":
            msg.append("   ")
        else:
            msg.append(char)
    for c in msg:
        x+=len(c)
    if x<2000:
        Cp("".join(msg))
        print("Paste #" + str(b))
    else:
        sleep(3)
        for i in range(0,len(msg)):
            if x+len(msg[i]) < 2000:
                curr+=msg[i]
                x+=len(msg[i])
            else:
                Cp(curr)
                print("Paste #" + str(b))
                b+=1
                sleep(2)
                curr=msg[i]
                x=len(msg[i])
        Cp(curr)
            
        

while True:
    b=input("Message :\n")
    if  b == "":
        break
    else:
        toE(b)
