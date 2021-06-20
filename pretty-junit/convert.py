import xml.etree.ElementTree as ET
import glob
import json
import os

def generate_html(path,reportname="Test Summary"):
    count = 0
    passCount = 0
    failCount = 0
    skipCount = 0
    testSuites = glob.glob(path+"/*.xml")
    testSuites.sort(key=os.path.getmtime)

    suiteData = []
    suiteRow={}
    f = open("./report_template.html", "r")
    suiteTemplateContent = f.read()
    f.close()
    for testsuite in testSuites:
        et = ET.parse(testsuite)
        root = et.getroot()
        suiteRow['name'] = root.get("name").split(".")[-1]
        suiteRow['tests'] = root.get("tests")
        suiteRow['fail'] = root.get("failures")
        suiteRow['skipped'] = root.get("skipped")
        suiteRow['pass'] = str(int(suiteRow['tests']) - (int(suiteRow['fail'])+int(suiteRow['skipped'])))
        suiteRow['passPc'] = str(round(int(suiteRow['pass'])/int(suiteRow['tests'])*100, 2))+" %"
        passCount += int(suiteRow['pass'])
        failCount += int(suiteRow['fail'])
        skipCount += int(suiteRow['skipped'])
        testData = []
        for child in root:
            testRow = {}
            if child.get("name"):
                testRow['name'] = child.get("name")
                if not len(list(child)):
                    testRow['pass'] = "passed"
                    testRow['fail'] = ""
                    testRow['skipped'] = ""
                else:
                    for status in child:
                        testRow['pass'] = ""
                        if status.tag == "failure":
                            testRow['fail'] = "failed"
                            testRow['_children'] = {"error":status.text}
                        elif status.tag== "skipped":
                            testRow['skipped'] = "skipped"
                testData.append(dict(testRow))
                count += 1
                suiteRow['_children'] = testData
            else:
                #print(child)
                pass
        suiteData.append(dict(suiteRow))
    passPc = str(round((passCount/count)*100,2)) +" %"
    failPc = str(round((failCount/count)*100,2)) +" %"
    skipPc = str(round((skipCount/count)*100,2)) +" %"
    f=open(path+"/summary.html","w")
    suiteContent = suiteTemplateContent.replace("var tableData = [];", "var tableData = " + json.dumps(suiteData) + ";")
    suiteContent = suiteContent.replace("Total_Count", str(count)).replace("Failed_Count", str(failCount)+"("+failPc+")")\
        .replace("Passed_Count", str(passCount)+"("+passPc+")").replace("Skipped_Count", str(skipCount)+"("+skipPc+")")
    suiteContent = suiteContent.replace("Report_Name",reportname)
    f.write(suiteContent)
    f.close()
    print("Report Generated Successfully, Summary.html generated at "+ path)