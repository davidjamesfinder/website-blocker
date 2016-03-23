import sys
import time

#Four different input arguments:
    #block <URL>
    #unblock <URL>
    #block-file <FILE-NAME>
    #unblock-all

print(str(sys.argv))




def lessthanTime(endTime):
    if endTime<time.time():
        return false
    return true


def blockSite(URL):
    #Blocks a website
    if url.startsWith("http"):
        url=url.split("//")[2]
    if url.startsWith("www"):
        shortenedURL=url.split(".")[2]
    else:
        shortenedURL=url
        url="www."+url
    if not siteBlocked(shortenedURL):
        with open("/etc/hosts","a") as hostsFile:
            hostsFile.write("127.0.0.1 "+shortenedURL)
    #if website starts with www
        #block removing "www."URL
    #else, block for with www and current URL
def siteBlocked(URL):#Determines if a website has been blocked already
    hostsFile=open("/etc/hosts")
    for line in hostsFile:
        if (URL in line)and ("127.0.0.1" in line) and "#" not in line:
            hostsFile.close()
            return true
    hostsFile.close()
    return false 
def unblockAllSites():
    with open("/etc/hosts","r+") as hostsFile:

        for line in hostsFile:
            if("127.0.0.1" in line and "#" not in line and "localhost" not in line):
                line="#"+line

def removeCommentedSites():
    with open("/etc/hosts","r+") as hostsFile:
        newHostsFile=file.
        for line in hostsFile:
            if("127.0.0.1" in line and line.startsWith("#")):
                ##Remove LIne
