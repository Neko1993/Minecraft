### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Locate the Sample! 

```python
```

## Step 1
Пока Агент не обнаружил **ICE** продвигаться вниз. Если встречаются блоки на пути - разрушайте их. Не забудьте взять с собой образец голубого льда.

```ghost 
```python
def on_chat():
    while agent.inspect(AgentInspection.Block, DOWN) != ICE:
        agent.destroy(DOWN)
        agent.move(DOWN, 1)
    agent.destroy(DOWN)
    agent.collectAll()
player.on_chat("ice", on_chat)
```

