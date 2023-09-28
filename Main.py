from time import sleep
from WebScraper import geturl


print("╔"+"═"*70+"╗"+"\n"+"║"+" "*30+"WEB SCRAPER"+" "*29+"║\n"+"╚"+"═"*70+"╝")

importantWords = input("\nEnter important words (Using a space like separator): ").replace(" ", "+")
exactWords= input("\nEnter exact words (Using a space like separator): ").replace(" ", "+")
otherWords= input("\nEnter any words (Using a space like separator): ").replace(" ", "+")
excludeWords= input("\nEnter words to exclude (Using a space like separator): ").replace(" ", "+")

while (True):

    language= input("\nEnter a number to select lenguage: English(1) or Spanish(2): ")
    if (language=="1"):
        language="lang_en"
        break

    elif(language=="2"):
        language="lang_es"
        break

    else:
        print("Enter a correct number")

domain= input("\nEnter the domain for search: ")

number= input ("\nEnter the number of queries: ")

number= int(number)

while (True):

    azure= input ("\nEnter a number to activate Azure service: Yes(1) or No(0): ")
    if (azure=="1"):
            azure=True
            break

    elif(azure=="0"):
            azure=False
            break

    else:
            print("Enter a correct number")


query=("https://www.google.com/search?as_q="+importantWords
    +"+-filetype:pdf"
    +"&as_epq="+exactWords
    +"&as_oq="+otherWords
    +"&as_eq="+excludeWords
    +"&lr="+language
    +"&cr=countryCO&as_sitesearch="+domain
    +"&start=")

geturl(query, number, azure)