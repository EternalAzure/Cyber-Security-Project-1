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
Python3 is prerequisite. A virtual environment such as venv is recommended. <br>
Go to a directory of your liking and enter command ```$ clone git@github.com:EternalAzure/Cyber-Security-Project-1.git``` <br>
This will create a subdirectory called Cyber-Security-Project-1 as your project directory. <br>
Move to the project directory and enter command ```$ pip install```. <br>
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
### Cool option
You can manipulate the language configuration request with [Burp Suite](https://portswigger.net/burp/releases/professional-community-2021-9-1?requestededition=community). <br>
Burp Suite community editin is free to use and does not require registeration. Do the short tutorial that comes with the download. <br>
Burp Suite captures requests and lets you manipulate them before forwarding them. <br>

### Easy option
Alternatively you can use ssrf.rest with VS Code.
