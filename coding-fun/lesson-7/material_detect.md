### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1
```python
```

# Detecting your first material

## Step 1
Агенту необходимо собрать золотой блок **GOLD_BLOCK**. Для этого он должен определить что находится перед ним используя ``||agent: agent.inspect()||`` и сравнив результат с **GOLD_BLOCK**. Начните с кода, представленного ниже.
```python
def on_chat():
    while agent.inspect(AgentInspection.BLOCK, FORWARD) != GOLD_BLOCK:
       pass
player.on_chat("material", on_chat)
```

```ghost
def on_chat():
    while agent.inspect(AgentInspection.BLOCK, FORWARD) != GOLD_BLOCK:
        agent.move(LEFT, 1)
    agent.destroy(FORWARD)
    agent.collect_all()
player.on_chat("material", on_chat)
```



