# LossLib

In this library implements loss functions witch not in PyTorch.

Usage
~~~
pip install LossLib
~~~

~~~
from LossLib.segmentation import IoULoss

iou = IoULoss()

iou(<predicted_tensor>, <src_tensor>)
~~~

## Loss functions

### Segmentation:

- Dice loss
- Dice BCE loss
- IoU loss
- Focal loss
- Tversky loss
- Focal Tversky loss
- Combo loss

