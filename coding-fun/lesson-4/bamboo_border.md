### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Bamboo Border

## Step 1
Ваша задача посадить бамбук по периметру участка. По 16 саженцев на сторону.
Используйте обработчик ``||player: player.on_chat()||``, реагирующего на сообщение **bamboo** и цикл ``||loops: for i in range()||``. Не забудьте выдать Агенту ``||agent: agent.set_item()||`` саженцы бамбука. Постарайтесь выполнить задание за один запуск Агента.

#### ~ tutorialhint 
Начните со следующего кода. Исправьте в нем ошибки и допишите необходимую часть.
```python
def on_chat():
    agent.set_item(BAMBOO, 64, 1)
    for i in range(6):
        agent.place(UP)
        agent.move(FORWARD, 1)
    agent.turn(TurnDirection.Left)
player.on_chat("bamboo", on_chat)
```

```ghost
def on_chat():
    agent.set_item(BAMBOO, 64, 1)
    for i in range(6):
        agent.place(UP)
        agent.move(FORWARD, 1)
    agent.turn(TurnDirection.Left)
player.on_chat("bamboo", on_chat)
```