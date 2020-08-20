# InstaLogin
InstaLogin is a script to login Instagram using Pyhton.

## Usage
Provide **username** and **password** variables with the credentials.

## Details
Instagram requires enc_password which is nothing but #PWD_INSTAGRAM_BROWSER:_{epochTime}_:_{password}_, where {epochTime} represents **the number of seconds passed since epoch** which can be obtained by ```time.time()``` function.
