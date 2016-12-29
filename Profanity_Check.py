import urllib

def read_text():
    quotes = open (r"C:\Users\username\Downloads\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    check_profanity(quotes)
    quotes.close()
    

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q= %d"+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("profanity alert!!")
    elif "false"in output:
        print("There are no profane words in this document")
    else:
        print("Could not scan document clearly")


read_text()

