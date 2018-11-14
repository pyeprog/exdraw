# Exdraw, an external drawer for shapely geometry and more..

If you found it too hard to draw shapely geometry within your running server for debugging, try this mini tool.

This is a little tools that can draw shapely geometry using an independent file server. When the server is on, a module named `_probe` will be injected into your working project.
Then you can use:
```python
from _probe.draw_shapely import draw_all_shapley
draw_all_shapely(your_shapely_geometries_list)
```
![plot](imgs/1.png)
And Bang! A nice plot will show up without any side effect caused.
