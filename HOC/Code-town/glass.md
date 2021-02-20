### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1


### @hideIteration true 
### @explicitHints 1

```python
```
# Запрограммируй Агента собрать все стекло!

## Шаг 1
Запрограммируйте агента собрать все осколки стекла

```ghost
```python
def on_chat():
    agent.move(FORWARD, 1)
    agent.turn(LEFT_TURN)
    for i in range(5):
        agent.collect_all()
player.on_chat("start", on_chat)
```

https://minecraft.makecode.com/#tutorial:99618-32226-82568-93951 - redstone
https://minecraft.makecode.com/#tutorial:87506-16427-82069-97967 - pool
https://minecraft.makecode.com/#tutorial:50981-03440-94758-45394 - cat
https://minecraft.makecode.com/#tutorial:94776-39825-91289-15654 - glass
https://minecraft.makecode.com/#tutorial:05469-44902-32381-55501 - house

https://minecraft.makecode.com/#tutorial:21994-91329-54350-26336 - spiral, goldblock, staircase