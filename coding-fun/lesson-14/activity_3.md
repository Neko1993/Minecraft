### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Power the portal!
```python
```

## Step 1
Вам нужно нанести удар молнии, ы каждый **GOLD_BLOCK**. Во-первых, вам нужно вызвать ``||gameplay: gameplay.set_weather()||`` дождь **RAIN**. Затем попробуйте использовать ``||logic: if||``, ``||blocks: blocks.test_for_block()||`` и ``||mobs: mobs.spawn()||``, чтобы молния **LIGHTNING_BOLT** ударила точно в нужный момент, выполняйте проверку во время вашего перемещения.


### ~ tutorialHint
Золотые блоки распологаются под вами, в относительных координатах **0, -1, 0**. 
Молния должна быть в вашу позицию, **0, 0, 0**

```ghost
```python
def on_travelled_walk():
    if blocks.testForBlock(GOLD_BLOCK, pos(0, -1, 0)):
        mobs.spawn(LIGHTNING_BOLT, pos(0, 0, 0))
player.on_travelled(WALK, on_travelled_walk)
gameplay.set_weather(RAIN)
```
