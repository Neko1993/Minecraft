### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration false 
### @explicitHints 1


# Columns!

```python
```

## Step 1
Время построить акведук! Для начала создайте переменные ``||variable: length||`` и ``||variable: segments||``. Необходимо построить 6 секций по 5 блоков каждый.

## Step 2
Теперь, по команде в чате выполни постройку одной секции. Используй **END_STONE_BRICKS** в качсетве материала. Цикл  ``||loops: for||`` и ``||variable: length||`` помогут тебе сократить количество строк кода. Вода может течь только по желобу, поэтому размещай блоки слева, под и справа от Агента. Не забудь сдвинуться вперед.

## Step 3
Теперь добавь еще один внешний цикл ``||loops: for||`` с указанием количества секций. Перед каждой новой секцией спускайся вниз на один блок.

```ghost
```python
l = 5
s = 6

def on_chat():
    for i in range(s):
        for j in range(l):
            agent.set_item(END_STONE_BRICKS, 64, 1)
            agent.place(LEFT)
            agent.move(FORWARD, 1)
player.on_chat("1", on_chat)

```
