def count_upper_case(message):
    count = 0 
    for c in message:
        if c.isupper():
            count += 1
    return count
    
assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("ABA") == 3, "3 upper cases"
assert count_upper_case("BB") == 2, "2 upper cases"

print("All tests have passed")


