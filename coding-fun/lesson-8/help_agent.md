### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Iron
```python
```

## Step 1
Запрограммируйте агента двигаться вперед пока он не встретит **IRON_ORE**. Если на пути попадутся преграды - разруште их. Не забудьте собрать образец железной руды.
```ghost
```python
def on_chat():
    while agent.inspect(AgentInspection.Block, DOWN) != IRON_ORE:
        if agent.detect(AgentDetection.Block, FORWARD):
            agent.destroy(FORWARD)
        agent.move(FORWARD, 1)
    player.say("Found the iron ore!")
    agent.destroy(DOWN)
    agent.collectAll()
player.on_chat("4", on_chat)
```
