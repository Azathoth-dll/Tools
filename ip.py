switch = 1
while(switch):
    
    # input info
    print("input ip address to transfer ip\ninput 'quit' to quit\n")
    Option = input("Options:")
    
    # quit
    if(Option == "quit"):
        switch = 0
    
    # ip to int
    else:
        
        #ip format judgement
        original_ip = Option
        if(original_ip.count('.') != 3):
            print("ILLEGAL IP! Error_01")
            continue
        
        #ip devision
        original_ip = original_ip.split('.',3)
        
        #ip format judgement
        if (not (original_ip[0].isdigit() and original_ip[1].isdigit() and original_ip[2].isdigit() and original_ip[3].isdigit())):
            print("ILLEGAL IP! Error_02")
            continue
        
        #ip to int
        int_original_ip = [0,0,0,0]
        judge = 0
        for i in range(0,4):    
            int_original_ip[i] = int(original_ip[i])

            # ip range judgement
            if(int_original_ip[i] > 255 or int_original_ip[i] < 0):
                print("IP Address Out of Range! Error_03")
                judge = 1
        if judge == 1:
            continue
        
        # ip to binary
        binary_ip = [[],[],[],[]]
        line_binary_ip=[]
        str_binary_ip = [[],[],[],[]]
        for i in range(0,4):
            binary_ip[i] = list(bin(int_original_ip[i])[2:])
            length = len(binary_ip[i])
            
            while(length < 8):
                binary_ip[i].insert(0,0)
                length = length + 1
            
            str_binary_ip[i] = "".join([str(x) for x in binary_ip[i]])
            i=i+1
        print("{}{}{}{}".format(str_binary_ip[0],str_binary_ip[1],str_binary_ip[2],str_binary_ip[3]))
        for i in range(0,4):
            for x in binary_ip[i]:
                line_binary_ip.append(int(x))
        #print(line_binary_ip)
        
        # progress control
        control = 1
        while (control):
            Option = input("Input 'next' for next ip transfering\nInput 'x' for subnet mask, while x is a number in range[1,32)\n")
            if (Option == "next"):
                control = 0
            else:
                
                # sub_ip to binary
                sub_ip = Option
                if(not (sub_ip.isdigit())):
                    print("ILLEGAL Input! Error_04")
                    continue
                length = int(sub_ip)
                if(length > 31 or length < 1):
                    print("ILLEGAL Input! Error_05")
                    continue
                int_sub_ip = []
                for i in range(0,32):
                    if(i < length):
                        int_sub_ip.append(1)
                    else:
                        int_sub_ip.append(0)
                #print(int_sub_ip)
                and_ip = []
                for i in range(32):
                    and_ip.append(int(line_binary_ip[i] and int_sub_ip[i]))
                string_and_ip = "".join([str(x) for x in and_ip])
                print(string_and_ip)
