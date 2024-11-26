# Your session token
session="53616c7465645f5f05403d719a4f3a0ac27d084a6f8c4d1fabc7800011e8d8211d993d744e383ee3f2a0f46ce1ccc822aff9e31f258e410e1f00d56130201776"

# URL to fetch the input data
url="https://adventofcode.com/2023/day/1/input"

# Output file
output_file="day1.txt"

# Use curl to download the input data
curl -s -b "session=$session" "$url" -o "$output_file"

# Check if the download was successful
if [ $? -eq 0 ]; then
    echo "Downloaded input data to $output_file"
else
    echo "Failed to download input data"
    exit 1
fi