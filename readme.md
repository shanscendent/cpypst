# cpypst
Small python tool to copy paste text between different machines easily via the cli. Uses a http server, so it is currently possible to copy from the browser.

## Requirements
Python 3.4+

## Installation
1. I recommend installing this in a virtual environment. `venv`
2. After cloning, cd into the cpypst folder, then
3. Run `pip install .`
4. After it's finished, should be available to use via
`python -m cpypst`
- Optional: run `install.sh` to set an alias if you desire, replacing the above with just `cpypst`.

## Usage
To use, spawn a cpypst server on a machine using `screen` or `tmux`, then set its IP address on other machines you wish to copy/paste to and from.
The server will refresh the cached string on every `copy` command, and `paste` will print it to `stdout`.
- `cpypst copy <text>` - Copy text to server
- `cpypst paste` - 'Paste' text from server to stdout, alternatively, `curl <host>`
- `cpypst set <host>` - Sets IP address of cpypst server. Persistent.
- `cpypst run` - Run cpypst server on machine, web interface for copying on  port `8080`

## Notes
- NO SECURITY, do __NOT__ expose to internet, use only on your LAN
- Very haphazardly thrown together, look forward to the next iterations

## Motivation
Ever get frustrated after trying to copy and paste text between different machines/vms in your lan via vnc clients that don't support copy and paste? Enter cpypst.

## To implement
- Tidy up code
- No error codes for unconnectable server yet
- Remove 'placeholder' text if nothing has been copied yet
- Add proper exit handling for the server
- Figure out how to have arguments on the same level as subcommands
- Figure out what the proper POST response is (enabling `curl -d`)
- Save last `n` copies, currently only saved in memory
- Shell script for installing/aliases
- Add ability to change port
- Accept string from pipe