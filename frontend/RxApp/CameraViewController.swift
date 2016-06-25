//
//  CameraViewController.swift
//  RxApp
//
//  Created by Aakanchhya Tamrakar on 6/25/16.
//  Copyright © 2016 Aakanchhya Tamrakar. All rights reserved.
//

import UIKit
import Alamofire
import SwiftyJSON

class CameraViewController: UIViewController, UINavigationControllerDelegate, UIImagePickerControllerDelegate {
    

    @IBOutlet weak var imageView: UIImageView!
    @IBOutlet weak var CameraBtn: UIButton!
    var counter = 0;

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
        var imagePicker: UIImagePickerController!
    @IBAction func CameraButton(sender: UIButton) {
        imagePicker =  UIImagePickerController()
        imagePicker.delegate = self
        imagePicker.sourceType = .Camera
        
        presentViewController(imagePicker, animated: true, completion: nil)
        
        
    }
    func imagePickerController(picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : AnyObject]) {
        imagePicker.dismissViewControllerAnimated(true, completion: nil)
        imageView.image = info[UIImagePickerControllerOriginalImage] as? UIImage
        let imageData = UIImagePNGRepresentation(imageView.image!)
        
        counter += 1
        upload(
            .POST,
            "http://ec2-52-207-209-180.compute-1.amazonaws.com/api/photo",
            multipartFormData: { multipartFormData in
                multipartFormData.appendBodyPart(data: imageData!, name: "userPhoto", fileName: "test\(self.counter).jpg", mimeType: "image/jpeg")

            },
            encodingCompletion: { encodingResult in
                switch encodingResult {
                case .Success(let upload, _, _):
                    upload.progress { (bytesWritten, totalBytesWritten, totalBytesExpectedToWrite) in
                        print("Uploading Image: \(totalBytesWritten) / \(totalBytesExpectedToWrite)")
                        dispatch_async(dispatch_get_main_queue(),{
                            /**
                             *  Update UI Thread about the progress
                             */
                        })
                    }
                    upload.responseJSON { (JSON) in
                        dispatch_async(dispatch_get_main_queue(),{
                            //Show Alert in UI
                            print("Picture uploaded");
                        })
                    }
                    
                case .Failure(let encodingError):
                    //Show Alert in UI
                    print("Avatar uploaded");
                }
            }
        );
    }
    
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
