# jak-tracker
Auto-Tracker for OpenGOAL Jak 1 (Randomizer)

Download the latest release `JakTracker.zip` from [here](https://github.com/OpenGOAL-Unofficial-Mods/jak-tracker/releases/latest)

Piggybacking on the work done to support LiveSplit autosplitter, this program will scan OpenGOAL memory and display which Power Cells you've collected in your current game. 

<img width="250" alt="image" src="https://user-images.githubusercontent.com/2515356/204374691-a52eb4fb-3111-4e38-a1f2-c9e50f346f3e.png">

- Windows/antivirus software may flag this program as a risk, we promise it is safe to run. This project is open source and you can audit the source code if you want to verify yourself - we simply use `pyinstaller` to package it up into an exe.
- The program may load for ~10 seconds on startup, as it takes some time to scan through OpenGOAL memory
- Tracker UI Customization!
  - **Icon layout** is defined in `layout.yaml`:
    https://github.com/OpenGOAL-Unofficial-Mods/jak-tracker/blob/74829b5afe97c552905888afed14c214dd4ed64d/layout.yaml#L6-L26
  - **Colors/sizing/etc** are defined in `prefs.yaml`
    https://github.com/OpenGOAL-Unofficial-Mods/jak-tracker/blob/74829b5afe97c552905888afed14c214dd4ed64d/prefs.yaml#L3-L21
  - **Custom icons** can be used - just replace the corresponding PNG file(s) in the `icons` subfolder
  - *Both of the above YAML files and the entire `icons` subfolder should live in the same folder as `JakTracker.exe`*
