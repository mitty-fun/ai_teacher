challenges = [
  {
    'description':  '錯誤測試：變數沒有命名\n題目要求：輸入一個數字 N，並使用迴圈印出 1, 2, 3, 4 ... N',
    'inputs': '5',
    'outputs': '1\n2\n3\n4\n5',
    'code': 'def a ():\n    print(1)\ndef b ():\n    print(2)\ndef c ():\n    print(orange)\ndef d ():\n    print(4)\ndef e ():\n    print(5)\na()\nb()\nc()\nd()\ne()'
  },
  {
    'description': "錯誤測試：縮排測試\n輸入兩個數值，如果第一個比較大印出「a比較大」\n如果第二個比較大印出「b比較大」\n一樣則印出「一樣大」",
    'inputs': '10\n20',
    'outputs': 'b比較大',
    'code': "a = int(input())\nb = int(input())\n\nif a > b:\n    print('a比較大')\nelif a < b:\nprint('b比較大')\nelse:\n    print('一樣大')"
  },
  {
    'description': "錯誤測試：語法錯誤\n輸入一個數字密碼，如果密碼是 1234567890 就印出「密碼正確」反之印出「密碼錯誤」",
    'inputs': '1234567890',
    'outputs': '密碼正確',
    'code': "pwd = input('password')\n\nif pwd = '1234567890':\n    print('密碼正確')\nelse:\n    print('密碼錯誤')"
  },
  {
    'description': "錯誤測試：型態錯誤\n輸入兩個數值，相乘後印出",
    'inputs': '10\n20',
    'outputs': '200',
    'code': "a = input('除數')\nb = input('被除數')\n\nprint(a * b)"
  },
  {
    'description': "錯誤測試：讀取不存在的屬性或方法\n將字串用空白符號切割，並轉成串列印出",
    'inputs': 'orange 2020 apple',
    'outputs': "['orange', '2020', 'apple']",
    'code': "s = input()\nprint(s.plit())"
  }
]