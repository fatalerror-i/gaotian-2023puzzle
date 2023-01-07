# %% [markdown]
# + 对B站UP[【码农高天】](https://space.bilibili.com/245645656)的新年puzzle[【这个两分钟的新年谜题，你两个小时解得开么？】](https://www.bilibili.com/video/BV1314y1A7x2)的个人解答。
# + 时间：2023.01.05
# + 版本：Python 3.8

# %% [markdown]
# # 0x00
# + 谜面
#   + 解说：人生，是一段连续的旅程。你刚刚做的决定，就会是你下一段旅程的开端。
#   + 文字：（上述文字）
# + 解释
#   + 上一关的谜底会作为下一关的输入。

# %% [markdown]
# # 0x01
# + 谜面
#   + 解说：而程序员的人生，其实很简单。答案常常就在这16个数里。
#   + 文字：0123456789abcdef
# + 解释
#   + 用16进制表示结果。

# %% [markdown]
# # 0x02
# + 谜面
#   + 解说：这个谜题让我们从二零二三开始。
#   + 文字：二零二三
# + 解释
#   + 初始输入。

# %%
init = '二零二三'
# 每个月份对应一个谜面和谜底
ans = {}

# %% [markdown]
# # 0x03
# + 谜面
#   + 解说：我们使用着不同的文字，指望在寻找一个统一的答案。
#   + 画面：独角兽；VSCode编辑区。
#   + 文字：Jan.16
# + 解释
#   + 对图片有不同的解读方法，但答案最终都指向Unicode：独角兽Unicorn与Unicode读音近似；编辑器下方所用编码为UTF-8；uni-前缀和code组合起来也是Unicode。
#   + 不同文字、统一答案也指一致的编码方式Unicode。
#   + 谜底即为上文汉字的Unicode 16进制编码连接。
#   + 右上角文字的含义暂时未知，见下文。

# %%
ans['Jan'] = ''.join(hex(ord(ch))[2:] for ch in init)

# %% [markdown]
# # 0x04
# + 谜面
#   + 解说：当我们不想透露答案，又想确认答案是否一致，就要想点办法。
#   + 画面：作者的项目Viztracer的Readme；医生；索尼迷你光盘；门捷列夫肖像；摩尔多瓦国旗。
#   + 文字：Feb.32
# + 解释
#   + Readme使用markdown，缩写为md；医学博士Doctor of Medicine缩写为MD；迷你光盘Mini Disc缩写为MD；门捷列夫Dmitri Mendeleev缩写为M.D.；摩尔多瓦Moldavia缩写为MD（[参考](<https://www.abbreviationfinder.org/moldova-abbreviations/>)）。一共出现了5组MD，意指MD5。
#   + MD5算法被用于确保信息传输完整一致。
#   + MD5默认加密位数为32位，可以推测，画面右上角文字中的数字表示这一谜题的答案有多少位（16进制下）。

# %%
from hashlib import md5
ans['Feb'] = md5(ans['Jan'].encode()).hexdigest()

# %% [markdown]
# # 0x05
# + 谜面
#   + 解说：有时候事情没有头绪，不妨把它们排个序，或许就能看到解决的路径。
#   + 画面：顺序指引的1\~5。
#   + 文字：Mar.32
# + 解释
#   + 顺序排序即可。

# %%
ans['Mar'] = ''.join(sorted(ans['Feb']))

# %% [markdown]
# # 0x06
# + 谜面
#   + 解说：二月，抑或三月，或许就是四月的答案。
#   + 画面：异或门。
#   + 文字：Apr.32
# + 解释
#   + “抑或”与“异或”谐音，指对二月和三月的答案作异或。注意是对16进制数作异或而非字符串。

# %%
ans['Apr'] = hex(int(ans['Feb'], 16) ^ int(ans['Mar'], 16))[2:]

# %% [markdown]
# # 0x07
# + 谜面
#   + 解说：若是还没看到结果，可以努力多一点。
#   + 画面：凯撒雕像；凯撒沙拉。
#   + 文字：
#     + May 32
#     + F -> 0
# + 解释
#   + 指凯撒密码。“多一点”指偏移量为1位，使F与0对齐。
#   + 五月可以直接用“May”表示而非“May.”，因此五月的谜面比其他月份的“少一点”，不知道这算不算一个小彩蛋（笑）。

# %%
ans['May'] = ans['Apr'].translate(str.maketrans('0123456789abcdef', '123456789abcdef0'))

# %% [markdown]
# # 0x08
# + 谜面
#   + 解说：当然，也可能换个角度看人生，一切就不同了。
#   + 画面：由螺旋箭头串联起来的8\*4网格。
#   + 文字：Jun.32
# + 解释
#   + 按箭头顺序重新排列字符串即可。

