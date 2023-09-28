import re
import unidecode
from Constants import KeyWords_Address, KeyWords_Phone


def searchData (txt):
    txtstring=(unidecode.unidecode(txt)).lower()
    if len(txtstring.split(":"))<2:
        data = re.findall("\S+@.+\.\S+", txtstring)
        if len(data)>0 :
            return data[0], "email"
        data = re.findall("\S+@.+\.\S+\.\S+", txtstring)
        if len(data)>0 :
            return data[0], "email"
    if len(txtstring.split("+"))<2 or len(txtstring.split(":"))<2:
        for i in KeyWords_Address:
            data = re.findall("^"+i+"\W*.+\d+.+",txtstring)
            if len(data)>0:
                return data[0], "address"
            data = re.findall(".+("+i+"\W\d+.+\d+.*\d*).+",txtstring)
            if len(data)>0:
                return data[0], "address"
    for i in KeyWords_Phone:
        data = re.findall("^"+i+".*:(.*\d+.+\w).*",txtstring)
        if len(data)>0:
            return data[0], "phone"
        data = re.findall(".*(\W\d{2}\s*\d\W\s*\d{3}\s*\d{4}).*", txtstring)
        if len(data)>0: 
            return data[0], "phone"
        data = re.findall(".*(\W{2}\d{2}\W\s*\d{10}).*", txtstring)
        if len(data)>0: 
            return data[0], "phone"
        data = re.findall(".*phone=(\d+).*", txtstring)
        if len(data)>0: 
            return data[0], "phone"
        data = re.findall(".*(\d{3}\s\d{3}\s\d{4}).*", txtstring)
        if len(data)>0: 
            return data[0], "phone"
        if len(txtstring.split(" "))<2 and len(txtstring.split("/"))>1:
            data = re.findall("(.+facebook\D+)", txtstring)
            if len(data)>0: 
                return data[0], "social media"
            data = re.findall("(.+instagram.+)", txtstring)
            if len(data)>0: 
                return data[0], "social media"
            data = re.findall("(.+linkedin.+)", txtstring)
            if len(data)>0: 
                return data[0], "social media"
    return "", ""

      
def cleanUrl(result, vector, max):
    if len(vector) <= max:
        url="https://"+result.split("/")[2]
        if url not in vector:
            vector.append(url)
    return(vector)
        

