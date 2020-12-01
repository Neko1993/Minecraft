### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration false 
### @explicitHints 1


# Higher Ground!
```python
```

## Step 1
Запрограммируй Агента строить башню используя **PLANKS_OAK** высотой в 10 блоков. Убедитесь что у Агента есть необходимые материалы или выдайте ему их с помощью ``||agent: agent.set_item()||`` команды. Установите блоки **впереди**, **справа** и **слева** используя ``||agent:agent.place()||``.

#### ~ tutorialhint 
Используйте цикл ``||loop: for i in range()||`` для выполнения задания.

## Step 2
Спуститесь вниз и постройте лестницу **LADDER**.

#### ~ tutorialhint 
Не забудьте выдать агенту необходимые материалы ``||agent: agent.set_item()||``


```ghost
```python
def on_chat():
    agent.move(FORWARD, 1)
    agent.set_item(LADDER, 64, 1)
    for i in range(10):
        agent.place(FORWARD)
        agent.move(UP, 1)
player.on_chat("tower", on_chat)

``` 
