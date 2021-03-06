### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Make it rain!

```python
```

## Step 1
Вызовите дождь исполнив ритуальный танец дождя!

1. Создайте 3 глобальные логические переменные: **walk**, **jump** и **swim**. Инициализируйте их как **False**.
2. Создайте 3 обработчика событий: **WALK**, **FALL**, **SWIM_WATER**
3. При срабатывании каждого события измените значение соответсвующей переменной на **True**.
4. При сообщении в чат "Rain, rain come again" выполняете проверку: если **walk** и **jump** и **swim** измените погоду на дождливую ``||gameplay: gameplay.set_weather(RAIN)||``


### ~ tutorialHint
Не задубьте что переменные глобальные!


```ghost
```python
walk = False
jump = False
swim = False

def on_travelled_walk():
    global walk
    walk = True
player.on_travelled(WALK, on_travelled_walk)

def on_travelled_fall():
    global jump
    jump = True
player.on_travelled(FALL, on_travelled_fall)

def on_travelled_swim():
    global swim
    swim = True
player.on_travelled(SWIM_WATER, on_travelled_swim)

def on_chat():
    if walk and jump and swim:
        gameplay.set_weather(RAIN)
player.on_chat('rain', on_chat)
```
