import csv
import os

lan_Hant = 4
lan_Hans = 5
lan_en = 6
lan_ja = 7
lan_vi = 8

lans = [lan_Hant,lan_Hans,lan_en,lan_ja,lan_vi]
language = ["zh-Hant.lproj","zh-Hans.lproj","en.lproj","ja.lproj","vi.lproj"]
lanStr = ["","","","",""]

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def getLocalizableString():
  i = 0
  # 開啟 CSV 檔案
  with open('String/input/字串表.csv', newline='') as csvFile:
  # 1.直接讀取：讀取 CSV 檔案內容
    rows = csv.reader(csvFile)
  # 2.自訂分隔符號：讀取 CSV 檔案內容
    rows = csv.reader(csvFile, delimiter=',')
    for row in rows:
      if i <= 1:
        i+=1
        continue
      if row[3] == "":
        continue
    
      for i in range(0,5):
        s = row[lans[i]]
        
        if s.find("\n") > 0 :
            s = s.replace("\n","\\n")
        if s.find("”") > 0:
            s = s.replace("”","\"")
        #replace \"game Center \" to "game Center ",先將所有的\"換成"
        if s.find("\\\"") > 0 :
            s = s.replace("\\\"","\"")
        #replace " mark to \"
        if s.find("\"") > 0 :
            s = s.replace("\"","\\\"")
        str = "\""+row[3]+"\""+"="+"\""+s+"\";"
#        if "PleaseLoginGameCenter" in row[3]:
#            print(s)
        lanStr[i]+=str
        lanStr[i]+="\n"


getLocalizableString()
for i in range(0,5):
  rootName = "String/output/"+language[i]
  createFolder(rootName)
  fo = open(rootName+"/Localizable.strings", "w")
  fo.write(lanStr[i] )
  fo.close
print("export String success!!")
