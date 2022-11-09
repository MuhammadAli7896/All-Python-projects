# # Enter your code here. Read input from STDIN. Print output to STDOUT
# while True:
#     a = int(input())
#     b = int(input())
#     try:
#         #b = int(input())
#         print(a/b)
#     except ValueError:
#         print("Error Code: invalid literal for int() with base 10: ", b)
#         continue
#     except ZeroDivisionError:
#         print("Error Code: integer division or modulo by zero")
#         continue

        
for _ in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(a//b)
    # except ZeroDivisionError:
    #     print("Error Code: integer division or modulo by zero")
    #     continue
    # except ValueError:
    #     print("Error Code: invalid literal for int() with base 10: ", b)
    #     continue
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e) 
    

        
        
        
