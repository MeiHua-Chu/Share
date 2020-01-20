# 模板故事-生成源始碼-gyb

多個重複的程式碼共享同一個結構下，降低維護程式碼的成本。


## install gyb
開啟terminal，輸入以下指令
>$ brew install nshipster/formulae/gyb

## gyb語法
>gyb的基底為python


### %{code}  執行python代碼
```
% with open('colors.json') as json_file:
    % data = json.load(json_file)
    % for row in data:
%{
```

### %code … end. 進行流程控制
```
% for row in data:
.
.
.
%end
```


### ${code} 變數名稱
```
if #available(iOS 11.0, *) {
            return UIColor(named: "${name}")!
        } else {
            return UIColor(hexString: "${hexString}")
        }
```

## Reference
[gyb]https://www.uraimo.com/2016/02/09/a-short-swift-gyb-tutorial/
[gyb]https://juejin.im/post/5d079e50f265da1b667bdc07
[gyb]https://nshipster.cn/swift-gyb/
[stencil]https://github.com/SwiftGen/StencilSwiftKit
[SwiftGen]https://github.com/SwiftGen/SwiftGen#core-data
[R.swift]https://qiita.com/Nick_paper/items/5aeb6fe63a96c7038857


