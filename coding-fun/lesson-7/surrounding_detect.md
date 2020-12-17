### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Surroundings 

## Step 1
Следуйте следующему алгоритму:
Пока Агент определяет под собой каменный блок **STONE**, проверить, нет ли перед Агентом преграды, если есть - повернуть влево, иначе двигаться прямо. 

```python
def on_chat():
    while agent.inspect(AgentInspection.BLOCK, DOWN) == STONE:
        pass

player.on_chat("inspect", on_chat)
```

```ghost
def on_chat():
    while agent.inspect(AgentInspection.BLOCK, DOWN) == STONE:
        if agent.detect(AgentDetection.BLOCK, FORWARD):
            agent.turn(TurnDirection.Left)
        else:
            agent.move(FORWARD, 1)

player.on_chat("inspect", on_chat)
```

