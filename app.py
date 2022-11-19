import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time


def get_image_links(url):
    # read the website url
    response = requests.get(url)
    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(response.text, "html.parser")
    # create a list to store the links
    links = []
    # Iterate over the image tags found
    for img in soup.findAll('img'):
        # extract the link from the img tag and append it to the list
        links.append(img.get('src'))
    # return the list of links
    return links


# Function to create a timestamp as string:
def getTimeStampString():
    return str(time.time()).split('.')[0]


# function to create a folder with todays date-time
def createFolder():
    folder = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # if the folder doesn't exist, create it
    if not os.path.exists(folder):
        os.makedirs(folder)
    # change the working directory to the new folder
    os.chdir(folder)



# Create a function that will accept a list of links and download the images
def download_images(links):
    createFolder()
    for link in links:
        # read the image binary
        response = requests.get(link)
        # extract the image name from the link
        name = link.split('/')[-1]
        # open a file in the write binary mode and write the image binary
        with open(getTimeStampString()+'_' + name, 'wb') as f:
            f.write(response.content)


imagesList = get_image_links(
    'THE URL TO THE PAGE WHICH CONTAINS THE IMAGES')
download_images(imagesList)