import time
my_time=int(input("enter your number in seconds :"))

for counter in range(my_time,0,-1):#forloop use kiya for specific range tk loop chalany ky liya user sy input lyn gy aur phr otny time ka counter chly ga 
    sec= counter%60
    minutes=int(counter/60)
    hours=int(counter/3600)
    print(f"{hours:02}:{minutes:02}:{sec:02}")
    time.sleep(1)#time.sleep use hota delay ky liya kitna delay chahiya output ma 

print("Times up")
