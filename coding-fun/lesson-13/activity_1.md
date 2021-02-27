### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Lava swim

```python
```

## Step 1
Вам необходимо установить сопротивление огню. 

Используйте событие ``||player:player.on_travelled()||`` и вид движения **SWIM_LAVA**.
Примените эффект сопротивления огню ``||mobs:mobs.apply_effect()||`` на ближайшего игрока ``||mobs:mobs.target(NEAREST_PLAYER)||``.

```python
mobs.apply_effect(FIRE_RESISTANCE, mobs.target(NEAREST_PLAYER))
```


```ghost

def on_travelled_walk():
    mobs.apply_effect(FIRE_RESISTANCE, mobs.target(NEAREST_PLAYER), 10)
player.on_travelled(WALK, on_travelled_walk)
```
