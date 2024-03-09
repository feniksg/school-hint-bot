LEARNING_DATA = {
    "1. Линейные уравнения с одной переменной": 
            '''Линейное уравнение с одной переменной — это уравнение вида ax + b = 0, где x — переменная, а a и b — числовые коэффициенты, причём a ≠ 0. Число a называется коэффициентом при переменной, а b — свободным членом.
            Примеры линейных уравнений:
            •	2x + 3 = 0
            •	-x - 5 = 0
            •	4.5x + 1 = 0
            Решение линейных уравнений
            Решение линейного уравнения — это значение переменной x, при котором уравнение обращается в верное числовое равенство. Чтобы найти это значение, нужно выполнить следующие шаги:
            •	Перенести все члены уравнения с переменной x на одну сторону, а числовые члены — на другую.
            •	Привести подобные слагаемые.
            •	Разделить обе части уравнения на коэффициент при x.
            Пример решения уравнения 2x + 3 = 0:
            •	Переносим 3 на другую сторону уравнения: 2x = -3.
            •	Делим обе части уравнения на 2: x = -3/2.
            Проверка решения:
            •	Подставляем найденное значение x в исходное уравнение: 2(-3/2) + 3 = -3 + 3 = 0. Уравнение верно, значит, решение найдено правильно.
            Применение линейных уравнений в задачах:
            Линейные уравнения часто используются для решения различных практических задач, например:
            •	Задачи на движение, где неизвестно расстояние или скорость.
            •	Задачи на работу, где нужно найти время или производительность труда.
            •	Задачи на смеси и сплавы, где необходимо вычислить концентрацию вещества.
        ''',
    '2. Многочлены': {
        "Определение": 
            """Многочлен — это математическое выражение, состоящее из суммы или разности членов, каждый из которых является произведением некоторой константы (называемой коэффициентом) и переменной, возведенной в некоторую степень, причем эта степень является неотрицательным целым числом. 
            Например, 2x^3 - 3x^2 + 5x - 7 — это многочлен.
            Каждый член многочлена имеет следующий вид: ax^n, где a - коэффициент, x - переменная, а n - неотрицательное целое число, называемое степенью этого члена.
            Основные понятия:
            Степень многочлена — это наивысшая степень его переменной. Например, степень многочлена 2x^3 + 3x^2 - x + 4 равна 3.
            Коэффициент — это числовая величина, на которую умножается переменная в многочлене. В упомянутом выше примере коэффициенты равны 2, 3, -1 и 4.
            Члены многочлена — это составные части многочлена, соединенные знаками плюс или минус. В многочлене 2x^3 + 3x^2 - x + 4 есть четыре члена: 2x^3, 3x^2, -x, и 4.
            Важные свойства многочленов:
            •	Многочлены замкнуты относительно операций сложения, вычитания и умножения, что означает, что результат этих операций всегда будет многочленом.
            •	Деление многочленов может привести как к многочлену, так и к рациональному выражению.
            •	Многочлены могут быть разложены на множители, используемые для упрощения выражений и решения уравнений.
            """, 
        '2.3.1. Вынесение общего множителя за скобки' : 
            """Вынесение общего множителя за скобки
            Что это такое?
            Вынесение общего множителя за скобки — это метод упрощения многочлена, при котором из всех его членов выделяется общий множитель. Этот процесс помогает сократить многочлен и сделать его более компактным для дальнейших операций, таких как умножение или факторизация.

            Как это делать?
            Сначала определите общий множитель. Это число или выражение, которое делит каждый член многочлена без остатка.
            Разделите каждый член многочлена на этот общий множитель.
            Запишите общий множитель перед скобкой и внутри скобки укажите результаты деления каждого члена на общий множитель.

            Пример:
            Допустим, у нас есть многочлен 6x^3 + 12x^2 + 18x.
            Определяем общий множитель. В данном случае, 6x можно вынести за скобки, так как каждый член многочлена делится на 6x.
            Делим каждый член на 6x:
            6x^3 / 6x = x^2
            12x^2 / 6x = 2^x
            18x / 6x = 3
            Выносим общий множитель за скобки и записываем результаты деления в скобках:
            6x^3 + 12x^2 + 18x = 6x(x^2 + 2x + 3)
            Теперь многочлен 6x(x2 + 2x + 3) выглядит намного проще, чем исходный, и его легче использовать для дальнейших операций.

            Другой пример:
            Рассмотрим многочлен 4x^4 + 8x^3 - 12x^2:
            Общий множитель здесь — 4x^2.
            Делим каждый член на 4x^2:
            4x^4 / 4x^2 = x^2
            8x^3 / 4x^2 = 2x
            -12x^2 / 4x^2 = -3
            Выносим общий множитель и записываем оставшиеся члены в скобках:
            4x^4 + 8x^3 - 12x^2 = 4x^2(x^2 + 2x - 3)
            """, 
       "2.3.2 Группировка многочленов" : 
            """Что такое группировка?
            Группировка многочленов — это способ факторизации, который используется, когда многочлен содержит четыре или более члена. Идея состоит в том, чтобы разделить многочлен на группы с общими множителями, а затем вынести эти общие множители за скобки. Иногда, после группировки, появляется возможность вынести ещё один общий множитель, который раньше не был очевиден.

            Как это делать?
            Разделите многочлен на группы таким образом, чтобы в каждой группе можно было вынести общий множитель.
            Вынесите общий множитель в каждой группе.
            Если после вынесения общих множителей получились одинаковые множители в скобках, вынесите этот повторяющийся множитель за скобку.

            Пример:
            •	Рассмотрим многочлен x^3 + 2x^2 + x + 2.
            1) Разделим его на две группы: (x^3 + 2x^2) и (x + 2).
            2) В первой группе общий множитель — это x^2, а во второй — можно считать, что это 1, так как другого общего множителя нет.
            3) Вынесем общие множители и посмотрим, что у нас получится:
                      x^2 * (x + 2) из первой группы
                      1 * (x + 2) из второй группы
            4) Теперь у нас есть два выражения (x + 2) в обоих группах, что означает, что мы можем их объединить:
                     (x2 + 1) * (x + 2)
            5) Теперь мы успешно разложили исходный многочлен на множители с помощью метода группировки: x^3 + 2x^2 + x + 2 = (x^2 + 1) * (x + 2).
               Этот метод особенно полезен, когда нет очевидного общего множителя у всех членов многочлена или когда стандартная факторизация на первый взгляд не работает. Группировка помогает увидеть скрытую структуру в многочлене и использовать её для упрощения.
            """, 
        "2.3.3 Формулы сокращённого умножения": 
            """Разложение многочлена на множители: Формулы сокращённого умножения
            Формулы сокращённого умножения — это математические выражения, которые облегчают умножение и факторизацию, позволяя быстро умножать двучлены и трёхчлены без необходимости применения распределительного закона по каждому члену. Их часто используют для разложения многочленов на множители.
            Вот основные формулы сокращённого умножения, которые используются в школьной программе:

            1.	Квадрат суммы
                Формула: (a + b)2 = a^2 + 2ab + b^2
                Пример:
                (x + 3)2 = x^2 + 2*x*3 + 32 = x^2 + 6x + 9
            Эта формула используется, когда вам нужно возвести в квадрат сумму двух выражений.

            2.	Квадрат разности
              Формула: (a - b)^2 = a^2 - 2ab + b2
              Пример:
              (x - 4)^2 = x^2 - 2*x*4 + 42 = x^2 - 8x + 16
            Это удобный способ быстро найти квадрат разности двух выражений.

            3.	Разность квадратов
              Формула: a^2 - b2 = (a + b)(a - b)
              Пример:
              x^2 - 9 = (x + 3)(x - 3)
            Эта формула позволяет разложить разность квадратов на произведение суммы и разности.

            4.	Куб суммы
              Формула: (a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3
              Пример:
              (x + 2)^3 = x^3 + 3*x^2*2 + 3*x*22 + 23 = x^3 + 6x^2 + 12x + 8
            Формула помогает вычислить куб суммы двух чисел или переменных.

            5.	Куб разности
              Формула: (a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3
              Пример:
              (x - 1)^3 = x^3 - 3*x2*1 + 3*x*12 - 13 = x^3 - 3x^2 + 3x - 1
            Используйте эту формулу, когда нужно возвести в куб разность двух выражений.

            6.	Сумма кубов
              Формула: a^3 + b^3 = (a + b)(a^2 - ab + b^2)
              Пример:
              x^3 + 8 = x^3 + 23 = (x + 2)(x^2 - x*2 + 22) = (x + 2)(x^2 - 2x + 4)
            Эта формула позволяет разложить сумму кубов на произведение двух многочленов.

            7.	Разность кубов
              Формула: a^3 - b^3 = (a - b)(a^2 + ab + b^2)
              Пример:
              x^3 - 27 = x^3 - 33 = (x - 3)(x^2 + x*3 + 32) = (x - 3)(x^2 + 3x + 9)
            Используется для разложения разности кубов на произведение двух многочленов.
            """
    }
}