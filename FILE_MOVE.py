import os
import shutil
import time
import sys
def select_among(L):
    File_extension=[]
    for i in L:
        if os.path.isfile(i):
            
            index_0=int(i.rindex('.'))
            index_l=int(len(i))
            string_extension=i[index_0:index_l]
            
        if string_extension not in File_extension:
            File_extension.append(string_extension)
    return File_extension # Returning the list containing all the type of extensions (uinque).
def process1():
    List_dir=os.listdir(os.getcwd())
    
    print(List_dir)
    print('Enter the type of File you want to transfer:',end='')
    ABC=select_among(List_dir)
    print('Select among {}.'.format(ABC))
    Typ=input()
    if Typ[0]=='.':
        Name_folder='_Files'
        if Typ=='.txt':
            Grb='TXT'
        elif Typ=='.py' or Typ=='.pyw':
            Grb='Python'
        elif Typ=='.pdf':
            Grb='PDF'
        elif Typ.lower()=='.png' or Typ.lower()=='.jpg' or Typ.lower()=='.jpeg':
            Grb='Image'
        elif Typ=='.exe':
            Grb='Software'
        else:
            Grb='Others'
        Name_folder=Grb+Name_folder
        if os.path.exists(os.getcwd()+'/'+Name_folder)==False:
            os.mkdir(Name_folder)
        
        destination=Name_folder
        c=0
        name_1=sys.argv[0].split('.')
        name=name_1[0] #File name part of "foo.<file-extension>"
        for i in List_dir:
            c+=1
            if i[-len(Typ):].lower()==Typ.lower():
#                print(i[:-len(Typ)],name,'\n',16*'==')
                if i[:-len(Typ)].lower()!=name.lower():
                    try:
                        shutil.move(i,destination)
                        time.sleep(0.2)
                        print('Moved File {} from {} to {}'.format(i,os.path.basename(os.getcwd()),destination))
                    except:
                        pass
        print('Want to Remove some more type of files ?')
        response=input()
        if response.lower()=='yes':
            process1()
        else:
            time.sleep(0.5)
            print('<<<<<<<<<<<<<<<<<<<<<<< Thank you! >>>>>>>>>>>>>>>>>>>>>>>>')
            time.sleep(0.3)
            exit
    else:
        print('\n...................Wrong Type Entered !.................... \nDo you want to try again ?')
        respons=input()
        if respons=='yes':
            process1()
#            continue
        else:
            print('You have Chosen to Exit !')
            time.sleep(0.9)
            print('Exiting.........')
            time.sleep(0.3)
process1()
            
