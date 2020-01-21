#  Color 的匯出檔案
使用美術匯出的colors.json經由assetsColor.py及Color.swift.gyb匯出成.swift及.xcassets的檔案供程式使用。

## color.swift.gyb
自動匯出swift的檔案,若project支援iOS 11.0以上後，可略過此檔案。
匯出時請使用Command line輸入 
` gyb color.swift.gyb -o color.swift`
成功後會匯出color.swift的檔案，若尚未安裝gyb請參考
[link] https://www.uraimo.com/2016/02/09/a-short-swift-gyb-tutorial/

．若json格式有變動請修改line 15及line 16改變取得的名字及argb的hex值。

## color.swift
gyb匯出的檔案.直接將此檔拖曳至XCode。若project支援iOS 11.0以上後，可略過此檔案
 
 ## assetColor.py
 使用json檔案匯出成xcode的assets的檔案. 匯出的檔案為Color.xcassets。
 直接將檔案拖曳至Xcode既可。

## Color.xcassets
assetColor.py匯出的檔案，直接將檔案拖曳至Xcode既可。
