#!/usr/bin/python
import xml.etree.ElementTree as ET
import httplib as http
import os
feed_host = "showrss.karmorra.info";
feed_url = "/rss.php?user_id=87355&hd=null&proper=null&namespaces=true"
log_file = "/etc/btscripts/torrent.log"
log_data = ""
print os.getcwd()

def check_log(log, torrent):
    for line in log:
        if(line == torrent):
            return 1;
    
    return -1;

try:
    f = open(log_file, 'r')
except:
    print "No log found\n"
else:
    log_data = f.readlines()
    f.closed

#connection = http.HTTPConnection(feed_host)
#connection.request("GET",feed_url)

#response = connection.getresponse()
#feed_xml = response.read()
#connection.close()

feed_data = ET.parse("test.xml")
#feed_data = ET.fromstring(feed_xml)
feed_channel = feed_data.getroot().find("channel")

with open(log_file, 'a+') as f:
    for child in feed_channel:
        if child.tag == "item":
            torrent_link = child.find("link").text+"\n"
            
            if(check_log(log_data,torrent_link) == -1): 
                #doesn't exists, download
                print "download added"
                #system()
                
                # and add to log
                f.write(torrent_link)

f.closed

