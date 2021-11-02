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
This comments out rest of SQL statement preventening password comparison.
Further more using f-string instead of bind variables allows for other harmfum inputs.
### XSS | html
Browsers automatically escape special characters in input fields of html files. <br>
Using .j2 file ending disables automatic character escaping. <br>
```<IMG """><SCRIPT>alert("XSS")</SCRIPT>"\>``` Will work on person page when sending a message.
### CSRF
```<img src=/change?secret=thanks&user_id=2 onerror=""></img>``` changes victims secret.

## Identification and Authentication Failures 
- Permits automated attacks such as credential stuffing
- Permits brute force or other automated attacks
- Permits default, weak, or well-known passwords
- Uses plain text, encrypted, or weakly hashed passwords data stores
- Has missing or ineffective multi-factor authentication

## Server Side Request Forgery

