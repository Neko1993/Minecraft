### @flyoutOnly true
### @hideIteration true
### @explicitHints true

# Building a dock

## Step 1
Build the outside edges of a dock that's 6 blocks long and 4 blocks wide. (Hint: Draw a picture of your dock before you start!)

#### ~ tutorialhint 
The ``||hoc2020:move and place||`` block will move the agent forward and then place a wood plank below.  
The ``||hoc2020:agent move||`` block will move the Agent in whatever direction you specify.  
The ``||hoc2020:turn agent||`` block will turn the Agent either left or right.  

```ghost
    hoc2020.placePlanks(0)
    hoc2020.moveAgent(SixDirection.Left, 0)
    hoc2020.turnAgent(TurnDirection.Left)  
```
```template
//
```
```package
hoc2020-ts=github:rewrite-media/hoc2020-ts#v0.4.0
```