# Xcode Template


## 自定義project/file的模組化版塊，減少重複開發時間
![](https://i.imgur.com/XilnL2r.png)

## Path
>Xcode.app/Contents/Develop/library/Xcode/Templates

| 關鍵字                                   | 意義          |
|:---------------------------------------- | ------------- |
| __FILENAME__                             | File Name     |
| __FILEBASENAMESIDENTIFIER/__FILEBASENAME | class Name    |
| __PROJECTNAME__                          | Project  Name |
| __YEAR__                                 | Year          |
| <# Code #>                               | Highlight     |

## SampleCode

``` swift
//___FILEHEADER___

import UIKit

protocol ___FILEBASENAME___CoordinatorDelegate:class { }

final class ___FILEBASENAMEASIDENTIFIER___ {

    fileprivate let navigationController: UINavigationController
    fileprivate var childCoordinators = [Coordinator]()

    init(with navigationController: UINavigationController) {
        self.navigationController = navigationController
    }

    deinit {
        print("deallocing \(self)")
    }

    func start() {

    }
    
    //navigationController.show(followers, sender: self)
    //navigationController.present(settings, animated: true, completion: nil)
    
    fileprivate func popViewController() {
        navigationController.popViewController(animated: true)
    }

    fileprivate func dismissModal() {
        navigationController.dismiss(animated: true, completion: nil)
    }
}

//When you open ViewController
//extension ___FILEBASENAME___Coordinator : FollowingDelegate {
//
//}


```
 
## Reference
[Xcod TemplateHelper](https://github.com/giftbott/XcodeTemplateHelper)

[Template](https://edit.theappbusiness.com/streamlining-your-development-workflow-with-xcode-templates-b99a73a5b5f8)