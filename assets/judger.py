import sys
import time
import tb as traceback
from browser import document as doc, window

arr = doc['inputs'].value.split('\n')

is_judger = doc['outputs'].value != ''

def post_message (type, text):
    window.parent.postMessage({
        'type': type,
        'text': text
    }, '*')

def input (*args):
    if len(arr) > 0:
        return arr.pop(0)
    else:
        return ''


def IndentationErrorToZh (err):
    return f'親愛的，第 { err.lineno } 行的位置 { err.text } \n這段程式，似乎發生了縮排錯誤，再檢查看看吧！'

def SyntaxErrorToZh (err):
    return f'親愛的，第 { err.lineno } 行的位置 { err.text } \n這段程式，似乎發生了語法錯誤，再檢查看看吧！'

def nameErrorToZh (err):
    args = str(err).split(' ')
    return f'親愛的，執行中用到了一個名為 {args[1]} 變數，但此變數並不存在。\n可能是變數名稱拼錯 or 未被初始化，再檢查看看吧！'

def TypeErrorToZh (err):
    return f'親愛的，執行的程式似乎出現了型態錯誤！\n可能是在使用加減乘除的運算符號時，兩邊的資料格不符合格式，試著檢查看看吧！'

def IndexErrorToZh (err):
    return f'親愛的，你在讀取可以迭代的對象(串列、字串等)時，\n讀取超過了範圍導致程式錯誤，再檢查看看吧！'

def AttributeErrorToZh (err):
    return f'親愛的，你在執行程式時，對一個對象讀取或執行了不存在的屬性或方法，再檢查看看吧！'

class cOutput:
    encoding = 'utf-8'

    def __init__(self):
        self.cons = doc["console"]
        self.buf = ''

    def write(self, data):
        self.buf += str(data)

    def flush(self):
        self.cons.value += self.buf
        self.buf = ''

    def __len__(self):
        return len(self.buf)

cOut = cOutput()
sys.stdout = cOut
sys.stderr = cOut

doc["console"].value = ''
src = doc["script"].value

start_time = time.perf_counter()

try:
    ns = {'__name__': '__main__' }
    if is_judger: ns['input'] = input
    exec(src, ns)
except IndentationError as err:
    post_message('error', IndentationErrorToZh(err))
    traceback.print_exc(file=sys.stderr)
except SyntaxError as err:
    post_message('error', SyntaxErrorToZh(err))
    traceback.print_exc(file=sys.stderr)
except NameError as err:
    post_message('error', nameErrorToZh(str(err)))
    traceback.print_exc(file=sys.stderr)
except TypeError as err:
    post_message('error', TypeErrorToZh(str(err)))
    traceback.print_exc(file=sys.stderr)
except IndexError as err:
    post_message('error', IndexErrorToZh(str(err)))
    traceback.print_exc(file=sys.stderr)
except AttributeError as err:
    post_message('error', AttributeErrorToZh(str(err)))
    traceback.print_exc(file=sys.stderr)
except Exception as err:
    post_message('error', err)
    traceback.print_exc(file=sys.stderr)

sys.stdout.flush()

if is_judger:
    a = doc['outputs'].value.strip()
    b = doc['console'].value.strip()
    post_message('result', a == b)


end_time = time.perf_counter()
print('<completed in %6.2f ms>' % ((end_time - start_time) * 1000.0))

sys.stdout.flush()
post_message('console', doc['console'].value)
