### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1

```python
```
# Simulation  

## Step 1
Добро пожаловать в симулятор! Запрограммируйте своего агента, чтобы собирать золотые блоки самым оптимальным способом.

```python
def on_chat():
    while agent.inspect(AgentInspection.BLOCK, FORWARD) != GOLD_BLOCK:
        if agent.inspect(AgentInspection.BLOCK, LEFT) == GOLD_BLOCK:
            pass
        if agent.inspect(AgentInspection.BLOCK, FORWARD):
            agent.turn(TurnDirection.Left)            
player.on_chat("simulations", on_chat)
```
```ghost
def on_chat():
    while agent.inspect(AgentInspection.BLOCK, FORWARD) != GOLD_BLOCK:
        if agent.inspect(AgentInspection.BLOCK, LEFT) == GOLD_BLOCK:
            agent.destroy(LEFT)
            agent.collect_all()
        if agent.inspect(AgentInspection.BLOCK, FORWARD):
            agent.turn(TurnDirection.Left)
        agent.move(FORWARD, 1)
    agent.destroy(FORWARD)
    agent.collect_all()
player.on_chat("simulations", on_chat)

```
