### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# The great chasm!
```python
```

## Step 1
Напишите обработчик ``||player: player.on_chat()||``, который будет реагировать на сообщение **build**. Для моста используй материал **PLANKS_OAK** и команду ``||agent:agent.place()||``. Не забудь выдать материалы агенту ``||agent: agent.set_item()||``. Используй цикл ``||loops:while <условие>:||``, логическое выражение ``||logik:not||`` и ``||agent:agent.detect()||`` для определения обрыва.

```ghost
def on_chat():
    agent.set_item(PLANKS_OAK, 64, 1)
    while not (agent.detect(AgentDetection.BLOCK, FORWARD)):
        agent.move(FORWARD, 1)
        agent.place(DOWN)
player.on_chat("build", on_chat)

``` 