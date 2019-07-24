import requests


headers = {
            'Origin': 'https://ww4.hanjutv.com',
            'Referer': 'https://ww4.hanjutv.com/index.php?path=https://meiju4.qfxmj.com/20190216/vaRFOBjB/index.m3u8&f=ck_m3u8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
}

url='blob:https://ww4.hanjutv.com/b330257d-be63-42ec-b891-7b2b46a6b796'
re=requests.get(url,headers=headers)
print(re.content)



























