### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1

```python
```
# 3d Space

## Step 1
Для решения следующего задания, тебе понадобится запрограммировать агента собрать 2 золотых блока **GOLD_BLOCK**: один в нижнем лабиринте, второй - в верхнем. 
Напиши программу прохождения лабиринта снизу, затем подними агента **на 3 уровня выше** и повтори программу.
```python
def on_chat():
    for i in range(2):
        pass
player.on_chat("3D", on_chat)
``` 

```ghost
def on_chat():
    for i in range(2):
        while agent.inspect(AgentInspection.Block, FORWARD) != GOLD_BLOCK:
            if not agent.detect(AgentDetection.Block, FORWARD):
                agent.move(FORWARD, 1)
            else:
                agent.turn(LEFT_TURN)
        agent.destroy(FORWARD)
        agent.collectAll()
        agent.move(UP, 3)
player.on_chat("3D", on_chat)
```