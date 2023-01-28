import PyPDF2

def main():
    print("Welcome to my low budget PDF extractor")
    filename = input("Please enter the full name of the file you want to extract: ")
    outputFile = open(filename+".txt","w", encoding="utf-8")

    # reading the pdf file
    pdfFileObj = open(filename, 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    # set the starting page and the ending pages we are interested in
    startPage = input("Please enter the data extraction start page: ")
    endPage = input("Please enter the data extraction end page: ")
    text = ""
    
    # read each page and extract the text 
    while startPage < endPage:
        pageObj = pdfReader.pages[startPage]
        startPage +=1
        text = pageObj.extract_text()
        try:
            for line in text:
                outputFile.write(line)
            outputFile.write("\n")
        except:
            print("Error writing to file")

if __name__ == "__main__":
    # calling the main function
    main()