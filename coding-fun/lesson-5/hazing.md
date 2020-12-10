### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Hazing 

```python
```

## Step 1
Агенту необходимо установить растяжку **TRIPWIRE** что бы волки не смогли ее пройти. Выдайте Агенту необходимый материал используя ``||agent: agent.set_item()||``. Устанавливайте ее под агента используя цикл ``||loops: while||``

#### ~ tutorialhint
Не забудьте про логическое отрицание **not**.

```ghost
```python
def on_chat():
    agent.set_item(TRIPWIRE, 64, 1)
    while not agent.detect(AgentDetection.BLOCK, FORWARD):
        agent.place(DOWN)
        agent.move(FORWARD, 1)
player.on_chat("hazing", on_chat)
```
