

def main():
    total = 0.0

    try: 
        infile = open('text'.txt,'r')

        for line in infile: 
            amount = float(line)
            total += amount 

            infile.close() 

        print(format(total, ".2f"))

        
    except:
        print("AN ERROR OCCURED!!!")




main() 

