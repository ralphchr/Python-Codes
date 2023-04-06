import time

def SNconverter(streng):
    for i in streng:
        if i in alphabet:
            final.append((alphabet.index(i)+1))
        elif i in "0123456789":
            final.clear()
            final.append("A number is not allowed")
            break
        elif i == " ":
            final.append("_")
    time.sleep(3)
    print("Converting... Please wait")
    time.sleep(3)
    print()
    print("The Converted String is:",end=" ")
    for i in final:
        print(i,end=" ")
        
def NSconverter(nums):
    space = 0
    for i in nums:
        if i in "0123456789":
            i = int(i)
            final.append(alphabet[i-1])
        elif i == "_":
            final.append(" ")
            space += 1
        elif i not in "0123456789_":
            final.clear()
            final.append("A number is required")
            break
    time.sleep(3)
    lenha = len(nums) - space
    for i in range(1, lenha+1):
        print(f"Converting {i} out of {lenha}.")
        time.sleep(1)
    print()
    print("The Final String is:", end=' ')
    for i in final:
        print(i, end='')

alphabet ="abcdefghijklmnopqrstuvwxyz"
final = []

                    
print("String-Number Converter")
time.sleep(3)
print("Choose a Mode to use")
mode = input("""
String to Number = SN
or
Number to String = NS

Mode: """).upper()

if mode == "SN":
    print()
    streng = input("Enter your string: ")
    SNconverter(streng)
    time.sleep(1)
    print()
    time.sleep(1)


elif mode == "NS":
    time.sleep(1)
    print("A little tutorial on how to input your numbers.")
    time.sleep(1)
    print("""
    Example:
    input: 1 2 3 _ 4 5 6
    The output would be 'abc def'""")
    time.sleep(2)
    print()
    nums = input("Enter your number (use _ for space): ").split()
    NSconverter(nums)
    time.sleep(1)
    print()
    time.sleep(1)
    
print("Do you want to continue? Y or N")
time.sleep(1)
ans= input("Yes or No: ").upper()
print()
while ans == "Y":
    for i in range(100):
        print("\n")
    final.clear()
    print("Choose a Mode to use")
    mode = input("""
    String to Number = SN
    or
    Number to String = NS

    Mode: """).upper()
    if mode == "SN":
        streng = input("Enter your string: ")
        print()
        SNconverter(streng)
        time.sleep(1)
        print()
        time.sleep(1)
    elif mode == "NS":
        time.sleep(1)
        print("A little tutorial on how to input your numbers.")
        print()
        time.sleep(1)
        print("""
        Example:
        input: 1 2 3 _ 4 5 6
        The output would be 'abc def'""")
        print()
        time.sleep(2)
        nums = input("Enter your number (use _ for space): ").split()
        NSconverter(nums)
        time.sleep(1)
        print()
        time.sleep(1)
    print("Do you want to continue? Y or N")
    time.sleep(1)
    ans= input("Yes or No: ").upper()

print("Thank you for using the converter.")
