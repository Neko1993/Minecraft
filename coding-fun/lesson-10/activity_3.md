### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Surroundings 
```python
```

## Step 1
Ваша задача собрать руду и драгоценные металы (**IRON_ORE**, **GOLD_BLOCK**, **EMERALD** и **DIAMOND**). Посмотрите внимательно на кольцо Сатурна. Можно ли придумать такой путь, в котором все движения будут в одном цикле?

```ghost
```python
def on_chat():
    while agent.inspect(AgentInspection.Block, DOWN) != PACKED_ICE:
        if agent.inspect(AgentInspection.Block, DOWN) == IRON_ORE or agent.inspect(AgentInspection.Block, DOWN) == GOLD_BLOCK:
            agent.turn(LEFT_TURN)
            agent.destroy(DOWN)
            agent.collectAll()
        if agent.inspect(AgentInspection.Block, DOWN) == DIAMOND or agent.inspect(AgentInspection.Block, DOWN) == EMERALD:
            agent.turn(RIGHT_TURN)
            agent.destroy(DOWN)
            agent.collectAll()
        agent.move(FORWARD, 1)
player.on_chat("3", on_chat)
```

