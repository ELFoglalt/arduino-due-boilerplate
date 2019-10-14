# arduino-due-boilerplate

A super janky repository set up for C++ development on the [Auino Due](https://store.arduino.cc/due), using VSCode the [arduino-cli](https://github.com/arduino/arduino-cli). I wouldn't recommend using it as-is, since I have no idea what I'm doing, but this might be a helpful starting point for others.

## Usage

- Fork/clone/copy the repository
- Rename the folder and the [arduino sketch file](https://github.com/elfoglalt/arduino-due-boilerplate/blob/master/arduino-due-bolerplate.ino). Make sure the sketch file and the folder share the same name (this is required by arduino-cli).
- Run `./scripts/install.sh` to download the Arduino SAM Core.
- Build and run using either directly the arduno-cli, or using the configured tasks. (The tasks currently require python3 to automatically find the connected board's port. Customize the [tasks.json](https://github.com/elfoglalt/arduino-due-boilerplate/blob/master/.vscode/tasks.json) file to your liking.)