# %%
ans['Jun'] = ans['May'][::4] + ans['May'][29:31] + ans['May'][31::-4] + ans['May'][2] + ans['May'][1:29:4] + ans['May'][26:2:-4]

# %% [markdown]
# # 0x09
# + 谜面
#   + 解说：时间过去了一半，不妨将问题也拆掉一半。烦恼的乘法不是每个人都要做。
#   + 文字：
#     + Jul.16
#     + □/
# + 解释
#   + 这一关的谜底存疑最大。
#   + 去掉一半、由32位变为16位，最朴素的想法是只保留前16位或后16位，然而结果均不对。
#   + 考虑到要做与乘法相对应的运算，再加上九月的答案提到了快速平方根算法（见下文），因此尝试对上一关答案开平方取整。

# %%
ans['Jul'] = hex(int(int(ans['Jun'], 16) ** 0.5))[2:]

# %% [markdown]
# # 0x0a
# + 谜面
#   + 音乐：（高音Do和低音Do按某种顺序进行，见下文）
#   + 文字：
#     + Aug.6
#     + 人生难免有起落，记得留下高光，忘掉低潮
# + 解释
#   + 共16个音，与上一关谜底长度相同。
#   + 根据高低音序列，保留高音索引对应位置的数字。高音共6个，与本关答案长度相同。

# %%
tones = [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1]
ans['Aug'] = ''.join(ans['Jul'][i] for i in range(16) if tones[i])

# %% [markdown]
# # 0x0b
# + 谜面
#   + 解说：你可能觉得答案就在眼前，但也可能正是它们遮住了双眼。
#   + 画面：（这里仅以与之近似的颜色代替）<br>
#       <font color=#669933>B</font> <font color=#6600cc>k</font> <font color=#ff0000>V</font> <font color=#669933>1</font> <font color=#ff0000>R</font><br>
#       <font color=#6600cc>6</font> <font color=#ff0000>P</font> <font color=#6600cc>m</font> <font color=#ff0000>4</font> <font color=#669933>y</font><br>
#       <font color=#ff0000>1</font> <font color=#6600cc>C</font> <font color=#669933>B</font> <font color=#6600cc>n</font> <font color=#6600cc>9</font><br>
#       <font color=#ff0000>7</font> <font color=#6600cc>L</font> <font color=#ff0000>3</font> <font color=#6600cc>X</font> <font color=#669933>g</font><br>
#   + 文字：Sept.8
# + 解释
#   + 上一关答案长度为6，这一关画面出现了多种颜色，意指上一关答案是表示RGB的16进制数。
#   + 由于视频存在压缩，所以屏幕取色得到的RGB可能不代表真实值，只能粗略认为上一关答案指紫色。
#   + 结合解说，可能需要去掉紫色文字，保留其他文字，即为BV1RP4y1B73g。尚不清楚紫色文字有无其他含义。
#   + 这一BV号对应了UP的上一期视频[【没那么神秘的快速平方根倒数，给你解释一下这个数是怎么来的】](https://www.bilibili.com/video/BV1RP4y1B73g)，介绍了雷神之锤3中的快速平方根倒数代码与其中的魔数0x5f3759df。
#   + Python并无C中保持地址不变、将浮点数强行转换为整数的操作。而答案又是一个8位16进制整数，可以推测，答案就是存在于视频中的某个整数，亦即0x5f3759df。

# %%
ans['Sept'] = '5f3759df'

# %% [markdown]
# # 0x0c
# + 谜面
#   + 解说：对于复杂的问题，我们总可以把它们拆成小的单位，然后优先解决最大的那个。
#   + 文字：
#     + Oct.5
#     + PRIME
# + 解释
#   + prime既指首要的，又指素数。结合解说，即为分解质因数，并取最大的质因子。
#   + [这里](https://zh.numberempire.com/numberfactorizer.php)可以直接计算质因数分解结果。计算结果与答案长度为5一致。

# %%
from typing import List, Tuple
def prime_factorization(num: int) -> List[Tuple[int, int]]:
    res = []
    primes = [2]
    cnt = 0
    while num % 2 == 0:
        num //= 2
        cnt += 1
    if cnt:
        res.append((2, cnt))

    for x in range(3, num + 1, 2):
        # 判断质数
        flag = True
        for p in primes:
            if p ** 2 > x:
                break
            if x % p == 0:
                flag = False
                break
        if flag:
            primes.append(x)
            # 检查是否是num的质因子
            cnt = 0
            while num % x == 0:
                num //= x
                cnt += 1
            if cnt:
                res.append((x, cnt))
            if num == 1:
                break

    return res

