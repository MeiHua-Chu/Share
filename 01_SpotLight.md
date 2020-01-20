# SpotLight


## Core Spotlight

>= iOS 9.0

通過建立索引的部分，在spotlight上可以呈現出app內的內容

![](https://i.imgur.com/8iQXLsr.png)

### import framework

``` swift
import CoreSpotlight
import MobileCoreServices
```


### 建立SearchItems

``` swift
create SearchItems

let searchableItemAttributeSet =
CSSearchableItemAttributeSet(itemContentType:kUTTypeText as String)
        
// Set the title.
searchableItemAttributeSet.title = title
        
// Set the description.
searchableItemAttributeSet.contentDescription = "Description\(index)"
searchableItemAttributeSet.keywords = [title]
        
searchableItemAttributeSet.phoneNumbers = ["886912886319"]
searchableItemAttributeSet.supportsPhoneCall = true
searchableItemAttributeSet.supportsNavigation = false
searchableItemAttributeSet
        
let data = UIImage(named:"hello")?.pngData()
searchableItemAttributeSet.thumbnailData = data
let searchableItem = CSSearchableItem(uniqueIdentifier: title, domainIdentifier: title, attributeSet: searchableItemAttributeSet)
```

### Insert Items to SpotLight
``` swift
CSSearchableIndex.default().indexSearchableItems(searchableItems) { (error) -> Void in
    if error != nil {
        print(error?.localizedDescription ?? "")
    }
}
```

### 點擊spotlight後移置app裡
>  因swift目前無法試出，故貼上objective-c版本

``` swift
- (BOOL)application:(UIApplication *)application continueUserActivity:(NSUserActivity *)userActivity restorationHandler:(void (^)(NSArray * _Nullable))restorationHandler{
    
    NSString* idetifier = userActivity.userInfo[@"kCSSearchableItemActivityIdentifier"]; 
    if ([idetifier isEqualToString:@"1"]) {
        // open special viewcontroller
    }
    NSLog(@"%@",idetifier);
    
    return YES;
}
```

## SpotLight Extension

刪除你的index跟增加index。重置item

![](https://i.imgur.com/tDmCApV.png)


### create spotlight Extension

File->New->Target->Spotlight Extension

![](https://i.imgur.com/9XiG8Y9.png)

### 重置所有items

```
//重新設置所有item
override func searchableIndex(_ searchableIndex: CSSearchableIndex, reindexAllSearchableItemsWithAcknowledgementHandler acknowledgementHandler: @escaping () -> Void) {
        
    // Reindex all data with the provided index
    CSSearchableIndex.default().deleteAllSearchableItems { (error) in
            
    }
    acknowledgementHandler()
}
```

### 重置items by identifier
```
override func searchableIndex(_ searchableIndex: CSSearchableIndex, reindexSearchableItemsWithIdentifiers identifiers: [String], acknowledgementHandler: @escaping () -> Void) {
    // Reindex any items with the given identifiers and the provided index
    print(identifiers)
    acknowledgementHandler()
}
```

### 替換data
```
override func data(for searchableIndex: CSSearchableIndex, itemIdentifier: String, typeIdentifier: String) throws -> Data {
     // Replace with Data representation of requested type from item identifier
        
     return Data()
}
```

### 替換url
```
    override func fileURL(for searchableIndex: CSSearchableIndex, itemIdentifier: String, typeIdentifier: String, inPlace: Bool) throws -> URL {
        // Replace with to return file url based on requested type from item identifier
        
        return URL(string:"file://")!
    }
```

