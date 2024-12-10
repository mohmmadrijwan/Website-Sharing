Step 1 : The Website Sharing automation is develop using python, robotframework, selenium, beautifulsoup4, pillow etc libraries and
        it uses the Variety.com for taking latest news articles and download their latest content and show them on user webpage i.e.
        index.html.

Step 2 : Logic is simple there are required packages.txt file where you can find all the required packages you can simplly install them 
        if you have install python, using pip command you can install other packages please check and copy paste each command on cmd
        'required packages.txt'

Step 3 : After successfully install all the packages please check for the 'run.py' file you need to simplly run it 'python run.py'. it
        will run the main.robot file in scr folder it help us to debug get output files in result folder log files and run the script
        till infinite while loop

Step 4 : If all the packages are install correctly it will open chrome browser and open Variety.com news feed for checking latest news

Step 5 : It takes the first news from list of 'Variety.com' and compare its title with previously store title in 'testData/data.json'
        file. data.json stores the caption of article, title, and shortern shortUrl

Step 6 : If title match with data.json['title'] then it will continue from the begining i.e. Step 3 refresh page till it didnt find any
        new article.

Step 7 : If any new article is there then it will open article and get all the paragraphs and image from that paragraph

Step 8 : The paragraph is used to create 200 word caption with shortern url using TinyUrl api and image will be stored in img folder

Step 9 : caption and shortern url will be stored in data.json in testData folder

Step 10 : createHtml.py file is used to create a html page where showing image and caption with shortern url to original article. It
        takes values from data.json i.e caption and shortern url and image from img folder.
