### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Repair the Rover 
```python
```
## Step 1
Перепишите и исправьте следующий код. Вот что необходимо сделать:
Пока Агент определяет перед собой **не** блок **AIR**, Агенту нужно дивгаться вправо. Если он обнаружит блок **LAPIS_LAZULI_BLOCK** перед собой необходимо: сдвинуться вправо, повернуть налево и опять сдвинуться вправо. После выполнения цикла, нужно вывести **"Found the break!"** и установить **REDSTONE_BLOCK** перед собой.


```python
def on_chat():
    while (agent.inspect(AgentInspection.Block, FORWARD) == AIR):
    agent.move(RIGHT, 1)
        if agent.inspect(AgentInspection.Block, FORWARD) == LAPIS_LAZULI_BLOCK:
            agent.move(RIGHT, 1)
            agent.turn(RIGHT_TURN)
            agent.move(LEFT, 1)
    player.say("Found the break!")
    agent.setItem(GRASS, 1, 1)
    agent.place(FORWARD)
player.on_chat("repair", on_chat)
```
