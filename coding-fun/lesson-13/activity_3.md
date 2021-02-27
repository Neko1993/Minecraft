### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Building

```python
```

## Step 1
Выдайте ``||mobs:mobs.give()||`` себе (**NEAREST_PLAYER**) **34** блока изумруда(**EMERALD_BLOCK**). Создайте переменную **count** и проинициализируйте ее равной 0. Каждый раз когда вы ставите ``||blocks:blocks.on_block_placed()||`` блок добавляйте ``||count += 1||`` к переменной единицу и выведите ее в чат не забыв преобразовать в текст ``||player: player.say(str(count))||``. Не забудьте в обработчике события указать что переменная является глобальной.

### ~ tutorialhint 

```python
count = 0
def on_block_placed():
    global count 
    count = count + 1
    player.say(str(count))
blocks.on_block_placed(EMERALD_BLOCK, on_block_placed)
```

```ghost
count = 0
mobs.give(mobs.target(NEAREST_PLAYER), EMERALD_BLOCK, 64)
def on_block_placed():
    global count 
    count = count + 1
    player.say(str(count))
blocks.on_block_placed(EMERALD_BLOCK, on_block_placed)
```