ans['Oct'] = hex(prime_factorization(int(ans['Sept'], 16))[-1][0])[2:]

# %% [markdown]
# # 0x0d
# + 谜面
#   + 解说：只有看清了每一条路的荆棘，才可能寻找到人生的捷径。
#   + 画面：标有数字的8\*9网格（见下文），左上角有箭头指入，右下角有箭头指出。
#   + 文字：Nov.16
# + 解释
#   + 意在寻找从左上角到右下角的路径，使路径上所有数字之和最小。
#   + [x]表示上一关答案的第x位。
#   + 注意到网格尺寸为8\*9、答案长度为16，因此每一步的前进方向必须为向右或向下，最终路径上的数字相连即为答案。

# %%
digits = [
    '0068bc763',
    '46a{3}afc{4}e',
    '7{0}959e7dc',
    '8d89{1}e{2}{1}1',
    'eac9ecd84',
    '2d{4}6f919a',
    'c{0}75d7{2}1{3}',
    '43eba4f61'
    ]
for i in range(len(digits)):
    digits[i] = digits[i].format(*ans['Oct'])
grid = [[int(d, 16) for d in row] for row in digits]

def minCostRoute(grid: List[int]) -> List[Tuple[int, int]]:
    # 动态规划
    rows = len(grid)
    cols = len(grid[0])
    step = [[(0, 0)] * cols for _ in range(rows)] # 到达当前格子代价最小的上一步走法
    # 到达当前格子的最小代价，直接原地操作
    for i in range(1, rows):
        grid[i][0] += grid[i-1][0]
        step[i][0] = (i-1, 0)
    for j in range(1, cols):
        grid[0][j] += grid[0][j-1]
        step[0][j] = (0, j-1)
    for i in range(1, rows):
        for j in range(1, cols):
            if grid[i-1][j] < grid[i][j-1]:
                grid[i][j] += grid[i-1][j]
                step[i][j] = (i-1, j)
            else:
                grid[i][j] += grid[i][j-1]
                step[i][j] = (i, j-1)

    route = [(rows-1, cols-1)]
    while True:
        i, j = route[-1]
        if i == j == 0:
            break
        route.append(step[i][j])

    return route[::-1]

ans['Nov'] = ''.join(digits[i][j] for i, j in minCostRoute(grid))

# %% [markdown]
# # 0x0e
# + 谜面
#   + 解说：换个形式填充问题，就可以直接看到答案。
#   + 画面：8\*8的国际象棋棋盘。
#   + 文字：Dec.2
# + 解释
#   + 将16位16位数转换为64位2进制数，即可填充到8\*8的棋盘上。
#   + 观察填充结果即可得到答案。

# %%
board = '\n'.join(''.join(str((int(ans['Nov'], 16) >> 63 - 8*i - j) & 1) for j in range(8)) for i in range(8))
# print(board)

# 或
# board = [[(int(ans['Nov'], 16) >> 63 - 8*i - j) & 1 for j in range(8)] for i in range(8)]
# import matplotlib.pyplot as plt
# plt.imshow(board, cmap='gray')
# plt.axis('scaled')

ans['Dec'] = '84'

# %% [markdown]
# # 0x0f
# + 谜题
#   + 解说：是不是到现在依然一头雾水？其实很多谜题就是这样，直到终点前一步还迷雾重重，而揭示谜底的那一刻，一切便豁然开朗了。
#   + 画面：2023年的年历，某些日期依次闪烁的动画（顺序见下文），每个月份都会有两个日期闪烁。
# + 解释
#   + 注意到每个月份闪烁日期的数字都不大于该月答案的长度，可以推测是对该月答案按日期进行索引（下标从1开始）。
#   + 每个月份的两个16进制数字为一组，转换为对应ASCII码的字符即可得答案。

# %%
sequence = [
    ('Dec', 2, 1),
    ('Jun', 11, 24),
    ('Feb', 7, 21),
    ('Mar', 16, 2),
    ('Sept', 4, 6),
    ('Jan', 13, 2),
    ('Nov', 15, 6),
    ('Oct', 4, 4),
    ('Apr', 5, 21),
    ('May', 5, 23),
    ('Aug', 1, 3),
    ('Jul', 11, 2)
    ]
blessing = ''.join(chr(int(ans[month][idx1-1] + ans[month][idx2-1], 16)) for month, idx1, idx2 in sequence)
# print(blessing)

# %% [markdown]
# # `HappyNewYear`


