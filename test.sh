#!/bin/bash
# Builds and runs the Pytest command

# Test running command:
test_command="pytest"

# Setup test path:
export PYTHONPATH=:.

# Disable Pytest warnings:
test_command="${test_command} --disable-warnings"

# Setup test scope:
if [ -z "$1" ]; then
  test_command="${test_command} tests/"
else
  test_command="${test_command} -m"
fi

# Run the commands
echo $test_command "$@";
eval $test_command "$@";
