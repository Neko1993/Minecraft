### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1

```python
```
# Locating stone 

## Step 1
Перепишите и исправьте следующий код. Вот что необходимо сделать:
переместитесь влево 4 раза, разруште блок вниз и спуститесь вниз. Если Агент определит **STONE** перед собой, он должен вывести в чат **"Found the stone!"**, разрушить его и собрать. Иначе выведите **"No stone here!"**. Каждый раз после движения вниз, Агент должен подняться вверх, на поверхность. выполните весь код **4** раза.


```python
def on_chat():
    for index in range(3):
        agent.move(RIGHT, 4)
        agent.destroy(DOWN)
        agent.move(DOWN, 1)
        if agent.inspect(AgentInspection.Block, FORWARD) != STONE:
            player.say("Found the stone!")
            agent.destroy(FORWARD)
            agent.collectAll()
        else:
            player.say("No stone here!")
        agent.move(UP, 1)
player.on_chat("stone", on_chat)
```
