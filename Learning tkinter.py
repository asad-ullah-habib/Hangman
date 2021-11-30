main_list = []
n = int(input())
ten_thousands = n / 10000
thousands = (n - (ten_thousands * 10000)) // 1000)
for i in range(ten_thousands + 1):
    main_list.append(10000)

