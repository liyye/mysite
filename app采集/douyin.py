import requests

url='http://v6-dy.bytecdn.cn/928edecd906e523f9a8a0cb8bb1a3125/5d27320e/video/m/220846efc2c304f4e81b32c8c29d99acefe1162d291e00001268fb044f1c/?rc=amdpNTx0eDM5bjMzZmkzM0ApQHRAbzlEODQ0NzYzNDw5PDQ6PDNAKXUpQGczdSlAZjN2KUBmcHcxZnNoaGRmOzRAb29iYV82a15mXy0tLS0vc3M1byNvIzAvMDItLS4tLTAyLi4tLi9pOmIwcCM6YS1xIzpgMG8jYmZoXitqdDojLy5e'
# q=requests.get(url).json()
# print(q['data'][0]['content'])

res = requests.get(url=url)
print(res.content)
with open('dysp1.mp4', 'ab') as f:
    f.write(res.content)








