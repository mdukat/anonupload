# anonupload
![logo](https://raw.githubusercontent.com/d3suu/anonupload/dev/doc/pixil-frame-0.png)<br />
An CLI tool for fast file and directories upload on Anonfile, Bayfiles and Megaupload with GPG encryption

## Installation
`chmod +x anonupload.py`<br />
`mv anonupload.py /usr/bin/anonupload`

## Usage
`anonupload -e -g[1-9] -b[1-9] -d <file_or_directory_to_upload>`<br />
 - _-e_   - Encrypts file with your GPG key (see configuration)
 - _-g_   - Gzip's file with given option [1-9]
 - _-b_   - Bzip2 file with given option [1-9]
 - _-h_   - Show help
 - _-d_   - Tar directory, then work on it
 
## Configuration
~~Create file: `$HOME/.config/anonupload`~~<br />
~~Available options:~~<br />
 ~~- _API_ - Api key for server~~<br />
 ~~- _SERVER_ - Server type [anonfile, bayfiles, megaupload]~~<br />
 ~~- _GPG_ - Your GPG name~~<br />
 
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
