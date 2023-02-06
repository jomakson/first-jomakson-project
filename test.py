import argparse

_file_name = ""
_cnt_i = 10
_cnt_j = 30

def file_write_test():
    parser = argparse.ArgumentParser()

    parser.add_argument('--file_name' )
    parser.add_argument('--cnt_i')
    parser.add_argument('--cnt_j')
    
    args = parser.parse_args()
    
    _file_name_tmp = args.file_name
    _cnt_i_tmp = args.cnt_i
    _cnt_j_tmp = args.cnt_j
    
    print(_file_name_tmp)
    print(_cnt_i_tmp)
    print(type(_cnt_j_tmp))
    
    f = open("numbers.txt", 'w') #_file_name,'w')

    for i in range(1, _cnt_i):
        for j in range(1, _cnt_j):
            f.write(str(j))
        f.write("\n")
    f.close()
    return

def main():
    file_write_test()

if __name__ == "__main__":
    main()