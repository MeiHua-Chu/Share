import os
import json

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        
def rootToJson():
    return {
      "info" : {
        "version" : 1,
        "author" : "xcode"
      }
    }
        
def colorToJson(r,g,b,a):
    cJson = {
      "info" : {
        "version" : 1,
        "author" : "xcode"
      },
      "colors" : [
        {
          "idiom" : "universal",
          "color" : {
            "color-space" : "srgb",
            "components" : {
              "red" : str(r),
              "alpha" : str(a),
              "blue" : str(b),
              "green" : str(g)
            }
          }
        }
      ]
    }
    return cJson

rootName = "./Color/output/Color.xcassets/"
createFolder(rootName)
with open(rootName+"Contents.json", 'w') as ofile:
    json.dump(rootToJson(), ofile)
    
with open("Color/input/colors.json","r") as json_file:
    data = json.load(json_file)

    for color in data:
        folderName = rootName+color['name']+".colorset/"
        createFolder(folderName)
        
        r = format(color['color']['r']/255, '0.3f')
        g = format(color['color']['g']/255, '0.3f')
        b = format(color['color']['b']/255, '0.3f')
        a = format(color['color']['a'], '0.3f')
        with open(folderName+"Contents.json", 'w') as outfile:
            json.dump(colorToJson(r,g,b,a), outfile)

