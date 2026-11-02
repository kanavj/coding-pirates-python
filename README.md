# Coding Pirates: Python 🐍🏴‍☠️

Code for the Coding Pirates Python module.

**For instructors and parents:** please install the following on the child's computer before the first class:

- [ ] Python
- [ ] VS Code
- [ ] The Python extension for VS Code
- [ ] The code from this project

## Install Python

### Windows
1. Go to [python.org/downloads](https://www.python.org/downloads/) and click **Download Python**.
2. Open the installer.
3. ⚠️ **Tick "Add python.exe to PATH"** at the bottom of the first screen.
4. Click **Install Now**.
5. Open a terminal (search for **PowerShell**) and check that it works:
   ```
   python --version
   ```

### Mac
1. Go to [python.org/downloads](https://www.python.org/downloads/) and click **Download Python**.
2. Open the `.pkg` file and click through the installer.
3. Open **Terminal** and check that it works:
   ```
   python3 --version
   ```

### VS Code
1. Download and install VS Code from [code.visualstudio.com](https://code.visualstudio.com/), if it isn't installed already.
2. Open VS Code and go to **Extensions** (the four squares on the left).
3. Search for **Python** and install the one by Microsoft.

## Get the code

1. Go to the project's GitHub page: **PROJECT-URL**
2. Click the green **Code** button, then **Download ZIP**.
3. Unzip the file:
   - **Windows:** right-click the ZIP in your Downloads folder, choose **Extract All...**, then click **Extract**. ⚠️ Don't just double-click it. Windows then only *shows* the files inside the ZIP, and the code won't run from there.
   - **Mac:** double-click the ZIP in your Downloads folder. A normal folder appears next to it.
4. Move the unzipped `coding-pirates-python` folder (the name may end in `-main`) somewhere easy to find, like the **Desktop**.
5. Open VS Code, choose **File → Open Folder...**, and select that folder.
6. If VS Code asks **"Do you trust the authors of the files in this folder?"**, click **Yes, I trust the authors**.

You should now see the `module1` folder in the left sidebar of VS Code.

## Check that everything works

Make sure the project folder is open in VS Code (see above), then open a terminal (**Terminal → New Terminal**) and type:

```
cd module1
python3 1-hello.py
```

On Windows, use `python` instead of `python3`.

You should see `Hello!` followed by some information about a superhero. 🎉

## Troubleshooting

| Problem | Fix |
|---|---|
| Windows: `python` opens the Microsoft Store or says "not recognized" | Reinstall Python and make sure **Add python.exe to PATH** is ticked. Then restart VS Code. |
| Mac: a popup asks to install "command line developer tools" | Python from python.org isn't installed yet. Close the popup and follow the Mac steps above. |
| `No such file or directory` | The terminal is in the wrong folder. Make sure you opened the project folder and ran `cd module1`. |
