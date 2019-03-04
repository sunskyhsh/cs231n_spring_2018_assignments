## ReLU & Nesterov Momentum (1 epoch):
lr, val acc
1e-4, 31.8%
1e-3, 50.40%
1e-2, 57.1%

## SeLU & Adam (1 epoch):
1e-4, 45.6%
1e-3, 54.7%
1e-2, 49.8%, 45.8%

## SeLU & Adam (10 epoch):

### conv 16->conv 16->pool->conv 16->conv 16->pool->fc 500->fc
lr=1e-3

```
Starting epoch 0
Iteration 0, loss = 7.5260
Got 114 / 1000 correct (11.40%)

Iteration 700, loss = 1.5615
Got 530 / 1000 correct (53.00%)

Starting epoch 1
Iteration 1400, loss = 1.1664
Got 607 / 1000 correct (60.70%)

Starting epoch 2
Iteration 2100, loss = 0.8663
Got 618 / 1000 correct (61.80%)

Starting epoch 3
Iteration 2800, loss = 0.9813
Got 621 / 1000 correct (62.10%)

Starting epoch 4
Iteration 3500, loss = 0.8096
Got 618 / 1000 correct (61.80%)

Starting epoch 5
Iteration 4200, loss = 0.7160
Got 643 / 1000 correct (64.30%)

Starting epoch 6
Iteration 4900, loss = 0.8628
Got 604 / 1000 correct (60.40%)

Starting epoch 7
Iteration 5600, loss = 0.8975
Got 604 / 1000 correct (60.40%)

Starting epoch 8
Iteration 6300, loss = 0.8366
Got 616 / 1000 correct (61.60%)

Starting epoch 9
Iteration 7000, loss = 0.9675
Got 614 / 1000 correct (61.40%)
```

### conv 32->pool->conv 64->pool->conv 128->pool->fc 4000->fc.
lr=5e-4

```
Starting epoch 0
Iteration 0, loss = 5.6381
Got 138 / 1000 correct (13.80%)

Iteration 700, loss = 1.5179
Got 568 / 1000 correct (56.80%)

Starting epoch 1
Iteration 1400, loss = 1.1150
Got 633 / 1000 correct (63.30%)

Starting epoch 2
Iteration 2100, loss = 1.0101
Got 651 / 1000 correct (65.10%)

Starting epoch 3
Iteration 2800, loss = 0.7236
Got 653 / 1000 correct (65.30%)

Starting epoch 4
Iteration 3500, loss = 0.4902
Got 700 / 1000 correct (70.00%)

Starting epoch 5
Iteration 4200, loss = 1.1561
Got 634 / 1000 correct (63.40%)

Starting epoch 6
Iteration 4900, loss = 1.4028
Got 652 / 1000 correct (65.20%)

Starting epoch 7
Iteration 5600, loss = 0.9994
Got 682 / 1000 correct (68.20%)

Starting epoch 8
Iteration 6300, loss = 0.3580
Got 686 / 1000 correct (68.60%)

Starting epoch 9
Iteration 7000, loss = 0.3109
Got 664 / 1000 correct (66.40%)
```

### conv 16->conv 16->pool->conv 32->conv 32->pool->conv 63->conv64->pool->fc 384->fc 192->fc.

Starting epoch 0
Iteration 0, loss = 10.0711
Got 116 / 1000 correct (11.60%)

Iteration 700, loss = 1.3491
Got 569 / 1000 correct (56.90%)

Starting epoch 1
Iteration 1400, loss = 0.7611
Got 661 / 1000 correct (66.10%)

Starting epoch 2
Iteration 2100, loss = 0.7920
Got 652 / 1000 correct (65.20%)

Starting epoch 3
Iteration 2800, loss = 0.8098
Got 696 / 1000 correct (69.60%)

Starting epoch 4
Iteration 3500, loss = 0.4376
Got 657 / 1000 correct (65.70%)

Starting epoch 5
Iteration 4200, loss = 0.5564
Got 709 / 1000 correct (70.90%)

Starting epoch 6
Iteration 4900, loss = 0.4092
Got 690 / 1000 correct (69.00%)

Starting epoch 7
Iteration 5600, loss = 0.3292
Got 689 / 1000 correct (68.90%)

Starting epoch 8
Iteration 6300, loss = 0.3146
Got 706 / 1000 correct (70.60%)

Starting epoch 9
Iteration 7000, loss = 0.2089
Got 737 / 1000 correct (73.70%)

