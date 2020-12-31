# mclighting-hotkey
A python/windows script for toggling a mclighting-controlled LED strip with a keyboard shortcut

## Windows Setup
You must leave the invoke.bat script in the same directory as your python file. Edit your PYTHONPATH accordingly, if you don't have PYTHONPATH in your environment.

On Windows 10, you can automatically invoke a batch script using a keyboard shortcut. To do this, right click the batch file, and choose send to --> desktop (create shortcut).

Right click on the shortcut on the desktop, and choose properties. Click inside the shortcut key window, and press the key corresponding to the shortcut. In this case, I've mapped F13 to a macro key on my NIBBLE, and I'm using that as the hotkey. Choose OK.

Pressing the chosen hotkey will now launch the batch script and automatically call the linked python script!