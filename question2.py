import os

def fix_filename(path,wrong,correct):
    
    for r,d,f in os.walk(path):

        if wrong in r:
            
            for file in f:
                if wrong in file:
                    fixed = file.replace(wrong,correct)
                    os.rename(f'{r}/{file}',f'{r}/{fixed}')

            dir_fixed = r.replace(wrong,correct)
            os.rename(f'{r}',f'{dir_fixed}')
if __name__ == '__main__':

    fix_filename('./temp','ATCC17978','ATCC10231')