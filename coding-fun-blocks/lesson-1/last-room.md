### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1

# Запрограммируй Агента двигаться к золотому блоку!

## Шаг 1
Запрограммируй агента таким образом, что бы он достиг золотого блока. При этом ты должен оказаться на другом золотом блоке не позже чем через 10 секунд.

```template
player.onChat("run", function () {
})
```

```ghost
player.onChat("run", function () {
    agent.move(FORWARD, 1)
    agent.turn(LEFT_TURN)
})
```