# jak-tracker
## Auto-Tracker for OpenGOAL Jak 1 (Randomizer)

Download the latest release `JakTracker.zip` from [here](https://github.com/OpenGOAL-Unofficial-Mods/jak-tracker/releases/latest)

Piggybacking on the work done to support LiveSplit autosplitter, this program will scan OpenGOAL memory and display which Power Cells you've collected in your current game. 

<img width="250" alt="image" src="https://user-images.githubusercontent.com/2515356/204374691-a52eb4fb-3111-4e38-a1f2-c9e50f346f3e.png">

### Notes
- Windows/antivirus software may flag this program as a risk, we promise it is safe to run. This project is open source and you can audit the source code if you want to verify or run the python yourself - we simply use `pyinstaller` to package it up into an exe for easier distribution.
- The program may load for ~10 seconds on startup, as it takes some time to scan through OpenGOAL memory
- Use the right-click menu to swap between layouts. Also useful for refreshing the current layout from file, as you test changes
- `prefs.yaml`, `fields.yaml` and the `layouts` and `icons` subfolders should all live in the same folder as `JakTracker.exe` (see below for more details)
 
### Configuration Files
- **Custom icons** can be used - just replace the corresponding PNG file(s) in the [`icons`](https://github.com/OpenGOAL-Unofficial-Mods/jak-tracker/tree/main/icons) subfolder
- **Icon/text layout** is defined in the [`layouts`](https://github.com/OpenGOAL-Unofficial-Mods/jak-tracker/tree/main/layouts) subfolder, for example:
https://github.com/OpenGOAL-Unofficial-Mods/jak-tracker/blob/8e7f73a996bb8543bf194a63c9933c0de2ea8340/layouts/noLTS_moles_plants.yaml#L6-L26
- **Colors/sizing/etc** are defined in [`prefs.yaml`](https://github.com/OpenGOAL-Unofficial-Mods/jak-tracker/blob/main/prefs.yaml):
https://github.com/OpenGOAL-Unofficial-Mods/jak-tracker/blob/8e7f73a996bb8543bf194a63c9933c0de2ea8340/prefs.yaml#L3-L23
- *`fields.yaml` defines the autosplitter/autotracker fields and their offsets - you shouldn't need to touch this!*
