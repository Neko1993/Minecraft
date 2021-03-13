### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration false 
### @explicitHints 1


# Mining Quartz!

```python
```

## Step 1
Напиши программу, которая **вычислит** количество блоков необходимых для постройки колонн. Данные необходимые для рассчета: **высота** колонн 6, **количество** колонн 6. Начни рассчет с объявления и инициализации переменных: ``||variable:height||``и ``||variable:quantity||``. Также объяви переменную ``||variable:total||`` для рассчитанного количества блоков. 

## Step 2
Объяви обработчик события: блок **PILLAR_QUARTZ_BLOCK** сломан. Добавляй единицу к переменной ``||variable:total||`` и выводи текущее значение на экран ``||player: player.say()||``, если происходит это событие.

## Step 3
После изменения ``||variable:total||`` добавь проверку ``||logic: if||``. Если собрано достаточное количество блоков, то выведи в чат сообщение: **"Collected enough blocks!"**.

```ghost
```python
h = 6
k = 6
count = 0

def on_block_broken():
    global count, h, k
    count += 1
    player.say(str(count))
    if count == h*k:
        player.say("Collected enough blocks!")
blocks.on_block_broken(PILLAR_QUARTZ_BLOCK, on_block_broken)
```
