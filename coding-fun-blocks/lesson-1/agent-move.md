### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1

# Запрограммируй Агента двигаться к золотому блоку!

## Шаг 1
Напишите обработчик ``||player: при команде чата||``, который будет реагировать на сообщение **up**. Для управления агентом используйте ``||agent: переместиться||`` и ``||agent: повернуться||``.

```template
player.onChat("", function () {
    
})
```

```ghost
player.onChat("start", function () {
    agent.move(FORWARD, 1)
    agent.turn(LEFT_TURN)
})
```