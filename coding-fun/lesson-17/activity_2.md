### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Build a Town Hall!

```python
```

## Step 1
Создай собственную функцию **plantSeed** и размести в нее тот же код, что и напредыдущем задании. Она поможет тебе упростить код и сделать его более читаемым. Добавь обработчик события ``||player: player.on_chat()||``. Внутри функции используй цикл  ``||loops: for||`` и вызов твоей функции **plantSeed** чтобы посадить грядку.

### ~ tutorialHint
Для вызова функции используйте имя функции и круглые скобки.



```ghost
```python
def plantSeed():
    agent.till(FORWARD)
    agent.place(FORWARD)

def on_chat():
    for i in range(11):
        plantSeed()
        agent.move(FORWARD, 1)
player.on_chat("1", on_chat)
```
