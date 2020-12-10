### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Cattle

```python
```

## Step 1
Ваша задача провести Агента через поле **без подсчета блоков**. Посмотрите внимательно на возможный путь Агента, если всегда идти прямо до встречи с препятствием. Вам понадобиться цикл ``||loops: while||`` и логическое отлицание **not**. Конечная точка - **золотой блок**.
#### ~ tutorialhint 
Начните со следующего кода. Допишите необходимую часть.
```python
def on_chat():
    while not agent.detect(AgentDetection.BLOCK, FORWARD):
        agent.move(FORWARD, 1)
    agent.turn(TurnDirection.Left)
player.on_chat("sheep", on_chat)
```

```ghost
def on_chat():
    while not agent.detect(AgentDetection.BLOCK, FORWARD):
        agent.move(FORWARD, 1)
    agent.turn(TurnDirection.Left)
player.on_chat("sheep", on_chat)
``` 

