### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Separated Family!
```python
```


## Step 1
Запрограммируй Агента строить мост через пропасть из **PLANKS_OAK**. Не забудь выдать Агенту необходимые материалы ``||agent: agent.set_item()||``.

#### ~ tutorialhint 
Используй цикл ``||loops:while <условие>:||``, логическое отрицание **not** и ``||agent:agent.detect()||`` для определения обрыва.


```ghost
```python
def on_chat():
    agent.set_item(PLANKS_OAK, 64, 1)
    agent.move(FORWARD, 1)
    while not agent.detect(AgentDetection.BLOCK, FORWARD):
        agent.place(DOWN)
        agent.move(FORWARD, 1)
        agent.turn(TurnDirection.Left)
player.on_chat("family", on_chat)
``` 
