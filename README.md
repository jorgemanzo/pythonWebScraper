# Newegg.com WebScraper
### A web scraper using Python3, BeautifulSoup and Selenium

##### So why did I make it?
Because I got tired of writing in C/C++ and wanted to have some fun with python. That and
Im looking to upgrade my PC parts and want to find a decent price for a graphics card on Newegg.com

##### Why in python?
Uhhhh.... Because its easier. A lot of the groundwork is already in place which makes development easier and faster. Though Im sure python is much slower than a C/C++ implementation of this.

##### How did I make it?
I used a few things on top of just python3. I started with looking up a youtube [video](https://www.youtube.com/watch?v=XQgXKtPSzUI&t=1168s) on how to scrape information off of websites with python. Turns out this video actually implemented what I wanted using BeautifulSoup. But I wanted to build on top of that. So I then looked up a video on [python website queries](https://www.youtube.com/watch?v=EELySnTPeyw). This lead me to using selenium to automate opening up Firefox, going to Newegg.com and sending it a search for whatever I want. Thats the idea anyway.

##### Does it work?
Yes. .... kind of.  There are a few issues with it currently, but it can function enough to be operable.

##### How do I use it? 
You need a few things. I used it on Ubuntu. One, you need [geckdriver for Firefox](https://github.com/mozilla/geckodriver/releases/tag/v0.19.1). Then you need to make sure your $PATH contains the path to the driver. For example `export PATH=$PATH:/home/path_to/geckodriver` and paste that into your Terminal. Then you need to install [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup) and [Selenium](https://pypi.python.org/pypi/selenium) for python3. I just used pip. 

So now you should be ready to use it. Open terminal in the directory where the files are downloaded. Then you must run the program command-line arguments in this way: `python3 pythonScraper.py <FILENAME> <SEARCHTERM>`

So for example I would run this program to scrape Newegg for "GTX" graphics cards and to store the data found in the a file called "Nvidia.csv". You must output to a .csv file. So I would type and execute `python3 pythonScraper.py Nvidia.csv GTX` in my terminal. 

Once executed, the program will open Firefox, search your search term, and then close. Then the terminal will process the html from the website and output its findings to the terminal and to your output file. The output file can be opened in something like LibreOffice Calc and looks like this:

![NVIDIA.csv](https://i.imgur.com/oGIXrwz.png)

The scrape will collect the product's brand, the product's title, the cost, shipping cost, its rating, and number of reviews.

As you may notice there are a few bad eggs though (pun intended). Results that have no ratings or reviews will get reviews of -1. Results that have no shipping cost or price also get shipping cost and cost of -1.

Some results are just oddball in general. The PNY Technologies result for example must have its html entry different than most others from EVGA, ZOTAC, ect. That is because the function to search through the html of the result webpage follows a general pattern that can be seen in most results. However it appears that PNY Technologies result html is just different that of others and needs to be accounted for. 

Other issues include search results returning bundles of components with the search term in it. For example searching for "GTX" may return a bundle of PC components such as a motherboard, ram and some kind of GTX graphics card. 

### This will break the program!

That is because the patterns in html differ from bundles and single component results. 
