### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1


### @hideIteration true 
### @explicitHints 1

```python
```
# Запрограммируй Агента построить дом!

## Шаг 1
Запрограммируйте агента построить дом из блоков **PLANKS_ACACIA**

```ghost
```python
def on_chat():
    agent.set_item(PLANKS_ACACIA, 1, 1)
    agent.move(FORWARD, 1)
    agent.turn(LEFT_TURN)
    agent.place(FORWARD)
    for i in range(5):
        agent.collect_all()
player.on_chat("start", on_chat)
```

