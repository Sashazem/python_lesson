n = int(input('Введите, количество пингвинов: '))
a = "    _~_    "
b = "   (o o)   "
c = "  /  V  \  "
d = " /(  _  )\ "
e = "   ^^ ^^   "
penguin = (a * n + "\n" + b * n + "\n" +
           c * n + "\n" + d * n + "\n" + e * n + "\n")
print(penguin)
