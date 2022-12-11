import textwrap
def wrap(string, max_width):
    wrapped_list = textwrap.wrap(string, max_width)
    s = ""
    for i in wrapped_list:
        s = s + i + "\n"
        
    return s 


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)