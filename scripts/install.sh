command -v arduino-cli >/dev/null 2>&1
ARDUINO_CLI_INSTALLED=$?

if [[ ${ARDUINO_CLI_INSTALLED} != 0 ]]; then
    echo "This project requires the arduno-cli. See: https://github.com/arduino/arduino-cli"
    exit 1
fi

mkdir -p "dist"
arduino-cli "core" "install" "arduino:sam" && echo "Install finished successfully!"