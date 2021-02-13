### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Planet visit

```python
```
## Step 1
Выберите верный вариант кода что бы выполнить задание. Будьте внимательны, у Вас только одна попытка.


```python
def on_chat():
    for index in range(28):
        if agent.detect(AgentDetection.BLOCK, FORWARD) or agent.detect(AgentDetection.BLOCK, LEFT) or agent.detect(AgentDetection.BLOCK, RIGHT):
            agent.destroy(FORWARD)
            agent.destroy(LEFT)
            agent.destroy(RIGHT)
            agent.collectAll()
        agent.move(FORWARD, 1)
    agent.turn(TurnDirection.Right)
    for index in range(8):
        if agent.detect(AgentDetection.Block, FORWARD) or agent.detect(AgentDetection.Block, LEFT) or agent.detect(AgentDetection.Block, RIGHT):
            agent.destroy(FORWARD)
            agent.destroy(LEFT)
            agent.destroy(RIGHT)
            agent.collectAll()
        agent.move(FORWARD, 1)
    agent.turn(TurnDirection.Right)
    for index in range(24):
        if agent.detect(AgentDetection.Block, FORWARD) or agent.detect(AgentDetection.Block, LEFT) or agent.detect(AgentDetection.Block, RIGHT):
            agent.destroy(FORWARD)
            agent.destroy(LEFT)
            agent.destroy(RIGHT)
            agent.collectAll()
        agent.move(FORWARD, 1)
player.on_chat("1", on_chat)


def on_chat():
    for i in range(10):
        for j in range(4):
            for k in range(4):
                agent.move(FORWARD, 1)
                agent.setItem(PLANKS_OAK, 1, 1)
                agent.place(DOWN)
            agent.turn(TurnDirection.Right)
        agent.move(UP, 1)
player.on_chat("2", on_chat)


def on_chat():
    while agent.inspect(AgentInspection.BLOCK, FORWARD) != GOLD_ORE:
        if agent.detect(AgentDetection.Block, FORWARD):
            agent.destroy(FORWARD)
        if agent.inspect(AgentInspection.Block, DOWN) == GOLD_ORE:
            agent.turn(TurnDirection.RIGHT)
        if agent.inspect(AgentInspection.Block, DOWN) == IRON_ORE:
            agent.turn(TurnDirection.LEFT)
        agent.move(FORWARD, 1)
        player.say("Found Ore Deposit!")
player.on_chat("3", on_chat)
```

```ghost
def on_chat():
    for index in range(28):
        if agent.detect(AgentDetection.BLOCK, FORWARD) or agent.detect(AgentDetection.BLOCK, LEFT) or agent.detect(AgentDetection.BLOCK, RIGHT):
            agent.destroy(FORWARD)
            agent.destroy(LEFT)
            agent.destroy(RIGHT)
            agent.collectAll()
        agent.move(FORWARD, 1)
    agent.turn(TurnDirection.Right)
    for index in range(8):
        if agent.detect(AgentDetection.Block, FORWARD) or agent.detect(AgentDetection.Block, LEFT) or agent.detect(AgentDetection.Block, RIGHT):
            agent.destroy(FORWARD)
            agent.destroy(LEFT)
            agent.destroy(RIGHT)
            agent.collectAll()
        agent.move(FORWARD, 1)
    agent.turn(TurnDirection.Right)
    for index in range(24):
        if agent.detect(AgentDetection.Block, FORWARD) or agent.detect(AgentDetection.Block, LEFT) or agent.detect(AgentDetection.Block, RIGHT):
            agent.destroy(FORWARD)
            agent.destroy(LEFT)
            agent.destroy(RIGHT)
            agent.collectAll()
        agent.move(FORWARD, 1)
player.on_chat("1", on_chat)


def on_chat():
    for i in range(10):
        for j in range(4):
            for k in range(4):
                agent.move(FORWARD, 1)
                agent.setItem(PLANKS_OAK, 1, 1)
                agent.place(DOWN)
            agent.turn(TurnDirection.Right)
        agent.move(UP, 1)
player.on_chat("2", on_chat)


def on_chat():
    while agent.inspect(AgentInspection.BLOCK, FORWARD) != GOLD_ORE:
        if agent.detect(AgentDetection.Block, FORWARD):
            agent.destroy(FORWARD)
        if agent.inspect(AgentInspection.Block, DOWN) == GOLD_ORE:
            agent.turn(TurnDirection.RIGHT)
        if agent.inspect(AgentInspection.Block, DOWN) == IRON_ORE:
            agent.turn(TurnDirection.LEFT)
        agent.move(FORWARD, 1)
        player.say("Found Ore Deposit!")
player.on_chat("3", on_chat)
```

