### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Holodeck 
```python
```

## Step 1
Используйте эту симуляцию, чтобы отточить свои навыки!

```ghost
```python
def on_chat():
    while agent.inspect(AgentInspection.Block, FORWARD) != GOLD_BLOCK:
        if  not agent.detect(AgentDetection.Block, FORWARD):
            agent.move(FORWARD, 1)
        else:
            agent.turn(TurnDirection.LEFT)
    agent.destroy(FORWARD)
    agent.collectAll()
    agent.setItem(GRASS, 1, 1)
    agent.place(FORWARD)
    agent.till(FORWARD)
    agent.collect(IRON_SHOVEL)
    agent.setSlot(1)
    agent.transfer(1, 1, 2)
player.on_chat("3", on_chat)
```