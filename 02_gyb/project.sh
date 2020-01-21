#!/bin/sh
#===============================================================================
# Run Project.sh
#===============================================================================

SCRIPT_DIR=$(cd $(dirname $0);pwd)
COLOR_DIR=$SCRIPT_DIR/Color
STRING_DIR=$SCRIPT_DIR/String

# Strings
GEN_STRINGS_SRC=$STRING_DIR/input/Localizable.swift.gyb
GEN_STRINGS_DST=$STRING_DIR/output/WKLanguage.swift
GEN_STRINGS_PYFILE=$STRING_DIR/input/localizableString.py

# Color
GEN_COLOR_SRC=$COLOR_DIR/input/Colors.swift.gyb
GEN_COLOR_DST=$COLOR_DIR/output/WKColor.swift
GEN_COLOR_PYFILE=$COLOR_DIR/input/assetColor.py

echo "##### Check Porject  installation #####"
if which gyb >/dev/null; then
  echo "gyb is installed."
else
  echo "\033[41m install gyb."
  pip3 install gyb
fi
if which python3 >/dev/null; then
  echo "python3 is installed."
else
  echo "033[0;31m python3 is not installed."
fi
echo "\033[0;32m ##### Generate #####"

# Color
gyb --line-directive '' $GEN_COLOR_SRC -o $GEN_COLOR_DST
echo "##### Create WaninColor.swift #####"
python3 $GEN_COLOR_PYFILE
echo "##### Create Color asset #####"

# String
python3 $GEN_STRINGS_PYFILE
echo "##### Create LocallizableString #####"
gyb --line-directive '' $GEN_STRINGS_SRC -o $GEN_STRINGS_DST
echo "##### Create WaninLanguage.swift #####"
echo "##### success #####"
echo "\033[0;37m"
