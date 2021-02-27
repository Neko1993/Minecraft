### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1

# Change the world!
```python
```

## Step 1
Создай переменную **blockID** и инициализируй ее 0. 

Используйте событие срабатывающее при хотьбе ``||player:player.on_travelled()||`` что бы добавить к ID блока **1** и устанавить блок ``||blocks:blocks.place(blockID, world(100, 68, 100))||`` в координатах мира (**100, 68, 100**). 

Используйте событие падения **FALL** для того, чтобы задать значение переменной **blockID** равным 0 и установить этот блок в указанную позицию.

### ~ tutorialhint 
Когда Вы ходите блоки в центре механизма будут изменяться в порядке увеличения их ID.
Когда Вы прыгните ID сбросится в 0.

Не забудьте указать что переменная глобальная для ее использования.


```ghost
```python
blockID = 0
def on_travelled_walk():
    global blockID
    blockID += 1
    blocks.place(blockID, world(100, 68, 100))
player.on_travelled(WALK, on_travelled_walk)

def on_travelled_fall():
    global blockID
    blockID = 0
    blocks.place(blockID, world(100, 68, 100))
player.on_travelled(FALL, on_travelled_fall)
```

