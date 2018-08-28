# Лотерея "Охота на яблоки" в Hookah Place Уфа, 2018

`participants.csv`: список участников, номер карты и количество лотерейных билетов

`lottery.py`: скрипт лотереи

Для того, чтобы процесс выбора победителей был честный и прозрачный, мы используем библиотеку random, которая может генерировать случайные последовательности значений с учетом их "веса". Также эта библиотека позволяет повторить процесс розыгрыша, за счет чего любой желающий может запустить программу и убедиться в точности результатов.
Это достигается за счет того, что библиотека использует заранее заданную seed строку в качестве элемента случайности.

В качестве этого параметра seed мы будем использовать хеш первого блока биткоина, который появится после полуночи 00:00 GMT+5 первого сентября (после 19:00 GMT+0)
Его можно будет найти по ссылке https://www.blockchain.com/btc/blocks/1535709597281

Для примера, первый блок за 28 августа по уфимскому времени имеет хеш 0000000000000000001ca03d9e1dd30d2cf49e44ba1569c8819e56cef88b67d4, что можно наблюдать по ссылке https://www.blockchain.com/btc/blocks/1535363997281 (2018-08-27 19:01:07 GMT+0 = 2018-08-28 00:01:07 GMT+5)

```python
# Use bitcoin hash at height 538770.
python3 lottery.py 0000000000000000001ca03d9e1dd30d2cf49e44ba1569c8819e56cef88b67d4
```
