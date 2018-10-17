# anonupload
An CLI tool for fast file upload on Anonfile, Bayfiles and Megaupload

## Installation
`chmod +x anonupload.py`<br />
`mv anonupload.py /usr/bin/anonupload`

## Usage
`anonupload -e -g[1-9] -f <file_to_upload>`<br />
 - _-e_   - Encrypts file with your GPG key (see configuration)
 - _-g_   - Gzip's file with given option [1-9]
 - _-f_   - File to upload (WIP - remove this argument, use last arg as file)
 
## Configuration
Create file: `$HOME/.config/anonupload`<br />
Available options:<br />
 - _API_ - Api key for server
 - _SERVER_ - Server type [anonfile, bayfiles, megaupload]
 - _GPG_ - Your GPG name

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
