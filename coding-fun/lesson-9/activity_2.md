### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Deep Stone 
```python
```
## Step 1
Перепишите и исправьте следующий код. Вот что необходимо сделать:
спускайтесь под поверхность до тех пор, пока не встретите **GOLD_BLOCK** под собой. Пока опускаетесь Агент должен проверять и собирать **STONE** блок.

```python
def on_chat():
    while agent.inspect(AgentInspection.Block, LEFT) == AIR:
        agent.destroy(DOWN)
        agent.move(DOWN, 1)
            if agent.inspect(AgentInspection.Block, FORWARD) != GRASS:
                player.say("Found the stone!")
                agent.destroy(FORWARD)
                agent.collectAll()
player.on_chat("dig", on_chat)
```


