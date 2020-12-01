### @hideIteration true 
### @explicitHints 1

# Separated Family!

```python
```

## Step 1
Напишите свой код

```ghost
```python
def on_chat():
    agent.move(FORWARD, 1)
    agent.turn(TurnDirection.Left)
    for i in range(1):
        agent.place(FORWARD)
    while not agent.detect(AgentDetection.BLOCK, FORWARD):
        agent.set_item(GRASS, 1, 1)
player.on_chat("jump", on_chat)

```