### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Surroundings 
```python
```

## Step 1
Двигайтесь вперед пока агент видит ``||agent: agent.detect()||``  блок под собой. Если агент определил ``||agent: agent.inspect()||`` блок под собой как воздух **AIR** оповестите командора об этом, написав в чат `` || player: say() || `` сообщение **Crater found!**

```ghost
```python
def on_chat():
    while agent.detect(AgentDetection.Block, DOWN): 
        agent.move(FORWARD, 1)
    if agent.inspect(AgentInspection.Block, DOWN) == AIR:
        player.say("Crater found!")
player.on_chat("1", on_chat)
```