### @codeStart players set @s makecode 0
### @codeStop players set @s makecode 1

### @hideIteration true 
### @explicitHints 1


# Secure the Area

```python
```
## Step 1
Постройте забор **OAK_FENCE** вдоль дороги. Агент будет располагать блок справа от себя, разбивать блок впереди и двигаться вперед. Длина забора 17 блоков.

Используйте обработчик ``||player: player.on_chat()||``, реагирующего на сообщение **fence** и цикл ``||loops: for i in range()||``. Не забудьте выдать Агенту ``||agent: agent.set_item()||`` элементы забора.

```ghost
```python
def on_chat():
    agent.set_item(OAK_FENCE, 64, 1)
    for i in range(17):
        agent.place(RIGHT)
        agent.destroy(FORWARD)
        agent.move(FORWARD, 1)
player.on_chat("fence", on_chat)
``` 

