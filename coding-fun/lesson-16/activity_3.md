### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Build a Town Hall!

```python
```

## Step 1
Создайте обработчик события, запускающийся при сообщении **build** и имеющий 3 параметра **width**, **length**, **height**. Постройте стены дома из **STONE** используя 3 вложенных цикла ``||loops: for i in range()||`` и введенные параметры. 

При построении каждого уровня, в цикле считайте что у вас 2 повторения, а не 4. Сами же стены возводите по 2 за раз.


```ghost
```python
def on_chat(width, length, height):
    for i in range(height):
        for j in range(2):
            for k in range(width):
                agent.set_item(STONE, 1, 1)
                agent.place(DOWN)
                agent.move(FORWARD, 1)
            agent.turn(TurnDirection.RIGHT)
            for k in range(length):
                agent.set_item(STONE, 1, 1)
                agent.place(DOWN)
                agent.move(FORWARD, 1)
            agent.turn(TurnDirection.RIGHT)
        agent.move(UP, 1)
player.on_chat("1", on_chat)
```
