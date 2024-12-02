param (
    [Parameter(Mandatory=$true)]
    [int]$Day
)

# Define your session token in a session.ps1 file in the same folder as this script
# also don't forget to add session.ps1 to the .gitignore
# Import the session token
. ./session.ps1

# Define the year
$year = 2022

# URL to fetch the input data
$url = "https://adventofcode.com/$year/day/$Day/input"

# Define the output directory and files
$outputDirectory = "./$year/Day$Day"
$outputFile = "$outputDirectory/input.txt"
$testFile1 = "$outputDirectory/test.txt"
$part1 = "{0}/day{1}_part1.py" -f $outputDirectory, $Day
$part2 = "{0}/day{1}_part2.py" -f $outputDirectory, $Day

$template = @"
# Advent of Code $year - Day $Day
# Author: Yelleyo

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def main():
    with open('test.txt', 'r') as file:
        lines = file.read().splitlines()


if __name__ == '__main__':
    main()
"@

# Create the directory if it doesn't exist
if (-not (Test-Path -Path $outputDirectory)) {
    New-Item -ItemType Directory -Path $outputDirectory
}

# Use Invoke-WebRequest to download the input data
try {
    Invoke-WebRequest -Uri $url -WebSession (New-Object Microsoft.PowerShell.Commands.WebRequestSession) -Headers @{ "Cookie" = "session=$session" } -OutFile $outputFile
    Write-Output "Downloaded input data to $outputFile"
    New-Item -ItemType File -Path $testFile1 -Force | Out-Null
    New-Item -ItemType File -Path $part1 -Force | Out-Null
    New-Item -ItemType File -Path $part2 -Force | Out-Null
    
    New-Item -ItemType File -Path $part1 -Force | Out-Null
    Set-Content -Path $part1 -Value $template
    
    New-Item -ItemType File -Path $part2 -Force | Out-Null
    Set-Content -Path $part2 -Value $template

    Write-Output "Created files"

    Write-Output "Taking you to $outputDirectory"
    Set-Location -Path $outputDirectory
} catch {
    Write-Output "Failed to download and/or create data: $_"
    exit 1
}