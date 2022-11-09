if __name__ == '__main__':
    s = input()
    # l = [[], [], [], [], [], []]
    # for i in s:
    #     if i.isalnum() == True:
    #         l[0].append("True")
    #         if i.isalpha() == True:
    #             l[1].append("True")
    #             if i.islower() == True:
    #                 l[3].append("True")
    #             if i.isupper() == True:
    #                 l[4].append("True")
    #         if i.isdigit() == True:
    #             l[2].append("True")
    # for item in l:
    #     print(any(item))
    print(any([x.isalnum() for x in s]))
    print(any([x.isalpha() for x in s]))
    print(any([x.isdigit() for x in s]))
    print(any([x.islower() for x in s]))
    print(any([x.isupper() for x in s]))
