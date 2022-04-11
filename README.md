# shopping

通过模拟用户点击，快速点击【我知道了】【结算】按钮，在【美团买菜】上抢菜。。。

## 效果：

https://www.youtube.com/shorts/zEwL7KAKADw

## 风险： 适配 ios 系统，iphone 需要越狱。小心变砖！！！

android 不支持，不过应该比 ios 更简单，大家可以自行探索下。

## 步骤

1. iphone 手机越狱。[unc0ver](https://unc0ver.dev/)

2. 按照 [zstouch](https://github.com/xuan32546/IOS13-SimulateTouch) 文档，手机安装 zxtouch.

3. 手机，电脑连接至同一局域网下。设置 util.py 中手机端ip

```python
IPHONE_ADDRESS = "192.168.31.70"
```

4. 手机打开美团买菜购物车页面，电脑端执行 python3 meituan.py

5. 兼容性： 以下参数不同手机可能需要做出调整.

```python
# 【我知道了】按钮位置及颜色
OK_POSITION = (400, 1000)
OK_COLOR = (47, 204, 48)

# 【结算】按钮位置及颜色
SUBMIT_POSITION = (700, 1550)
SUBMIT_COLOR = (254, 72, 41)
# SUBMIT_COLOR = (254, 128, 106)

# 【立即支付】按钮位置及颜色
PAY_POSITION = (700, 1670)
PAY_COLOR = (255, 58, 38)

```
