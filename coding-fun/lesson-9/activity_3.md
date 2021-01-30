### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Track Down the Rover 
```python
```

## Step 1
Перепишите и исправьте следующий код. Вот что необходимо сделать:
пока Агент не обнаружит перед собой блок **BLOCK_OF_QUARTZ**, двигаться вперед. Если обнаружит **GOLD_BLOCK** блок под собой необходимо повернуть направо. Если обнаружит **IRON_BLOCK** блок под собой необходимо повернуть налево. В конце необходимо вывести в чат **"Found the rover!"**.


```python
def on_chat():
    while agent.inspect(AgentInspection.Block, FORWARD) != BLOCK_OF_QUARTZ:
            if agent.inspect(AgentInspection.Block, UP) == GOLD_BLOCK:
            agent.turn(LEFT_TURN)
            
            if agent.inspect(AgentInspection.Block, RIGHT) == IRON_BLOCK:
            agent.turn(RIGHT_TURN)
        agent.move(FORWARD, 1)
    player.say("Found the rover!")
player.on_chat("rover", on_chat)
```

