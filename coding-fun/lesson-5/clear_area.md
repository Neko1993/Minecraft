### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Clear the Foliage!

```python
```

## Step 1
Вам требуется разрушить **8х16** блоков листвы. Используйте ``||agent: agent.destroy()||`` для разрушения блоков. 
#### ~ tutorialhint 
Используйте **2** вложенных цикла ``||loops: for i in range()||``


```ghost
```python
def on_chat():
    for i in range(8):
        for i in range(16):
            agent.destroy(FORWARD)
            agent.move(FORWARD, 1)
            agnet.turn(TurnDirection.Left)
player.on_chat("foliage", on_chat)

``` 
