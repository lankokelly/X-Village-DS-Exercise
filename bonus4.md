資料名稱:屏東縣政府警察局建置路口錄監系統設置地點  
資料來源:https://data.gov.tw/dataset/86900  
排序依:Camera lens Quantity(監視器數量)  
主要欄位說明: number(編號)、towns(鄉鎮)、location(路口)、Camera lens Quantity(監視器數量)  
選擇比較排序法: bubble sort 與 cocktail shaker sort    

| sort | bubble sort | cocktail shaker sort |
| ------------- | ------------- | ------------- |
| time | 1.4426124969097323 | 0.003248239774448436 |
| 穩定排序 | 是 | 是 |

資料比數:1631  
說明:cocktail shaker sort 為 bubble sort 的輕微變形，cocktail shaker sort與bubble sort 
不同的地方在於cocktail shaker sort從低到高然後從高到低(雙向)，而氣泡排序則僅從低到高去比較序列裡的每個元素(單向)。
此資料 cocktail shaker sort 比 bubble sort 快，原因是氣泡排序只從一個方向進行比對（由低到高）且每次循環只移動一個項目。
由於選擇排序的資料依據(監視器數量)並不為範圍很大的變數，監視器數量大部分都在5以下，代表其實有部分資料是已被排序的狀態，所以就減少數列交換的動作，
bubble sort在部分被排序的資料上表現較好，如果是大範圍的亂數通常冒泡排序的表現較差，因為數列需要多次的交換，而cocktail shaker sort可以減少交換的輪數，
cocktail shaker sort外層的for迴圈控制排序回合，裡面包含兩個for迴圈，第一個for迴圈從由左向右比較並交換元素，第二個for迴圈由又向左比較並交換元素。
在此，cocktail shaker sort 比 bubble sort 節省約48倍的時間。因此，在大部份資料已經排序好的情況下bubble sort 或 cocktail shaker sort 皆可使用，
而cocktail shaker sort表現比bubble sort更為優秀。



```python
import json
import requests
import timeit

url = 'https://www.pthg.gov.tw/OD.aspx?type=json&u=/Upload/2015pthg/0/relfile/0/0/67fb04ab-d22a-4461-ac64-0f0c52da588e.json'
r = requests.get(url)
r.encoding = 'utf-8' 
data = r.json()
s = 'Camera lens Quantity'
print(len(data))

def bubble_sort(my_list):
    length= len(my_list)
    for i in range(0, length - 1): #有n-1回合
        for j in range(0,length -1 -i): #每回合進行比較的範圍
            if int(my_list[j].get(s)) > int(my_list[j+1].get(s)): 
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

def cocktail_shaker_sort(unsorted):

    for i in range(len(unsorted)-1, 0, -1):
        swapped = False
        
        for j in range(i, 0, -1):
            if int(unsorted[j].get(s)) < int(unsorted[j-1].get(s)):
                unsorted[j], unsorted[j-1] = unsorted[j-1], unsorted[j]
                swapped = True

        for j in range(i):
            if int(unsorted[j].get(s)) > int(unsorted[j+1].get(s)):
                unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
                swapped = True
        
        if not swapped:
            return unsorted

timer_start_bubble_sort = timeit.default_timer()
bubble_sort(data)
timer_end_bubble_sort = timeit.default_timer()
print ("bubble sort :" ,timer_end_bubble_sort - timer_start_bubble_sort)

timer_start_cocktail_shaker_sort = timeit.default_timer()
cocktail_shaker_sort(data)
timer_end_cocktail_shaker_sort = timeit.default_timer()
print ("counting sort :" ,timer_end_cocktail_shaker_sort - timer_start_cocktail_shaker_sort)

```