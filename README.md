# Coding Pirates: Python 🐍🏴‍☠️

Code for the Coding Pirates Python module.

**For instructors and parents:** please install the following on the child's computer before the first class:

- [ ] Python
- [ ] VS Code
- [ ] The Python extension for VS Code
- [ ] The code from this project

## Install Python

Any **Python 3.10 or newer** works. Use the official Python from [python.org](https://www.python.org/downloads/) (or the Microsoft Store on Windows). You don't need Anaconda.

> **Already have Python?** Open a terminal and type `python --version` (Windows) or `python3 --version` (Mac). If it says 3.10 or higher, skip to [VS Code](#vs-code).

- **Windows:** follow Microsoft's guide [Python on Windows for beginners](https://learn.microsoft.com/windows/python/beginners). The "Manual installation" tab is the easiest.
- **Mac:** follow [How to Install Python Using the Official Installer on macOS](https://realpython.com/installing-python/#macos-how-to-install-python-using-the-official-installer) (2 short steps). There's no install manager on Mac, so Python won't update itself. That's fine for this course.

### VS Code
1. Install [VS Code](https://code.visualstudio.com/), if it isn't installed already.
2. Install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) (search for **Python** by **Microsoft** under Extensions).
3. **If there are several Python versions on the computer:** open a `.py` file, click the Python version in the bottom right corner of VS Code, and pick the newest one.

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

Make sure the project folder is open in VS Code (see above), and the python extension is installed. Then click on the play button in the top right.

You should see `Hello!` followed by some information about a superhero in the bottom of the screen. 🎉

## Troubleshooting

| Problem | Fix |
|---|---|
| Windows: `python` opens the Microsoft Store or says "not recognized" | Check that the **Python install manager** is installed. Then click Start, open **Manage app execution aliases**, and make sure the **Python** aliases are turned on. Restart VS Code afterwards. |
| Windows: `python` runs an old version | An older Python is also installed. Go to **Settings → Apps → Installed apps**, search for **Python**, and uninstall the old versions. |
| VS Code runs the wrong Python version | Click the Python version in the bottom right corner of VS Code and pick the newest one. |
| Mac: a popup asks to install "command line developer tools" | Python from python.org isn't installed yet. Close the popup and follow the Mac steps above. |
