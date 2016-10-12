"""
New line
"""
print(sum(x for x in [1,-1,2,3] if x > 0))
print([3 * i for i in range(1, 11)])
from collections import Counter
print(Counter("I like cats."))
def get_middle(s):
	return s[(len(s) - 1) / 2 : len(s) / 2 + 1]
print(get_middle("asdfd"))
def get_middle(s):
	return s[(len(s) - 1) / 2 : len(s) / 2 + 1]

'found needle at the position {}'.format(xxx.index('needle'))

import re
def isHKNumber(number):
	return bool(re.match("^\d{4} \d{4}$", number))
def hasHKNumber(number):
	return bool(re.seach("\d{4} \d{4}"), number)
"""
re は「正規表現」
bool() はT/Fを判定する
^ 先頭から
$ 末尾から
\d 数字
"""
def DescendingOrder(num):
	return int("".join(sorted(str(num), reverse = True)))
"""
1234 => 4321
"""
def digitize(n):
    return map(int, str(n)[::-1])
"""
1234 => [4,3,2,1]
"""

isinstance(i, str)
"""
i がstrか判定
"""

import re
def insert_dash(num):
    return re.sub(r'([13579])(?=[13579])', r'\1-', str(num))

a = ['a', 'b']
for i,x in enumerate(a):
	print i,x # 0,'a' 1,'b'
for i,x in enumerate(a,1):
	print i,x # 1, 'a' 2,'b'

def my_parse_int(s):
    try:
        return int(s)
    except ValueError:
        return 'NaN'

def isUpper(word):
	return [i for i, x in enumerate(word) if x.isupper()]

def sort_dict(d):
    return sorted(d.items(), key=lambda x: x[1], reverse=True)

def sumDigits(number):
	return sum(int(d) for d in str(abs(number)))
"""
123 ==> 1 + 2 + 3
"""

def divisors(n):
	return len([i for i in range(1, n + 1) if n % i == 0])

xxx.isdigit()

letters =  {
    "A": "Alpha",  "B": "Bravo",   "C": "Charlie",
    "D": "Delta",  "E": "Echo",    "F": "Foxtrot",
    "G": "Golf",   "H": "Hotel",   "I": "India",
    "J": "Juliett","K": "Kilo",    "L": "Lima",
    "M": "Mike",   "N": "November","O": "Oscar",
    "P": "Papa",   "Q": "Quebec",  "R": "Romeo",
    "S": "Sierra", "T": "Tango",   "U": "Uniform",
    "V": "Victor", "W": "Whiskey", "X": "X-ray",
    "Y": "Yankee", "Z": "Zulu"
  }
  
def nato(word):
    return ' '.join(letters[c] for c in word.upper())

import string
def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())

def add_binary(a,b):
    return bin(a+b)[2:]

def largest(n, xs):
	sorted(xs)[-n:]
"""
(3, [1,2,3,4,4,5]) ==> [5,4,4]
"""
import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))
    # Python 3.4 solution || you don't need to import anything :)
    # return dna.translate(str.maketrans("ATCG","TAGC"))

return int (number * 100) / 100.0
"""
少数第二位以下を切り捨て
"""

str = "Taro, Jiro, Saburo, Hanako"
print str.split(",")
"""
文字列.split("区切り文字")
==> ['Taro', 'Jiro', 'Saburo', 'Hanako']
"""
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))
"""
test.assert_equals(reverse_words('This is an example!'),'sihT si na !elpmaxe');
"""
def order_word(s):
    return "".join(sorted(s)) if s else "Invalid String!"
"""
単語を並び替えする。 accb, ==> ,abcc
"""
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
 """
xoの数が同じなら、True、異なるならFalse
 """

from collections import OrderedDict
def unique(integers):
    return list(OrderedDict.fromkeys(integers))
 """
 OrderredDict 項目が追加された順序を記憶する辞書のサブクラス
この関数は、リストから重複するものを除き、かつ、もとの順序を保持して、リストを返す。
 """

def strong_enough(earthquake, age):
	strength = 1000 * 0.99 ** age
	stockwave = reduce(lambda x, y: x * y, [sum(i) for i in earthquake])
	if strength <= shockwave: return "Needs Reinforcement!"
	return "Safe!"

def solution(string, ending):
	return string.endswith(ending)
"""
 次の構文を使用すると、開始文字・終了文字を調べることができます。

.startswith(検索する文字列, 開始位置, 終了位置)
.endswith(検索する文字列, 開始位置, 終了位置) 
"""
def series_sum(n):
	return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
"""
分母が三ずつ増える分数の足し算で、答えを小数第二位で四捨五入
"""

import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i

 """
回数を数える
 """
