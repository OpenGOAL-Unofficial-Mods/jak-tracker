# jak-tracker
Auto-Tracker for OpenGOAL Jak 1 (Randomizer)

Piggybacking on the work done to support LiveSplit autosplitter, this program will scan OpenGOAL memory and display which Power Cells you've collected in your current game. 

- Windows/antivirus software may flag this program as a risk, we promise it is safe to run. This project is open source and you can audit the source code if you want to verify yourself - we simply use `pyinstaller` to package it up into an exe.
- The program may load for ~10 seconds on startup, as it takes some time to scan through OpenGOAL memory
- Tracker UI Customization!
  - **Icon layout** is defined in `layout.yaml`:
    https://github.com/OpenGOAL-Unofficial-Mods/jak-tracker/blob/9eb61a0eb2fac0d9a3eaee9f8de220146480f125/layout.yaml#L5-L22
  - **Colors/sizing/etc** are defined in `prefs.yaml`
    https://github.com/OpenGOAL-Unofficial-Mods/jak-tracker/blob/ce740918c70e920f618d532990a29f70d570a5db/prefs.yaml#L3-L15
  - **Custom icons** can be used - just replace the corresponding PNG file(s) in the `icons` subfolder
  - *Both of the above YAML files and the entire `icons` subfolder should live in the same folder as `JakTracker.exe`*

Download the latest release `JakTracker.zip` from [here](https://github.com/OpenGOAL-Unofficial-Mods/jak-tracker/releases/latest)
