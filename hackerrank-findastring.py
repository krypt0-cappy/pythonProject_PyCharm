from collections import Counter
string = "ABCDCDC"
sub_string = "CDC"

def count_substring(string, sub_string):
    string_count=0
    sub_string_count=len(sub_string)
    for i in range(len(string)):
        sub_count=string[i:i+sub_string_count]
        if sub_count==sub_string:
            string_count+=1
    return string_count


if __name__ == '__main__':
    string = string.strip()
    sub_string = sub_string.strip()

    count = count_substring(string, sub_string)
    print(count)