import os
import sys

import iterm2
import AppKit


async def main(connection):
    try:
        fnames = ' '.join([fname.replace(' ', '\\ ') for fname in sys.argv[1:]])
    except IndexError:
        fnames = ''
    shell = os.environ['SHELL']
    command = '{} -c "nvim {}"'.format(shell, fnames)
    await iterm2.Window.async_create(
        connection,
        command=command,
        # profile='Default'
    )


# Launch iTerm if it is not already running
workspace = AppKit.NSWorkspace.sharedWorkspace()
if ' '.join(str(s) for s in workspace.runningApplications()).find('com.googlecode.iterm2') < 0:
    workspace.launchApplication_('iTerm')

# Passing True for the second parameter means keep trying to
# connect until the app launches.
iterm2.run_until_complete(main, True)

# Bring app forward
workspace.launchApplication_('iTerm')