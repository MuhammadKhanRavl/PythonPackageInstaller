"""
______________________________________________________________________________________________________
              
PythonPackageInstaller - A simple script for installing python packages.

This script automates the process of installing Python packages using pip and a requirments file. 

Main Functions: 
    1. Creating an Updated Requirements File:
        - Reads from the specified requirements txt file.
        - Removes the version specifications from the package names (eg. "==1.2.3").
        - Outputs a new requirements file used for installing latest versions of packages.
    2. Installing Packages:
        - Installs Python packages listed in the specified requirements file using pip. 
        - Handles installation errors by logging them.
        - Continues with next package installation when encountering an error. 

Usage: 
- Ensure that a requirements file (in .txt format) is in the same directory as this script. 
- Run the script.
- Check the packageErrors.txt file to see if any packages were not installed. 
        
Author: Muhammad Abdullah Khan (khanmuh)
Date: 11/12/2023
Version: 1.0
______________________________________________________________________________________________________
"""

# Importing Libraries
import subprocess
import argparse


# Defining global variables
inputFile = 'requirements.txt'            # Incoming requirements file
outputFile = 'requirements-latest.txt'    # Outgoing requirements file
logFile = 'errors.txt'                    # Error logging file


# Function for removing version specification from given requirements file
def removeVersions(inputFile, outputFile):
    
    # Reading input file
    try:
        with open(inputFile, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file {inputFile} was not found.")    
        return False
    
    # Stripping versions
    newLines = [line.split('==')[0].strip() + '\n' for line in lines]

    # Outputting
    with open(outputFile, 'w') as file:
        file.writelines(newLines)

    return True


# Function for installing packages as per given requirements file
def installPackages(requirementsFile, logFile):

    # Reading requirements file
    try:
        with open(requirementsFile, 'r') as file:
            packages = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file {requirementsFile} was not found.")    
        return False

    # Installing packages and logging errors
    with open(logFile, 'w') as log:
        for package in packages:
            package = package.strip()
            result = subprocess.run(f"pip install {package}", capture_output=True, text=True, shell=True)
            if result.returncode != 0:
                errorMessage = f"Error installing {package}: {result.stderr}"
                print(f"Error installing {package}.")
                log.write(errorMessage + '\n\n')
            else:
                print(f"Successfully installed {package}. \n")
    
    return True


if __name__ == "__main__":

    # Handling script arguments 
    parser = argparse.ArgumentParser(description= "PythonPackageInstaller - A simple script for \
                                     installing python packages")
    parser.add_argument("--skip-strip", action="store_true", help="skips removal of version specification from \
                        requirements file")
    parser.add_argument("--skip-install", action="store_true", help="skips the installation of the packages")
    args = parser.parse_args()

    # Stripping Version Specification 
    if not args.skip_strip:
        isSuccess = removeVersions(inputFile, outputFile)
        if not isSuccess:
            exit(1)
        print("Version specifications removed successfully.")
    
    # Installing packages
    print("Installing packages...") 
    isSuccess = installPackages(outputFile, logFile)
    if not isSuccess:
        exit(1)
    
    print("Done installing packages.")


