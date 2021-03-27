### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Plant a Seed!
```python
```

## Step 1
Во-первых, передай агенту семена(правой кнопкой по агенту, перемести из своего инвентаря в его).
Затем, создай обработчик события ``||player: player.on_chat()||`` и используй команды обработать ``||agent: agent.till()||`` и ``||agent: agent.place()||`` для посадки семян.

```ghost
```python
def on_chat():
    agent.till(FORWARD)
    agent.place(FORWARD)
player.on_chat("1", on_chat)
```
