# Cyber Security Project 1

1. Broken Access Control
2. Cryptographic Failures
3. Injections
4. Identification and Authentication Failures
5. Server Side Request Forgery

## Broken Access Control
### Person pages
Pages are accessible without login via url. ```http://localhost:5000/person/<int:id>``` <br>
Pages are easy to iterate because they are numbered sequentially. <br>
This enables malicious automated data collection. <br>

## Cryptographic Failures
### Register and Login
User creation uses md5 hashing for passwords which has been found to suffer from extensive vulnerabilities.
### HTTP
HTTP does not encrypt data and thus attacker can monitor network traffic

## Injections
### SQL | Login
Password check can be avoided by adding ```'--``` behind every username when loggin in. <br>
This comments out rest of SQL statement preventing password comparison.
Further more using f-string instead of bind variables allows for other harmfum inputs.
### XSS | html
Browsers automatically escape special characters in input fields of html files. <br>
Using .j2 file ending disables automatic character escaping. <br>
```<IMG """><SCRIPT>alert("XSS")</SCRIPT>"\>``` Will work on person page when sending a message.
#### CSRF
```<img src=/change?secret=malicious_message&user_id=1 onerror=""></img>``` changes victims secret.

## Identification and Authentication Failures 
- Permits automated attacks such as credential stuffing
- Permits brute force or other automated attacks
- Permits default, weak, or well-known passwords
- Uses plain text, encrypted, or weakly hashed passwords data stores
- Has missing or ineffective multi-factor authentication

## Server Side Request Forgery
Application uses mock up API services to handle language configuration. <br>
User can manipulate URL and trick server to do request without knowing the API KEY.
Bad design allows user to read server response from html.

# How to install
Python3 and Git are prerequisites. A virtual environment such as venv is recommended. <br>
### Python & Flask
[Python Guide](https://cybersecuritybase.mooc.fi/installation-guide)
Try this only if you are not able to install Flask with later instructions.
```$ pip install flask```
If previous methods fail try ```sudo apt install python3-flask``` on Linux <br>
pip on Windows try [guide](https://www.liquidweb.com/kb/install-pip-windows/) <br>
pip on Mac try [guide](https://phoenixnap.com/kb/install-pip-mac)

### venv
You can use venv after cloning this repo with command ```$ python3 -m venv venv``` followed by ```$ source venv/bin/activate```. <br>
Both executed in your project directory. You can exit venv with ```$ deactivate```<br>
### repo
Go to a directory of your liking and enter command ```$ git clone git@github.com:EternalAzure/Cyber-Security-Project-1.git``` <br>
This will create a subdirectory called Cyber-Security-Project-1 as your project directory. <br>
Move to the project directory and enter command ```$ pip install -r requirements.txt```. <br>
This should install all required dependencies including Flask and multipledispatch. <br>

# How to use
## Set up
Once installed and while in the project directory enter command ```$ sh create_database.sh```. <br>
This will set up sqlite3 database with schema.sql. <br>
If you need to reset the database use command ```$ sh reset_database.sh```. <br>

## Run
Use command ```$ flask run``` to run the server. Go ```http://localhost:5000/``` with your browser to use the app.
You can terminate the process with ```$ ^C```

## SSRF
Get familiar with the app before trying SSRF. For this use a regular web browser.
### Cool option
You can manipulate the language configuration request with [Burp Suite](https://portswigger.net/burp/releases/professional-community-2021-9-1?requestededition=community). <br>
To run the installer go to Downloads and run something like ```$ sh burpsuite_community_linux_v2021_9_1.sh``` CHECK YOUR VERSION! <bt>
When launching Burp Suite choose Temporary project and then defaults. <br>
Burp Suite community edition is free to use and does not require registeration. Do the short tutorial that comes with the download. <br>
In case you missed or skipped the tutorial go to <b>proxy</b> tab on Burp Suite and there click to open embedded browser. <br>
Go to localhost:5000/ <br>
Burp Suite captures requests and lets you manipulate them before <b>forwarding</b> them. <br>
With Burp Suite browser log in to an account and on that personal page click to change language. Burp suite will capture the request and show you the following view.
<img src="https://github.com/EternalAzure/Cyber-Security-Project-1/blob/main/pictures/burp%20suite.png"  />
Replace the first line with ```GET /language?api=%2Fapi%2Fadmin&ref=%2Fperson%2F1 HTTP/1.1``` to access ```/api/admin``` and thus execute SSRF. <br>
You will see ```Kieli:mock response from /admin``` on your personal page.

### Easy option
Alternatively you can use ssrf.rest with VS Code to access ```/api/admin``` and thus execute SSRF. <br>
You will see 
```
        ...
<form action="/language" method="GET">
        Kieli:mock response from /admin<br>
        ...
```
in VS Code. <br>
OR <br>
You can be extra boring and simply write ```http://localhost:5000/language?api=/api/admin&ref=/person/1``` to browser.
Note that POST methods would not get through like this.
