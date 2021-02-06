### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Surroundings 

```python
```

## Step 1
Необходимо двигаться вдоль правой стены, пока не доберетесь до твердого грунта.

Вам понадобится определять **PACKED_ICE** под собой, двигаться вперед, если справа есть стена и двигаться вправо, если ее нет.




```ghost
```python
def on_chat():
    while agent.inspect(AgentInspection.Block, DOWN) == PACKED_ICE:
        if agent.detect(AgentDetection.Block, RIGHT):
            agent.move(FORWARD, 1)
        else:
            agent.move(RIGHT, 1)
player.on_chat("1", on_chat)
```

