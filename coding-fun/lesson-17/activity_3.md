### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration false 
### @explicitHints 1


# Planting Beets!

```python
```

## Step 1
Создай функцию **plantSeed**.
Как ты уже запомнил, в ней ты должен обработать перед собой землю и разместить в нее семена.

## Step 2
Создай функцию **plantSection**.
В ней в цикле ``||loops: for||`` вызывается функция **plantSeed** и агент сдвигается вперед.

## Step 3
Создайте обработчик события ``||player: player.on_chat()||`` и добавьте в нее следующую последовательность команд: 

посадить грядку;

если под агентом блок **LAPIS_LAZULI_BLOCK** повернуться направо, пройти один блок и опять повернуться направо;

иначе если под агентом блок **BLOCK_OF_QUARTZ** повернуться налево, пройти один блок и опять повернуться налево;

посадить еще одну грядку.


```ghost
```python
def plantSeed():
    agent.till(FORWARD)
    agent.place(FORWARD)

def plantSection():
    for i in range(11):
        plantSeed()
        agent.move(FORWARD, 1)

def on_chat():
    plantSection()
    if agent.inspect(AgentInspection.BLOCK, DOWN) == LAPIS_LAZULI_BLOCK:
        agent.turn(TurnDirection.Right)
    elif agent.inspect(AgentInspection.BLOCK, DOWN) == BLOCK_OF_QUARTZ:
        agent.turn(TurnDirection.Left)
player.on_chat("1", on_chat)

```
