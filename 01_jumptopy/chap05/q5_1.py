f= open('D:\\bigdata\\python_workspace\\openbigdata\\01_jumptopy\\chap05\\learning_python.txt', 'r')
lines = f.read()
f.close()

f= open('D:\\bigdata\\python_workspace\\openbigdata\\01_jumptopy\\chap05\\learning_python_copyed.txt', 'w')
f.write(lines.replace("python","C"))
f.close()