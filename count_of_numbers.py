def find_count_of_nos(num):
    no_count = {}
    for each in num:
        if each not in no_count.keys():
            no_count[each] = 1
        else:
            no_count[each] += 1
    for no,count in no_count.items():
        print(no," its count is :",count)

if __name__ == '__main__':
    input_no = input("Enter any 10 digit number")
    if len(input_no) == 10:
        find_count_of_nos(input_no)
    else:
        print("Please enter valid no with 10 digits")
