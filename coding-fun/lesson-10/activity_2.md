### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Surroundings 


## Step 1
Двигайтесь вдоль правой стенки, пока не обнаружите **PACKED_ICE** под собой. 
Во время движения собирайте образцы **COBBLESTONE** и **GRAVEL**, которые могут оказаться под ногами.

Используйте логическое выражение **OR** для объединения двух условий в одно выражение.


```python
def on_chat():
    while True :
        if agent.inspect(AgentInspection.Block, DOWN) == COBBLESTONE or agent.inspect(AgentInspection.Block, DOWN) == GRAVEL:
            pass
player.on_chat("ice", on_chat)
```

```ghost
```python
def on_chat():
    while agent.inspect(AgentInspection.Block, DOWN) != PACKED_ICE:
        if agent.detect(AgentDetection.Block, RIGHT):
            agent.move(FORWARD, 1)
        else:
            agent.move(RIGHT, 1)
        if agent.inspect(AgentInspection.Block, DOWN) == COBBLESTONE or agent.inspect(AgentInspection.Block, DOWN) == GRAVEL:
            agent.destroy(DOWN)
            agent.collectAll()
player.on_chat("2", on_chat)

```
