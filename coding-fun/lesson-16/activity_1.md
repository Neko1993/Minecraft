### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Mine the resources!

## Step 1
Вам необходимо добыть все блоки **GOLD_ORE** и **IRON_ORE**. 

Создайте обработчики срабатывающие при следующих сообщениях чате **forward**, **back**, **left**, **right**.
Добавьте параметр в функцию обработчика, отвечающий за количество шагов, для данного действия. Например:
```python
def on_chat(steps):
    agent.move(FORWARD, steps)
player.on_chat("forward", on_chat)
```
Такой подход позволит Вам управлять своим агентом из чата, не редактируя код.

### ~ tutorialHint
Пример запуска кода: **forward 5**


Не забудьте добавить команду **mine**, при которой Агент разрушит блок под собой и соберет полученую руду.

```ghost
```python
def on_chat(steps):
    agent.move(FORWARD, steps)
player.on_chat("forward", on_chat)

def on_chat2(steps):
    agent.move(LEFT, steps)
player.on_chat("left", on_chat2)

def on_chat3(steps):
    agent.move(RIGHT, steps)
player.on_chat("right", on_chat3)

def on_chat4():
    agent.destroy(DOWN)
    agent.collect_all()
player.on_chat("mine", on_chat4)
```


