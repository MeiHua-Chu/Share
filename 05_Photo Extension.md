# Photo Extension

## 介紹
可編輯圖片

![](https://i.imgur.com/bVQtX2n.png)

## Sample Code

``` swift
//開始調用
func startContentEditing(with contentEditingInput: PHContentEditingInput, placeholderImage: UIImage)

//完成調用 
func finishContentEditing(completionHandler: @escaping ((PHContentEditingOutput?) -> Void)) 

//詢問是否取消變更
var shouldShowCancelConfirmation: Bool

//取消
func cancelContentEditing()
```
