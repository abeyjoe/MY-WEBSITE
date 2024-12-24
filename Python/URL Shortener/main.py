# pip install pyshorteners and pyperclip
# a python external library for URL shorteners
import pyshorteners

# python prompt for accepting input from user and store into variable name "url"
url = input('Enter the url: ')

# python function to define the URL end point
def shortenurl(url):
    s = pyshorteners.Shortener() # In this case, we will use pyshorteners which is a python external library for URL link skortener
    print("TinyURL is " + s.tinyurl.short(url)) # URL shorteners with tinyurl extention

# call function
shortenurl(url)
