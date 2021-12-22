import os,sys
def Alter(file,old_str,new_str):
    """
    Alter string in file
    :param file: Filename with full path
    :param old_str: String to be replaced
    :param new_str: String used when replacing
    :return: None
    """
    file_data = ""
    assert os.path.exists(file),f"File Not Found:{file}"

    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)

def print_help():
    info = """
    run "v2raySwitchL.exe g" to switch v2ray to global mode.
    run "v2raySwitchL.exe n" to switch v2ray to normal mode.
    """
    print(info)

def main():
    if len(sys.argv)==1:
        print_help()
        return -1
    if sys.argv[1].lower().strip()=='g':
        Alter("guiNConfig.json",'"sysProxyType": 0,', '"sysProxyType": 1,')
    elif sys.argv[1].lower().strip()=='n':
        Alter("guiNConfig.json",'"sysProxyType": 1,', '"sysProxyType": 0,')
    ret = os.system("taskkill /F /T /IM v2rayN.exe")
    if 0!=ret:
        print("Wrong status!")
    ret = os.system("start v2rayN.exe")
    return ret

main()
sys.exit(0)