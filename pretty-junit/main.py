import convert
import sys

if __name__ == '__main__':
    try:
        path=sys.argv[1]
        reportname = "Test Summary"
        if(len(sys.argv) == 3):
            reportname=sys.argv[2]
        convert.generate_html(path,reportname)
    except:
        print("Error - Please check the command Usage")
