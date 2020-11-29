### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1

```python
```

# Program the Agent to move along the turtle tracks & destroy obstacles!

## Step 1
Напишите обработчик ``||player: player.on_chat()||``, который будет реагировать на сообщение **path**. Для разрушения и сбора блоков используйте ``||agent: agent.destroy()||`` и ``||agent: agent.collectAll()||``. Попробуйте использовать цикл ``||loops: for i in range()||`` для уменьшения количества строк кода.

#### ~ tutorialhint 
Возможные варианты направлений для ``||agent: agent.destroy()||``: **FORWARD** - вперед, **BACK** - назад, **LEFT** - налево, **RIGHT** - направо.

```ghost
```python
def on_chat():
    agent.move(FORWARD, 1)
    agent.turn(LEFT_TURN)
player.on_chat("path", on_chat)
for i in range(4):
    agent.destroy(FORWARD)
    agent.collectAll()
``
``` 