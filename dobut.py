a = '101.26.38.5 111.12.27.88 111.2.122.34 111.2.122.35 111.2.122.36 111.2.122.37 111.2.122.38 111.2.122.39 111.2.122.40 111.2.122.41 111.2.122.42 111.200.33.194 111.47.250.155 111.7.162.10 112.90.148.225 113.108.239.70 116.211.122.104 116.211.122.40 116.211.122.67 116.211.122.69 116.211.122.73 116.211.123.10 116.211.123.206 116.211.123.212 117.139.16.130 117.139.16.131 117.139.16.132 119.188.138.136 119.188.138.38 119.188.138.39 119.188.138.40 119.188.138.99 119.188.140.10 122.228.115.87 122.228.86.19 122.228.86.8 122.228.86.9 123.156.103.34 123.156.103.35 123.156.103.36 123.156.103.37 123.156.103.38 123.156.103.39 123.156.103.40 123.156.103.41 123.156.103.42 123.159.202.40 171.107.87.134 175.6.18.34 175.6.9.70 183.146.211.130 183.146.211.131 183.146.211.132 183.146.211.133 183.146.211.134 183.146.211.135 183.146.211.136 183.146.211.137 183.146.211.138 211.90.28.24 218.58.209.13 218.60.46.179 221.204.172.179 221.204.172.42 221.204.172.43 223.202.204.151 223.202.204.152 223.202.204.154 36.248.8.242 58.216.30.100 58.216.30.101 58.216.30.105 58.216.30.194 58.216.30.195 58.221.69.161 60.28.165.34 60.28.165.36 60.28.165.37 60.28.165.38 60.28.165.39 60.28.165.40 60.28.165.41 60.28.165.42 61.179.105.18 61.240.137.131 61.240.137.132 61.240.137.137 61.240.137.67'.split()
b = '58.216.30.100 116.211.122.69 175.6.10.146 58.221.69.161 218.60.46.179 221.204.172.179 123.159.202.40 223.202.204.151 111.7.162.10 117.169.22.76 '.split()
for i in b:
    if not i in a:
        print(i)