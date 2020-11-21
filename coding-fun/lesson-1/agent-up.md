### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @flyoutOnly 1
### @explicitHints 1


# Запрограммируй Агента двигаться к золотому блоку!

## Шаг 1
Use ``||player:on chat||`` and  ``||agent:agent move||`` commands to program the Agent to move towards the gold plate. You can program the Agent to move **up**. When done, press the **Play** button to compile the code. Go to Minecraft to run your code in game.



```python
player.onChat("up", function () {
    agent.move(FORWARD, 1)
    agent.turn(LEFT_TURN)
})
```