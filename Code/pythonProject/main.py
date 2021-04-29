def translateText(textToTranslate):

    dictionary = {65: '⠠⠁',  # A
                  66: '⠠⠃',  # B
                  67: '⠠⠉',  # C
                  266: '⠠⠉',  # Ċ
                  68: '⠠⠙',  # D
                  69: '⠠⠑',  # E
                  70: '⠠⠋',  # F
                  288: '⠠⠾',   # Ġ
                  71: '⠠⠛',  # G
                  72: '⠠⠓',  # H
                  294: '⠠⠮',  # Ħ
                  73: '⠠⠊',  # I
                  74: '⠠⠚',  # J
                  75: '⠠⠅',  # K
                  76: '⠠⠇',  # L
                  77: '⠠⠍',  # M
                  78: '⠠⠝',  # N
                  79: '⠠⠕',  # O
                  80: '⠠⠏',  # P
                  81: '⠠⠟',  # Q
                  82: '⠠⠗',   # R
                  83: '⠠⠎',  # S
                  84: '⠠⠞',  # T
                  85: '⠠⠥',  # U
                  86: '⠠⠧',  # V
                  87: '⠠⠺',  # W
                  88: '⠠⠭',  # X
                  379: '⠠⠽',  # Ż
                  90: '⠠⠵',  # Z
                  97: '⠁',  # a
                  98: '⠃',  # b
                  99: '⠉',  # c
                  267: '⠉',  # ċ
                  100: '⠙ ',  # d
                  101: '⠑',  # e
                  102: '⠋',  # f
                  289: '⠾',  # ġ
                  103: '⠛',  # g
                  104: '⠓',  # h
                  295: '⠮',  # ħ
                  105: '⠊',  # i
                  106: '⠚',  # j
                  107: '⠅',  # k
                  108: '⠇',  # l
                  109: '⠍',  # m
                  110: '⠝',  # n
                  111: '⠕',  # o
                  112: '⠏',  # p
                  113: '⠟',  # q
                  114: '⠗',  # r
                  115: '⠎',  # s
                  116: '⠞',  # t
                  117: '⠥',  # u
                  118: '⠧',  # v
                  119: '⠺',  # w
                  120: '⠭',  # x
                  380: '⠽',  # ż
                  122: '⠵',  # z
                  48: '⠴',  # 0
                  49: '⠂',  # 1
                  50: '⠆',  # 2
                  51: '⠒',  # 3
                  52: '⠲',  # 4
                  53: '⠢',  # 5
                  54: '⠖',  # 6
                  55: '⠶',  # 7
                  56: '⠦',  # 8
                  57: '⠔',  # 9
                  58: '⠒',  # :
                  59: '⠆',  # ;
                  44: '⠂',  # ,
                  45: '⠤',  # -
                  46: '⠲',  # .
                  33: '⠖',  # !
                  63: '⠦',  # ?
                  8220: '⠘⠴',  # “ (close)
                  8221: '⠘⠦',  # ” (open)
                  8216: '⠄⠴', # ' (close)
                  8217: '⠄⠦', # ' (open)
                  40: '⠐⠣', # (
                  41: '⠐⠜', # )
                  47: '⠸⠌', # /
                  92: '⠸⠡', # \
                  }

    translatedText = ""
    numberCache = ""
    i = 0
    for letter in textToTranslate:
        if letter.isnumeric():
            numberCache = numberCache + letter
        elif letter == 'g':
            if (textToTranslate[i+1] == 'ħ'):
                translatedText = translatedText + '⠣'
        elif letter == 'G':
            if (textToTranslate[i+1] == 'ħ'):
                translatedText = translatedText + '⠣'
        elif letter == 'ħ':
            if ((textToTranslate[i-1] != 'g') & (textToTranslate[i-1] != 'G')):
                letter = letter.translate(dictionary)
                translatedText = translatedText + letter
        else:
            if numberCache != '':
                numberCache = '⠼' + numberCache.translate(dictionary)
                translatedText = translatedText + numberCache + letter.translate(dictionary)
                numberCache = ''
            else:
                if letter == ' ':
                    translatedText = translatedText + ' '
                else:
                    letter = letter.translate(dictionary)
                    translatedText = translatedText + letter

        i = i + 1

    if numberCache != '':
        numberCache = '⠼' + numberCache.translate(dictionary)
        translatedText = translatedText + numberCache

    return translatedText


while 1:
    textToTranslate = input('Enter:')
    translatedText = translateText(textToTranslate)
    print(translatedText)
