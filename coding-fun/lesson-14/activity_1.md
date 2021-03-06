### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Pass the dinosaur!

```python
```

## Step 1
Вам необходимо прокрасться(Shift+W) мимо динозавра. Наложите на себя эффект ``||mobs:mobs.apply_effect()||`` невидимости, когда крадетесь, что бы динозавр Вас не заметил. 

### ~ tutorialHint
Доступные виды движения:
**WALK** - ходить, **SWIM_WATER** - плыть в воде, **FALL** - падать, **CLIMB** - взбираться, **SWIM_LAVA** - плыть в лаве, **FLY** - лететь, **RIDING** - ехать, **SNEAK** - красться, **SPRINT** - бежать

Доступные ваиранты эффектов:
**SPEED** - скорость движения, **SLOWNESS** - замедление, **HASTE** - ускорение работ, **STRENGTH** - сила, **JUMP_BOOST** - усиление прыжка, **RESISTANCE** - сопротивление, **FIRE_RESISTANCE** - сопротивление к огню, **WATER_BREATHING** - подводное дыхание, **INVISIBILITY** - невидимость, **NIGHT_VISION** - ночное зрение, **LEVITATION** - левитация 


```ghost
```python
def on_travelled_walk():
    mobs.apply_effect(INVISIBILITY, mobs.target(NEAREST_PLAYER))
player.on_travelled(SNEAK, on_travelled_walk)
```
