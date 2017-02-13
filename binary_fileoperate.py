#!/usr/bin/python3
"""demonstrates binary file read/write operations with python3"""

def main():

    #rb - reads the file in binary format
    fin = open("pdf.pdf", "rb")
 
    #wb - writes to the file in binary format
    fout = open("copy_pdf.pdf", "wb")
    size = 1000

    #copies the text from the file of "size" each time 
    text = fin.read(size)

    while len(text):
        fout.write(text)
        text = fin.read(size)
    print("copy done")

if __name__ == "__main__" : main()
