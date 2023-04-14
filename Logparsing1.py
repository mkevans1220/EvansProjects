#fullstack practice activity dns log 


#Printing a list of all Ips contained in the dns.log file
Every_ip = []
with open("/Users/chellemarshae/Downloads/dns.log","r") as f:
    var = f.readline()
    my_list = var.split()
    print(my_list[1])
    for l in f:
        Ip = l.split()[1]
        if Ip not in Every_ip:
            Every_ip.append(Ip)
print(Every_ip)