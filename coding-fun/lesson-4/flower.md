### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true
### @explicitHints 1


# Make the area pretty!
```python
```

## Step 1
Ваша задача украсить периметр участка одуванчивами **YELLOW_FLOWER**. По 14  на сторону.
Используйте обработчик ``||player: player.on_chat()||``, реагирующего на сообщение **flower** и цикл ``||loops: for i in range()||``. Постарайтесь выполнить задание за один запуск Агента.

#### ~ tutorialhint 
Не забудьте выдать Агенту ``||agent: agent.set_item()||`` саженцы цветов. 


```ghost
```python
def on_chat():
    agent.setItem(YELLOW_FLOWER, 64, 1)
    for i in range(4):
        for j in range(14):
            agent.place(DOWN)
            agent.move(FORWARD, 1)
        agent.turn(RIGHT_TURN)
player.on_chat("flower", on_chat)
``` 
