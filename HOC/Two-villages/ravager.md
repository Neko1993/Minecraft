### @flyoutOnly true
### @hideIteration true
### @explicitHints true

# Introduce the ravager

## Step 1
Help the Villagers meet a ravager. Use the Agent to lead the ravager to each Villager with an arrow above their head.

#### ~ tutorialhint 
Use the ``||hoc2020:lead ravager||`` block to have the ravager follow the Agent forward.  
The ``||hoc2020:turn agent||`` block will turn the Agent either left or right.

```ghost
    hoc2020.leadRavager(0)
    hoc2020.turnAgent(TurnDirection.Left)    
```
```template
//
```
```package
hoc2020-ts=github:rewrite-media/hoc2020-ts#v0.4.0
```
