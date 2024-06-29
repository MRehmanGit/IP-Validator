# This function checks if there are exactly three dots in the given string, which is required for a valid IP format.
def number_of_dots(s):
    dot_counter = 0
    for element in s:
        if element == '.':
            dot_counter += 1

    # If there are exactly 3 dots, return 1, indicating a potential valid IP format.
    if dot_counter == 3:
        return 1
    else:
        return 2

# This function validates each number in the IP address and checks if they are in the correct range (0-255).
def range_checker(s):
    string_counter = ""  # To accumulate the current segment of the IP address.
    counter_zero  = 0  # To count the number of zeroes in the IP address.
    for everyelement in s:
        if everyelement == ".":
            try:
                final_value = int(string_counter)  # Convert the accumulated string to an integer.
            except ValueError:
                return 2  # Return 2 if conversion fails, indicating an invalid segment.

            if final_value < 0 or final_value > 255:
                return 2  # Return 2 if the segment is out of the valid range.
            else:
                string_counter = ""  # Reset the accumulator for the next segment.
                continue
        else:
            # If the current element is "0", increment the zero counter.
            if everyelement == "0":
                counter_zero += 1
            # Accumulate the current element to form the current segment.
            string_counter += everyelement

    # End of loop, check if there are too many zeros in the IP address.
    if counter_zero == 16:
        return 2

    return 1

# This function combines the previous two checks to determine if the given string is a valid IP address.
def isValid(s):
    if range_checker(s) == 1 and number_of_dots(s) == 1:
        return True
    else:
        return False


# Input from the user
s = input("Enter IP Address: ")
# Check if the input string is a valid IP address and print the result.
if isValid(s):
    print("Valid IP Address")
else:
    print("Invalid IP Address")
