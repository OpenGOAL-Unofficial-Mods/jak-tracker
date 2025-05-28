# jak-tracker
## Customizable Tracker, w/ OpenGOAL Autotracker 

Download the latest release `JakTracker.zip` from [here](https://github.com/OpenGOAL-Unofficial-Mods/jak-tracker/releases/latest)

⚠ MAKE SURE YOU HAVE SPEEDRUNNER MODE ENABLED ⚠

Piggybacking on the work done to support LiveSplit autosplitter, this program will scan OpenGOAL memory and display which Power Cells you've collected in your current game. It also has a `manual` tracker mode which you could use for any game you want - you'd just need to setup a layout and corresponding icons.

<img width="250" alt="image" src="https://user-images.githubusercontent.com/2515356/204374691-a52eb4fb-3111-4e38-a1f2-c9e50f346f3e.png">

### Notes
- Windows/antivirus software may flag this program as a risk, we promise it is safe to run. This project is open source and you can audit the source code if you want to verify or run the python yourself - we simply use `pyinstaller` to package it up into an exe for easier distribution.
- In `auto` tracker mode, the program may load for ~10 seconds on startup, as it takes some time to scan through OpenGOAL memory
  - NEW: `prefs.yaml` has a `gk_offset` field to help speed this process up by skipping the first ~12MB of memory
- In `manual` tracker mode:
  - You can click on `boolean` icons to toggle them on/off
  - You can click/shift+click on `counter` icons to increase/decrease their count
- Use the right-click menu to swap between layouts, or refresh the current layout from file (useful as you test changes)
- `prefs.yaml`, `fields.yaml` and the `layouts` and `icons` subfolders should all live in the same folder as `JakTracker.exe` (see below for more details)
 
### Configuration Files
- **Custom icons** can be used - just replace the corresponding PNG file(s) in the [`icons`](https://github.com/OpenGOAL-Unofficial-Mods/jak-tracker/tree/main/icons) subfolder
- **Icon/text layout** is defined in the [`layouts`](https://github.com/OpenGOAL-Unofficial-Mods/jak-tracker/tree/main/layouts) subfolder, for example:
https://github.com/OpenGOAL-Unofficial-Mods/jak-tracker/blob/8e7f73a996bb8543bf194a63c9933c0de2ea8340/layouts/noLTS_moles_plants.yaml#L6-L26
- **Colors/sizing/etc** are defined in [`prefs.yaml`](https://github.com/OpenGOAL-Unofficial-Mods/jak-tracker/blob/main/prefs.yaml):
https://github.com/OpenGOAL-Unofficial-Mods/jak-tracker/blob/71faa5c915fc098294c6c3ebd3cc7bd22b306c35/prefs.yaml#L3-L27
- *`fields.yaml` defines the autosplitter/autotracker fields and their offsets - you shouldn't need to touch this!*
