//
//  ShareViewController.swift
//  share
//
//  Created by chu hua on 2019/11/8.
//  Copyright © 2019 hua. All rights reserved.
//

import UIKit
import Social

class ShareViewController: SLComposeServiceViewController {

    override func isContentValid() -> Bool {
        // Do validation of contentText and/or NSExtensionContext attachments here
        return true
    }

    override func didSelectPost() {
        
        
        guard let item : NSExtensionItem = self.extensionContext?.inputItems.first as? NSExtensionItem else{
            return
        }
        print("content:\(item.attributedContentText?.string ?? "" )")
    
        if item.attachments?.count ?? 0 > 0{
            for prodiver : NSItemProvider in item.attachments ?? []{
                if prodiver.hasItemConformingToTypeIdentifier("public.url"){
                    prodiver.loadItem(forTypeIdentifier: "public.url", options: nil) { (object , error) in
                        if let url = object as? NSURL {
                            // we found our URL, start sending!
                            print("URL:\(url.absoluteString ?? "")")
                        }
                        else {
                            print("error")
                        }
                    }
                }
            }
        }

    //通知宿主程序的扩展已完成请求。调用此方法后，扩展UI会关闭并返回容器程序中。其中的items就是返回宿主程序的数据项。
        self.extensionContext!.completeRequest(returningItems: [], completionHandler: nil)
    }

    override func configurationItems() -> [Any]! {
        // To add configuration options via table cells at the bottom of the sheet, return an array of SLComposeSheetConfigurationItem here.
        return []
    }

}
