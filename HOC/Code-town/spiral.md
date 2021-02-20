### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1


### @hideIteration true 
### @explicitHints 1

```python
```
# Запрограммируй Агента собрать все стекло!

## Шаг 1
Запрограммируйте агента добраться до золотого блока

```ghost
```python
def on_chat():
    agent.move(FORWARD, 1)
    agent.turn(LEFT_TURN)
    for i in range(5):
        agent.collect_all()
player.on_chat("start", on_chat)
```