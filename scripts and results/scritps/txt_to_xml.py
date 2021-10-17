import pascal_voc_writer as voc_xml
import os
import sys
import glob


def write_xml_file( main_path):

    saved_path = '/home/lunet/corq/Documents/FYP/DATA/TXTtoXML/xml'
    assert os.path.exists(main_path) ," Path %s Error"%(main_path)
    txt_files=glob.glob(os.path.join(main_path,'*.txt'))

    print('Found %d txt files'%len(txt_files))

    xml_status = False
    # Read txt
    for count,file in enumerate(txt_files):
        data=[]
        txts = [line.rstrip('\n') for line in open(file, 'r')]

        for i,txt in enumerate(txts):
            line = txt.split(',')# file_name, w,h,dim  \n x1,y1,x2,y2,num,conf \n
            if i==0:
                file_name=line[0]
                W=int(line[1])
                H=int(line[2])
                DIM=int(line[3])
            elif i==1:
                xml_status=True
                x1,y1,x2,y2,num,conf=[int(line[0]),int(line[1]),int(line[2]),int(line[3]),int(line[4]),float(line[5])]

                #Write to xml
                #path to relative path
                temp = voc_xml.Writer(file_name, W, H)
                temp.addObject(str(num), x1, y1, x2, y2)

            elif i>1:
                x1,y1,x2,y2,num,conf=[int(line[0]),int(line[1]),int(line[2]),int(line[3]),int(line[4]),float(line[5])]
                temp.addObject(str(num),x1,y1,x2,y2)

        if xml_status:
            temp.save(os.path.join(saved_path,'%s.xml'%os.path.splitext(os.path.basename(file_name.replace('\\',os.sep)))[0]))	
        sys.stdout.flush()
    
    sys.stdout.write('\r Writing xml: %d'%count)
    print('\nDone')
    
    
write_xml_file('/home/lunet/corq/Documents/FYP/DATA/TXTtoXML/txt')
