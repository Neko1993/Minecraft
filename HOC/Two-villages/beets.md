### @flyoutOnly true
### @hideIteration true
### @explicitHints true

# Protect the beets

## Step 1
Something keeps getting into the garden and taking beets. Have the Agent build a fence around the farm to keep the beets safe.

#### ~ tutorialhint 
The ``||hoc2020:place iron bars down||`` block will place an iron bar below the Agent.  
The ``||hoc2020:agent move||`` block will move the Agent in whatever direction you specify.  
The ``||hoc2020:turn agent||`` block will turn the Agent either left or right.  
The ``||hoc2020Different:repeat||`` block will allow you to repeat a set of blocks multiple times.


```ghost
    hoc2020.placeFence()
    hoc2020.moveAgent(SixDirection.Left, 0)
    hoc2020.turnAgent(TurnDirection.Left)  
    hoc2020Different.customRepeatLoop(0, () => {})
```
```template
//
```
```package
hoc2020-ts=github:rewrite-media/hoc2020-ts#v0.4.0
```