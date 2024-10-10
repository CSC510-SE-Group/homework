#!/bin/bash

# Extract passengers from 2nd class who embarked at Southampton,
# replace male/female labels with M/F, and calculate the average age.

awk -F',' '
NR == 1 {
    print; 
    header = 1;
    next
} 
NR > 1 {
    gsub(/^[ \t]+|[ \t]+$/, "", $5); 
    if (tolower($5) == "female") $5 = "F"; 
    else if (tolower($5) == "male") $5 = "M"; 
    gsub(/[^a-zA-Z]/, "", $12); 
    if ($12 == "S" && $3 == "2") {
        print $1 "," $2 "," $3 "," $4 "," $5 "," $6 "," $7 "," $8 "," $9 "," $10 "," $11 "," $12;
        total_age += $6; # Add age to total_age
        count++;         # Increment count of passengers
    } 
} 
END {
    if (count > 0) {
        avg_age = total_age / count;  # Calculate average age
        print "Average Age of Filtered Passengers: " avg_age;
    } else {
        print "No filtered passengers found.";
    }
}' titanic.csv 