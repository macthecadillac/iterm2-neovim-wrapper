# iTerm2 Neovim Wrapper

A Python `py2app` setup configuration.

## Prerequisites

The following Python libraries must be installed for the build to go foward:

  - `py2app`
  - `pyobjc`
  - `iterm2`

Obviously, you'll also need iTerm2 and Neovim to be present on your system for this to work.

## Build and install

Check out the repository, then in the directory, run `python3 setup.py py2app`. This will create `Neovim.app` under `dist`. Simply drag and drop the bundle to your application folder.

A note on profiles: if you use a custom profile for Neovim then you should uncomment the corresponding line in `launch_neovim_in_iterm2.py` and replace "Default" with the name of your profile before building the app bundle.

## Credits

The app icon is taken from [VimR](https://github.com/qvacua/vimr). The file assocation configuration is taken from TextEdit.