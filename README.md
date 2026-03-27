# filtered-calendar

## Що робить скрипт
- Відсортовує події за початковою датою (START_FROM_DATE)
- ділить події відповідно до групи

## Групи 
| Група | Пн    | Вт    | Ср    | Чт    | Посилання                                                                                                                                    |
| ----- | ----- | ----- | ----- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | 10:00 |       | 10:00 |       | [LNA_group1](https://calendar.google.com/calendar/embed?src=6ealjvds7kpike732q8gtpejmqllikkv%40import.calendar.google.com&ctz=Europe%2FKyiv) |
| 2     | 14:00 |       | 14:00 |       | [LNA_group2](https://calendar.google.com/calendar/embed?src=uqfh2h8okebhenpmnbr9j8f6s25ga3m5%40import.calendar.google.com&ctz=Europe%2FKyiv) |
| 3     | 17:00 |       | 17:00 |       | [LNA_group3](https://calendar.google.com/calendar/embed?src=3uvnbnfiunongse0o8ekcs2dvb1qsn15%40import.calendar.google.com&ctz=Europe%2FKyiv) |
| 4     | 19:00 |       | 19:00 |       | [LNA_group4](https://calendar.google.com/calendar/embed?src=pu28mm8nmgl2arefh6p07gd7ivs082pm%40import.calendar.google.com&ctz=Europe%2FKyiv) |
| 5     |       | 10:00 |       | 10:00 | [LNA_group5](https://calendar.google.com/calendar/embed?src=vfsj17ec4ou96e87lqbfbr3r8uca99bc%40import.calendar.google.com&ctz=Europe%2FKyiv) |
| 6     |       | 14:00 |       | 14:00 | [LNA_group6](https://calendar.google.com/calendar/embed?src=6p3tp63t0g3hf3t6s1jbganp1e5hbn7s%40import.calendar.google.com&ctz=Europe%2FKyiv) |
| 7     |       | 17:00 |       | 17:00 | [LNA_group7](https://calendar.google.com/calendar/embed?src=2heqn9ue3bstsdhn5t87d035ne9k5rb0%40import.calendar.google.com&ctz=Europe%2FKyiv) |
| 8     |       | 19:00 |       | 19:00 | [LNA_group8](https://calendar.google.com/calendar/embed?src=jjvj0g6bjsebsreroqr9h6pqodfeqmf5%40import.calendar.google.com&ctz=Europe%2FKyiv) |

## 🚀 Запуск скрипта

Скрипт запускається через командний рядок.

### 📌 Загальний формат
```shell
python run.py <group> [опції]
```

### 👥 Вибір групи
Одна група
```bash
python run.py group1
python run.py group2
python run.py group3
```

👉 Згенерує календар тільки для обраної групи
***

Всі групи
```bash
python run.py all
```
👉 Згенерує календари для всіх груп (1–8)
***

## ⚙️ Доступні ключі
`--json`
```bash
python run.py group3 --json
```
✔ додатково створює .json файл  
✔ зручно для перевірки даних  
✔ допомагає знайти помилки  

Результат:
```
output/
  group3.ics
data/
  group3.json
```

### Комбінації
```bash
python run.py all --json
```
👉 створить JSON + ICS для всіх груп

## 📂 Де зберігається результат

Після запуску файли `ics` з’являються у папці:
```
output/
```

`json` з’являються у папці:
```
data/
```

Приклад:
```
output/
  group1.ics
  group2.ics
  group3.ics
data/
  group1.json
  group2.json
  group3.json
```

## 🧪 Приклади використання

🔹 Швидкий запуск для групи 3
```bash
python run.py group3
```
🔹 Перевірити дані перед використанням
```bash
python run.py group3 --json
```
🔹 Згенерувати всі календарі
```bash
python run.py all
```

## ⚠️ Типові помилки
❌ Неправильна назва групи
```
python run.py 3
```
👉 неправильно

✔ правильно:
```
python run.py group3
```

❌ Забутий аргумент
```
python run.py
```
👉 скрипт не запуститься

## 💡 Поради

✔ використовуй `--json` при налагодженні  
✔ після перевірки використовуй тільки `.ics`  
✔ можна запускати для всіх груп одразу  

## 🔄 Для автоматичного запуску (GitHub)

У GitHub Actions використовується команда:
```bash
python run.py all
```

## 📌 Коротко
| Команда       | Що робить            |
| ------------- | -------------------- |
| group1        | календар для 1 групи |
| group3 --json | календар + JSON      |
| all           | всі групи            |
| all --json    | всі групи + JSON     |

