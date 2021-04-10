### @flyoutOnly true
### @hideIteration true
### @explicitHints true

# Lay down some rails

## Step 1
Create an easier way to travel between both towns by placing minecart rails through the tunnel.

#### ~ tutorialhint 
The ``||hoc2020:place rail below||`` block will place a rail under the Agent.  
The ``||hoc2020:agent move||`` block will move the Agent in whatever direction you specify.   
The ``||hoc2020Different:repeat||`` block will allow you to repeat a set of blocks multiple times.  

```ghost
    hoc2020.placeRails()
    hoc2020.moveAgent(SixDirection.Left, 0)
    hoc2020Different.customRepeatLoop(0, () => {})
```
```template
//
```
```package
hoc2020-ts=github:rewrite-media/hoc2020-ts#v0.4.0
```