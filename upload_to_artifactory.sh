#!/bin/bash

# Exit script on any error
set -e

# Configuration Variables
ARTIFACTORY_URL="http://cerdo.unraveldata.com/artifactory/api/pypi/pypi"
USERNAME="pvenkatesh@unraveldata.com"
PASSWORD="jsd9377Xv@"

# Ensure necessary tools are installed
echo "Checking for required tools..."
pip install --upgrade build twine

# Build the package using pypa/build
echo "Building the package with pypa/build..."
python -m build

# Verify the package
echo "Verifying the package..."
twine check dist/*

# Upload the package to Artifactory
echo "Uploading the package to Artifactory..."
twine upload --repository-url "$ARTIFACTORY_URL" -u "$USERNAME" -p "$PASSWORD" dist/*

# Success message
echo "Package uploaded successfully to $ARTIFACTORY_URL"
