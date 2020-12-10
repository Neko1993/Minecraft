### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Hazing Two

```python
```

## Step 1
Выдайте агенту растяжку **TRIPWIRE** используя ``||agent: agent.set_item()||``. Используйте цикл ``||loops: while||`` и логическое **not** для выполнения задания.

```ghost
```python
def on_chat():
    agent.set_item(TRIPWIRE, 64, 1)
    while not agent.detect(AgentDetection.BLOCK, FORWARD):
        agent.place(DOWN)
        agent.move(FORWARD, 1)
player.on_chat("hazing", on_chat)
```
