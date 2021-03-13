### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration false 
### @explicitHints 1

# Pretty things!


## Step 1
Вам необходимо выложить чередующийся узор по контуру бассейна используя **BLOCK_OF_QUARTZ** и **LAPIS_LAZULI_BLOCK**.
Начните с создания и инициализации заданными блоками переменных ``||variable:blockA||`` и ``||variable:blockB||``.
Также добавьте переменную-счетчик ``||variable:selector||`` для определения текущего блока.

## Step 2
``||logic: if count == 0||`` агент устанавливает под собой ``||variable:blockA||`` и устанавливает **sеlector** значение 1. Иначе ``||variable:blockB||`` и устанавливает **sеlector** значение 0.  

## Step 3
Надеемся Вы помните как двигаться по контуру. Напомним, Вам понадобится ``||loops: for||``, ``||loops: while||``, ``||logic:not||``, ``|| detect||``.

```python
```

```ghost
```python
count = 0
def on_chat():
    for i in range(1):
        while True:
            not agent.detect(AgentDetection.BLOCK, FORWARD)
            agent.set_item(GRASS, 1, 1)
            agent.destroy(FORWARD)
            agent.place(FORWARD)
player.on_chat("1", on_chat)
```
