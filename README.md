# HtmlExtractor

Get raw HTML code, text, or all the hyperlinks/emails present on a website.

# Run

Download the bs4 and main.py file on your devices.
Navigate to the folder using the terminal and execute the file.

To get the HTML code of a website, write "1" and hit enter.
Saves the raw html code as written by the source in a .html file.

To get the text present on a website, write "2" and hit enter.
Uses beautiful soap to extract all the text in the html code ignoring the tags and saves it into .txt file after striping the right and left whitespaces.

To get the hyperlinks present on a webiste, write "3" and hit enter.
EXtracts all the hyperlinks and emails from a website and saves it into .txt file in the following format:

*     link : https://......  

*     email : .......

*     link : https://.........

# Advantages: 

====> The links present in a website are present in the following different forms :

*   https://....

*   //........

*   /........

      But these are extracted and automatically completed to the proper https://.... forms.

====> Saves data in a consistent format to be analyzed easily and conveniently

====> Ignores all href values for ids in the html code.

# Author

Aasher Akhlaque (https://aasherakhlaque.me)
