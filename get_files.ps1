param (
    [Parameter(Mandatory=$true)]
    [int]$Day
)

# Define your session token
$session = "53616c7465645f5f05403d719a4f3a0ac27d084a6f8c4d1fabc7800011e8d8211d993d744e383ee3f2a0f46ce1ccc822aff9e31f258e410e1f00d56130201776"

# Define the year
$year = 2024

# URL to fetch the input data
$url = "https://adventofcode.com/$year/day/$Day/input"

# Define the output directory and files
$outputDirectory = "./$year/Day$Day"
$outputFile = "$outputDirectory/input.txt"
$testFile1 = "$outputDirectory/test1.txt"
$testFile2 = "$outputDirectory/test2.txt"
$part1 = "{0}/day{1}_part1.py" -f $outputDirectory, $Day
$part2 = "{0}/day{1}_part2.py" -f $outputDirectory, $Day

# Create the directory if it doesn't exist
if (-not (Test-Path -Path $outputDirectory)) {
    New-Item -ItemType Directory -Path $outputDirectory
}

# Use Invoke-WebRequest to download the input data
try {
    Invoke-WebRequest -Uri $url -WebSession (New-Object Microsoft.PowerShell.Commands.WebRequestSession) -Headers @{ "Cookie" = "session=$session" } -OutFile $outputFile
    Write-Output "Downloaded input data to $outputFile"
    New-Item -ItemType File -Path $testFile1 -Force | Out-Null
    New-Item -ItemType File -Path $testFile2 -Force | Out-Null
    New-Item -ItemType File -Path $part1 -Force | Out-Null
    New-Item -ItemType File -Path $part2 -Force | Out-Null
    Write-Output "Created files"
} catch {
    Write-Output "Failed to download and/or create data: $_"
    exit 1
}