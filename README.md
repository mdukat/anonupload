# anonupload
![logo](https://raw.githubusercontent.com/d3suu/anonupload/dev/doc/pixil-frame-0.png)<br />
An CLI tool for fast file and directories upload and download on Anonfile, Bayfiles and Megaupload with GPG encryption

## Installation
`$ chmod +x install.sh`<br />
`# ./install.sh` or `sudo ./install.sh`

## Usage
`anonupload -e -h -g[1-9] -b[1-9] -s [server] -a [api_key] -d [file_name/directory_name]`<br>
-e - encrypt using GPG<br>
-h - shows this help<br>
-g[1-9] - gzip file<br>
-b[1-9] - bzip2 file<br>
-d - use when you want to tar whole directory<br>
-s [server] - use different server (bayfiles, anonfile, megaupload)<br>
-a [api_key] - api key on-the-go<br><br>
`anonget [link]`<br>
[link] - link to file on bayfiles, anonfile or megaupload to download

 
## Configuration
Simply use `python3 config.py`, easy as that!

### Example configuration
`API:abcdef123456790`<br />
`SERVER:anonfile`<br />
`GPG:d3suu`

## HURR DURR IT'S USING OS.SYSTEM, WHY NOT BASH?!?!?!?!?
Computing hour costs less than Programmer hour. And it (should) work.

## See very cool workflow i made using draw.io!
![Cool!](https://raw.githubusercontent.com/d3suu/anonupload/dev/doc/Anonupload%20workflow.png)

## Offtopic
Check `doc` directory, there's some stuff about development. Also feel free to help and improve this tool.
