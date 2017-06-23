import xml.etree.ElementTree as ET

# AIMS TO CONVERT FILE TO DICTIONARY. DONE ONLY ONCE. FILE I/O WILL BE REQUIRED AGAIN TO WRITE TO FILE IF KEY IS NOT PRESENT IN DICTIONARY
def convertToDictionary(fileName):

    new_dict = dict()

    with open(fileName, "r") as f:
        data = f.readlines()
        print(type(data))

    counter = 0
    while(counter < len(data)):
        temp = data[counter]
        temp = temp.strip()
        new_dict[temp] = counter
        counter = counter + 1

    #print(new_dict)
    #print(type(new_dict))

    return new_dict

# PARSE XML FILES INDIVIDUALLY AND WRITE TO INDIVIDUAL TXT FILE. SHOULDN'T BE A BIG WORRY IF I FIGURE OUT HOW TO SET UP A HEIRARCHY OF METHODS. OTHER METHOD WOULD SIMPLY ADJUST TO CHECK
#WHETHER WORK EXISTS IN DICTIONARY, IF NOT THEN ADD IT AND THEN WE WILL HAVE TO WRITE OUTPUTS TO OUR TXT FILE CORRESPONDING TO OUR YOLO FILE

# create element tree object
def xmlParser(fileXML, fileResource, data):
    tree = ET.parse(fileXML)

#    print('Hello')
#    print(data)

    root = tree.getroot()

    classify = root[6][0].text
    width = float(root[4][0].text)
    height = float(root[4][1].text)

    xmin = float(root[6][4][0].text)
    ymin = float(root[6][4][1].text)
    xmax = float(root[6][4][2].text)
    ymax = float(root[6][4][3].text)
    '''
    print(classify)
    print(width)
    print(height)

    print(xmin)
    print(ymin)
    print(xmax)
    print(ymax)
    '''
    output2 = ((xmax + xmin) / 2) / width
    output3 = ((ymax + ymin) / 2) / height
    output4 = (xmax - xmin) / width
    output5 = (ymax - ymin) / height


#Check whether dictionary entry exists or not
    if classify in data:
        output1 = data[classify]


    else:
        output1 = len(data) + 1
        data[classify] = output1
        writeToFile(fileResource, classify, data)

    print(output1)
    print(output2)
    print(output3)
    print(output4)
    print(output5)

    st = fileXML[:-4] + ".txt"
#    print(fileXML[:-4])
    with open(st, "w") as f:
        f.write(str(output1))
        f.write("\n")
        f.write(str(output2))
        f.write("\n")
        f.write(str(output3))
        f.write("\n")
        f.write(str(output4))
        f.write("\n")
        f.write(str(output5))
        f.write("\n")



#convertToDictionary('resourceMain.txt')
def writeToFile(fileName, string, data):

    with open("resourceMain.txt", "a") as f:
        f.write(string)
        f.write("\n")



if __name__ == "__main__":

    data = convertToDictionary("resourceMain.txt")
    xmlParser("demoTester.lif", "resourceMain.txt", data)
