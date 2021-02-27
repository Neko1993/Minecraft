### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# The Climb

```python
```

## Step 1
Используйте бесконечный цикл ``||loops:while True||``, чтобы накладывать эффект усиливыющий прыжок **JUMP_BOOST**. Не забудьте снять эффект ``||mobs:clear_effect(mobs.target(NEAREST_PLAYER))||`` перед следующей итерацией


```ghost
```python
while True:
    mobs.apply_effect(JUMP_BOOST, mobs.target(NEAREST_PLAYER), 10)
    mobs.clear_effect(mobs.target(NEAREST_PLAYER))
```
