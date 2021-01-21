# BuiltIn-Manager
## Questions
### What is BuiltIn Manager?
BuiltIn Manager is an easy to use program for managing installed BuiltIn plugins in your Roblox Studio installation.
### What are BuiltIns?
A BuiltIn is a plugin that has access to more things in Roblox Studio than regular plugins. They are usually built into Roblox Studio, hence the name. These are usually plugins provided by Roblox.
### Why should I use this tool?
Sometimes people find regular plugins to be a bit limiting. Because of this, some developers like to run their plugins as BuiltIns. However, this isn't an easy process. You need to enable a flag in Studio to allow BuiltIns not provided by Roblox to run, and then you need to add those plugins directly into a folder in Roblox Studio's installation folder. Using this tool, that process is made much easier.
### How do I use this tool?
Using the tool is easy!
- Adding plugins
  Simply press the "Add plugin" button and select the plugin file provided to you by the developer of the plugin!
- Removing plugins
  Select the plugin you want to remove and press the "Remove plugin" button!
  `NOTE: This only works for plugins not provided by Roblox! Plugins provided by Roblox will say "Yes" in the "Verified" column.`
## Building
`This is for anyone who wants to build the tool themself. If you'd rather jump right in, navigate to Releases and download the exe file in the latest release.`

Building the tool is simple.
1. Install [python](https://www.python.org/). (make sure you install pip as well!)
2. Make sure that all the modules imported in `builtinmanager.py` are installed! (Run `pip install <module>` in command prompt.)
3. Install PyInstaller with pip. `pip install pyinstaller`
4. Download the repository as a zip, an extract it.
5. Open command prompt and navigate to where you extracted the zip file.
6. Run `pyinstaller builtinmanager.py -w --clean --onefile`
A few folders will appear in the extracted zip file. One of these folders will be named "dist". Open this folder, and there is your built exe.
`NOTE: Windows Defender may block parts of PyInstaller as well as your built exe! To fix this, simply allow these files whenever they are detected and rebuild.`
