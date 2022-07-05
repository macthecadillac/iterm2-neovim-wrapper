# iTerm2 Neovim Wrapper

A Python `py2app` setup configuration.

## Prerequisites

The following Python libraries must be installed for the build to go forward:

  - `py2app`
  - `pyobjc`
  - `iterm2`
  - `appdir`

Obviously, you'll also need iTerm2 and Neovim to be present on your system for this to work.

## Installation

Download the appropriate prebuilt archive from the releases page. Decompress and move to your application folder.

## Building from source

Check out the repository, then in the directory, run `python3 setup.py py2app`. This will create `Neovim.app` under `dist`. Simply drag and drop the bundle to your application folder.

## Configuration

The bundle will use whatever profile you put in `~/Library/Application Support/Neovim/profile`. It will fail to open if the name of the profile is invalid/unknown to iTerm2. The default profile will be used if this file does not exist.

## Credits

The app icon is taken from [VimR](https://github.com/qvacua/vimr). The file assocation configuration is taken from TextEdit.
