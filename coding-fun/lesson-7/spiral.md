### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1

```python
```
# Spiral

## Step 1
Следуйте следующему алгоритму:
пока перед Агентом не золотой блок проверять есть ли блок перед нами. Если блок есть, поворачивать налево, иначе двигаться прямо. Не забудь уничтожить блок после завершения цикла.

```ghost
```python
def on_chat():
    while agent.inspect(AgentInspection.BLOCK, FORWARD) != GOLD_BLOCK:
        if agent.detect(AgentDetection.BLOCK, FORWARD):
            agent.turn(TurnDirection.Left)
        else:
            agent.move(FORWARD, 1)
    agent.destroy(FORWARD)
    agent.collect_all()
player.on_chat("spiral", on_chat)
```
