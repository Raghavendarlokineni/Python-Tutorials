from urllib import request

def download_file(url, file_path):
    response = request.urlopen(url)
    
    string = str(response.read())
   
    lines = string.split('\\n')
    
    fw = open(file_path, 'w')
    for line in lines:
        fw.write(line + '\n')
    fw.close()
    
def high_range(stock_details):

    high = 0
    for i in range(len(stock_details)-1):
        num = float(stock_details[i]['Close'])
        if high < num:
            high = num
            index = i
    return index

def low_range(stock_details):

    low = float(stock_details[0]['Close'])
    for i in range(len(stock_details)-1):
        num = float(stock_details[i]['Close'])
        if low > num:
            low = num
            index = i
    return index
    
    
