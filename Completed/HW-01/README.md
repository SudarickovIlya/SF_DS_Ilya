# Домашнее задание-01. Угадай число

## Оглавление  
[1. Описание проекта](https://github.com/SudarickovIlya/SF_DS_Ilya/tree/main/HW-01#%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)  
[2. Какой кейс решаем?](https://github.com/SudarickovIlya/SF_DS_Ilya/tree/main/HW-01#%D0%BA%D0%B0%D0%BA%D0%BE%D0%B9-%D0%BA%D0%B5%D0%B9%D1%81-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC)  
[3. Краткая информация о данных](https://github.com/SudarickovIlya/SF_DS_Ilya/tree/main/HW-01#%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)  
[4. Этапы работы над проектом](https://github.com/SudarickovIlya/SF_DS_Ilya/tree/main/HW-01#%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)  
[5. Результат](https://github.com/SudarickovIlya/SF_DS_Ilya/tree/main/HW-01#%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)    
[6. Выводы](https://github.com/SudarickovIlya/SF_DS_Ilya/tree/main/HW-01#%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:[к оглавлению](https://github.com/SudarickovIlya/SF_DS_Ilya/tree/main/HW-01#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на python

:arrow_up:[к оглавлению](https://github.com/SudarickovIlya/SF_DS_Ilya/tree/main/HW-01#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

### Краткая информация о данных
С учетом условия задачи, данными являются условный интервал от 1 до 100 и рандомное число в данном промежутке.
  
:arrow_up:[к оглавлению](https://github.com/SudarickovIlya/SF_DS_Ilya/tree/main/HW-01#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### Этапы работы над проектом  
Этапами работы над проектом были написание функции "random_predict" для угадывания числа с условием использования бинарного поиска и score_game для угадывания среднего количнества попыток за 1000 подходов. Проект оформлен в файле "test" на основе схожего [проекта](https://docviewer.yandex.com/view/156408772/?*=9%2FXpS5GfJyjQd1Ke9g3lZyB2EIF7InVybCI6InlhLWRpc2s6Ly8vZGlzay9ndWVzcy1udW1iZXItdGFzayAoMikuemlwIiwidGl0bGUiOiJndWVzcy1udW1iZXItdGFzayAoMikuemlwIiwibm9pZnJhbWUiOmZhbHNlLCJ1aWQiOiIxNTY0MDg3NzIiLCJ0cyI6MTY3MTUzNDA3Mjc4OSwieXUiOiI4NzkzMzA2MTY2ODEwMjMzNyJ9) из курса Data Scientist от школы Skillfactory.

:arrow_up:[к оглавлению](https://github.com/SudarickovIlya/SF_DS_Ilya/tree/main/HW-01#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### Результат 
В результате была получена функция для угадывания числа за 6 попыток.

:arrow_up:[к оглавлению](https://github.com/SudarickovIlya/SF_DS_Ilya/tree/main/HW-01#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### Выводы
В Python возможно прописать функцию рандомного поиска числа за минимальное количество попыток.

:arrow_up:[к оглавлению](https://github.com/SudarickovIlya/SF_DS_Ilya/tree/main/HW-01#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)