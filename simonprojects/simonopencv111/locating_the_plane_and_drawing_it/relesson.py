with open('C:\Users\tzx\PycharmProjects\k_line_draw\C1.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 