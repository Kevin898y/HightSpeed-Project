# LINE 超商商品訂購及分類系統

## 系統需求
* Keras(2.2.4)
* kashgari(0.2.3)
* tensorflow-gpu (1.13.1)
* Python(3.6.7)
* Django(2.2)

## Tutorials

###執行程式

* 用`Label.ipynb` 產生Training data
* 用`NER.ipynb` 訓練Named-entity recognition model
* 用`FindOrder.ipynb`找出訂單
* 將`FindOrder.ipynb`產生的`Order.csv`放入High_Speed_Project/Web/LineOrderSystem

### 開啟網頁

```
cd High_Speed_Project/Web/LineOrderSystem
python3 manage.py runserver  0.0.0.0:8000
```

