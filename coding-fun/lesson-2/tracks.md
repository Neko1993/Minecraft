### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1

```python
```
# Program the Agent to move along the turtle tracks!

## Step 1
Напишите обработчик ``||player: player.on_chat()||``, который будет реагировать на сообщение **tracks**. Для управления агентом используйте ``||agent: agent.move()||`` или ``||agent: agent.turn()||``. Попробуйте использовать цикл ``||loops: for i in range()||`` для уменьшения количества строк кода
#### ~ tutorialhint 
Возможные варианты направлений для ``||agent: agent.move()||``: **FORVARD** - вперед, **BACK** - назад, **LEFT** - налево, **RIGHT** - направо.

Возможные варианты направлений для ``||agent: agent.turn()||``: **TurnDirection.LEFT** - налево, **TurnDirection.RIGHT** - направо.
```ghost
```python
def on_chat():
    agent.move(FORWARD, 1)
    agent.turn(LEFT_TURN)
player.on_chat("start", on_chat)
for i in range(4):
    pass
``
``` 
