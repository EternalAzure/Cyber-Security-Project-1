# Cyber Security Project 1

1. Broken Access Control
2. Cryptographic Failures
3. Injections

## Broken Access Control
### Person pages
Pages are accessible without login via url. ```http://localhost:5000/person/2``` <br>
Pages are easy to iterate because they are numbered sequentially. <br>
This enables automated data collection. <br>

## Cryptographic Failures
### Register and Login
User creation uses md5 hashing for passwords which has been found to suffer from extensive vulnerabilities.
### HTTP
HTTP does not encrypt data and thus attacker can monitor network traffic

## Injections
### Login
Password check can be avoided by adding ```'--``` behind every username. This comments out rest of SQL statement.
