import webbrowser
import time

print("Program Start Time: "+time.ctime())
s=1
for x in range(1,3):
    print ("Loop sequence number:%d" % s)
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/")
    s=s+1
