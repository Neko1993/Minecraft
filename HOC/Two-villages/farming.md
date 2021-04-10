### @flyoutOnly true
### @hideIteration true
### @explicitHints true

# Building a farm

## Step 1
The Villagers offered to teach the Illagers how to farm, but they need help to prepare the land. Have the Agent till the first 2 rows of dirt.

#### ~ tutorialhint 
The ``||hoc2020:till and move||`` block will till the dirt block below the Agent and then move forward.  
The ``||hoc2020:agent move||`` block will move the Agent in whatever direction you specify.  
The ``||hoc2020:turn agent||`` block will turn the Agent either left or right.  

```ghost
    hoc2020.tillSoil(0)
    hoc2020.moveAgent(SixDirection.Left, 0)
    hoc2020.turnAgent(TurnDirection.Left)  
```
```template
//
```
```package
hoc2020-ts=github:rewrite-media/hoc2020-ts#v0.4.0
```