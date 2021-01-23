### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Reach magma
```python
```


## Step 1
Запрограммируйте агента спуститься в кратер, пока он не встретит **MAGMA_BLOCK**.


```ghost
```python
def on_chat():
    agent.move(FORWARD, 1)
    while agent.inspect(AgentInspection.Block, DOWN) != MAGMA_BLOCK:
        agent.move(DOWN, 1)
player.on_chat("magma", on_chat)

```

