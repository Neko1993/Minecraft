### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Locate the cub!

```python
```

## Step 1
Напиши программу для Агента, которая прорубит путь сквозь завал. Используй ``||player: player.on_chat()||`` и команду **cub**. Что бы определить конец завала тебе понадобится цикл ``||loops:while <условие>:||`` и ``||agent:agent.detect()||`` комнады. Незабывай передвигаться вперед при помощи ``||agent:agent.move()||`` 

#### ~ tutorialhint 
Возможные варианты направлений для ``||agent: agent.move()||``: **FORWARD** - вперед, **BACK** - назад, **LEFT** - налево, **RIGHT** - направо, **UP** - вверх, **DOWN** - вниз.

Возможные варианты направлений для ``||agent: agent.destroy()||``: **FORWARD** - вперед, **BACK** - назад, **LEFT** - налево, **RIGHT** - направо, **UP** - вверх, **DOWN** - вниз.


```ghost
```python
def on_chat():
    while agent.detect(AgentDetection.BLOCK, FORWARD):
        agent.destroy(FORWARD)
        agent.move(FORWARD, 1)
        agent.destroy(UP)
player.on_chat("cub", on_chat)
``` 