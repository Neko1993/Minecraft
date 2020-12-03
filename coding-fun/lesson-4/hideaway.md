### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Bamboo Hideaway
```python
```

## Step 1
Запрограммируйте Агента для посадки бамбука  **BAMBOO** на игровой площадке с песком по 3 на сторону.
Используйте обработчик ``||player: player.on_chat()||``, реагирующего на сообщение **sand** и цикл ``||loops: for i in range()||``.

#### ~ tutorialhint
Вы должны использовать 2 вложенных цикла ``||loops: for i in range()||`` для выполнения этого задания.
 
```ghost
```python
def on_chat():
    agent.setItem(BAMBOO, 64, 1)
    for i in range(4):
        for j in range(3):
            agent.place(DOWN)
            agent.move(FORWARD, 1)
        agent.turn(RIGHT_TURN)
player.on_chat("sand", on_chat)
```


