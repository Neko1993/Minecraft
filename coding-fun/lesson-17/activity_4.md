### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration false 
### @explicitHints 1


# Beets!

```python
```

## Step 1
Создай функцию **plantSeed**.
Как ты уже запомнил, в ней ты должен обработать перед собой землю и разместить в нее семена.

## Step 2
Создай функцию **plantSection**.
В ней в цикле ``||loops: for||`` вызывается функция **plantSeed** и агент сдвигается вперед.

## Step 3
Создайте функцию **agentTurn**.
Проверяйте, если под агентом блок **LAPIS_LAZULI_BLOCK**, то поворачивайте вправо, иначе если блок **BLOCK_OF_QUARTZ** поворачивайте влево.

## Step 4
Создайте обработчик ``||player: player.on_chat()||``.
Продолжайте засеивать секлу, пока не обнаружите **GOLD_BLOCK**.

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