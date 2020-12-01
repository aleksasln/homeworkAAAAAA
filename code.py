print('''C помощью данной программы мы сможем ответить на следующие вопросы:
      а) Являются ли поля №1 и №2 полями одного цвета?

      6) На поле №1 расположен ферзь. Угрожает ли он полю №2?

      в) На поле №1 расположен конь. Угрожает ли он полю №2?

      г) Можно ли с поля №1 одним ходом ладьи попасть на поле  №2. Если нет, то как это можно сделать за два хода?

      д) Можно ли с поля №1 одним ходом ферзя попасть на поле  №2. Если нет, то как это можно сделать за два хода?

      е) Можно ли с поля №1 одним ходом слона попасть на поле  №2. Если нет, то как это можно сделать за два хода?
    ''')
k, l = map(int,input('Введите 2 координаты для поля №1 через пробел (от 1 до 8): ').split())
m, n =map(int,input('Введите 2 координаты для поля №2 через пробел (от 1 до 8): ').split())

if(k+l+m+n) % 2==0: #Ответ на пункт "а"
    print('а) Поля одного цвета')
else:
    print('а) Поля разных цветов')

if k == m or l == n or abs(k - m) == abs(l - n): #Ответ на пункт "б"
    print('б) Ферзь угожает полю №2 (%d,%1d)' % (m, n))
else:
    print('б) Ферзь не угожает полю №2 (%d,%1d)' % (m, n))
