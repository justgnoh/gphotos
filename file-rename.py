import json
import os
import datetime

countJSON = 0
countProcessed = 0
countFiles = 0

# Read Json Files
for file in os.listdir("./"):
    countFiles += 1

    if file.endswith(".json"):
        countJSON += 1

        fileInProcessing = file

        try :
            targetJSON = open(file)
            dataJSON = json.load(targetJSON)
            unix = dataJSON["photoTakenTime"]["timestamp"]
            dt = datetime.datetime.utcfromtimestamp(float(unix)+28800) # 28,800 seconds is 8hours (+8GMT for SG)

            fileName = os.path.splitext(dataJSON["title"])[0]
            fileExtension = os.path.splitext(dataJSON["title"])[1]

            targetJSON.close()

            # Find Said File
            if (os.path.exists(dataJSON["title"]) and os.path.isfile(dataJSON["title"])):
                print("File Found... Processing: " + str(fileName))
                countProcessed += 1

                target = dt.strftime('%Y-%m-%d_%H%M%S') + "_" + fileName + fileExtension
                
                # Rename Said File
                os.rename(dataJSON["title"], target)
                
                # Update JSON file
                dataJSON["title"] = target
                jsonFile = open(file, "w+")
                jsonFile.seek(0)
                jsonFile.write(json.dumps(dataJSON))
                jsonFile.close()

                # Rename JSON file
                os.rename(fileName + fileExtension + ".json", target + ".json")
                print("Successfully converted to: " + target)
        except Exception as ex: 
            print("===== Error: " + (fileInProcessing) + "=====")
            print(ex)
            continue

print("countJSON:", countJSON)
print("non JSON Files:", countFiles - countJSON)
print("processed Files:",countProcessed)

