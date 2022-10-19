# import urllib
# use the urllib.request to get the data
# write the function that takes the url and return the response 

import urllib.request as urllib


def main(url):
    print("Checking connectivity ")
    
    response = urllib.urlopen(url)
    print("Connected to" , url, "succesfully")
    print("The response code was: ", response.getcode())

print("This is a site connectivity checker program")
input_url = input("Input the url of the site you want to check: ")

main(input_url)