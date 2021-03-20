### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Build a starter house!

## Step 1
Создайте обработчик события, запускающийся при сообщении **house** и имеющий 2 параметра **size** и **height**. Постройте стены дома из **STONE** используя 3 вложенных цикла ``||loops: for i in range()||`` и введенные параметры.

ВНИМАНИЕ: постройте код таким образом, чтобы второй дом Вы построили изменив команду в чате, но не меняя код для Агента

### ~ tutorialHint
Не забудьте передать агрументы функции во время вызова, например:
**house 3 10**

```python
```

```ghost
def on_chat(size, height):
    for i in range(height):
        for j in range(4):
            for k in range(size):
                agent.set_item(STONE, 1, 1)
                agent.place(DOWN)
                agent.move(FORWARD, 1)
            agent.turn(TurnDirection.RIGHT)
        agent.move(UP, 1)
player.on_chat("house", on_chat)

```



