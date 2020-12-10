### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Chicken Coup

```python
```

## Step 1
Вам требуется установить металическую сетку **IRON_BARS** на 2 уровня выше. Одна сторона ограждения имеет длину **9** блоков. Помните, что у вас **4** стороны. Используйте цикл ``||loops: for i in range()||``.

#### ~ tutorialhint
В конечном итоге у вас должно получиться **3** вложеных цикла ``||loops: for i in range()||`` (длина, ширина и высота). Не забудьте выдать Агенту стоительные материалы ``||agent: agent.set_item()||``, их потребуется больше 64.


```ghost
```python
def on_chat():
    for i in range(2):
        agent.set_item(IRON_BARS, 64, 1)
        for j in range(4):
            for k in range(9):
                agent.place(DOWN)
            agent.turn(TurnDirection.RIGHT)
player.on_chat("chicken", on_chat)

``` 
