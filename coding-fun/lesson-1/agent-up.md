### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1

```python
```
# Запрограммируй Агента двигаться к золотому блоку!

## Шаг 1
Напишите обработчик ``||player: player.on_chat()||``, который будет реагировать на сообщение **up**. Для управления агентом используйте ``||agent: agent.move()||`` или ``||agent: agent.turn()||``.
#### ~ tutorialhint 
Возможные варианты направлений для ``||agent: agent.move()||``: **FORWARD** - вперед, **BACK** - назад, **LEFT** - налево, **RIGHT** - направо, **UP** - вверх, **DOWN** - вниз.

Возможные варианты направлений для ``||agent: agent.turn()||``: **TurnDirection.LEFT** - налево, **TurnDirection.RIGHT** - направо.

```ghost
```python
def on_chat():
    agent.move(FORWARD, 1)
    agent.turn(LEFT_TURN)
player.on_chat("up", on_chat)
```
