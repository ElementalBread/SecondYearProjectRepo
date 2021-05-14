def translateTextToBraille(textToTranslate):
    dictionary = {65: '⠠⠁',  # A
                  66: '⠠⠃',  # B
                  67: '⠠⠉',  # C
                  266: '⠠⠉',  # Ċ
                  68: '⠠⠙',  # D
                  69: '⠠⠑',  # E
                  70: '⠠⠋',  # F
                  288: '⠠⠾',  # Ġ
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
                  82: '⠠⠗',  # R
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
                  100: '⠙',  # d
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
                  8216: '⠄⠴',  # ' (close)
                  8217: '⠄⠦',  # ' (open)
                  39: '⠄',  # ' (general)
                  34: '⠄⠶',  # " (general)
                  40: '⠐⠣',  # (
                  41: '⠐⠜',  # )
                  47: '⠸⠌',  # /
                  92: '⠸⠡',  # \
                  }

    translatedText = ""
    numberCache = ""
    i = 0
    for letter in textToTranslate:
        if letter.isnumeric():
            numberCache = numberCache + letter
        elif letter == 'g':
            if (textToTranslate[i + 1] == 'ħ'):
                translatedText = translatedText + '⠣'
            else:
                translatedText = translatedText + letter.translate(dictionary)
        elif letter == 'G':
            if (textToTranslate[i + 1] == 'ħ'):
                translatedText = translatedText + '⠠⠣'
            else:
                translatedText = translatedText + letter.translate(dictionary)
        elif letter == 'ħ':
            if ((textToTranslate[i - 1] != 'g') & (textToTranslate[i - 1] != 'G')):
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


def translateBrailleToText(textToTranslate):
    dictionary = {10241: 97,  # ⠁ a
                  10243: 98,  # ⠃b
                  10249: 267,  # ⠉ ċ
                  10265: 100,  # ⠙ d
                  10257: 101,  # ⠑ e
                  10251: 102,  # ⠋ f
                  10302: 289,  # ⠾ ġ
                  10267: 103,  # ⠛ g
                  10259: 104,  # ⠓ h
                  10286: 295,  # ⠮ ħ
                  10250: 105,  # ⠊ i
                  10266: 106,  # ⠚ j
                  10245: 107,  # ⠅ k
                  10247: 108,  # ⠇ l
                  10253: 109,  # ⠍ m
                  10269: 110,  # ⠝ n
                  10261: 111,  # ⠕ o
                  10255: 112,  # ⠏ p
                  10271: 113,  # ⠟ q
                  10263: 114,  # ⠗ r
                  10254: 115,  # ⠎ s
                  10270: 116,  # ⠞ t
                  10277: 117,  # ⠥ u
                  10279: 118,  # ⠧ v
                  10298: 119,  # ⠺ w
                  10285: 120,  # ⠭ x
                  10301: 380,  # ⠽ ż
                  10293: 122,  # ⠵ z
                  10292: 48,  # ⠴ 0
                  10242: 49,  # ⠂ 1
                  10246: 50,  # ⠆ 2
                  10258: 51,  # ⠒ 3
                  10290: 52,  # ⠲ 4
                  10274: 53,  # ⠢ 5
                  10262: 54,  # ⠖ 6
                  10294: 55,  # ⠶ 7
                  10278: 56,  # ⠦ 8
                  10260: 57,  # ⠔ 9
                  10258: 58,  # ⠒ :
                  10246: 59,  # ⠆ ;
                  10242: 44,  # ⠂ ,
                  10276: 45,  # ⠤ -
                  10290: 46,  # ⠲ .
                  10262: 33,  # ⠖ !
                  10278: 63,  # ⠦ ?
                  10244: 39,  # ⠄ ' (general)
                  }

    translatedText = ""
    numberCache = ""
    letterCapital = False
    characterNotHandled = True
    i = 0
    for letter in textToTranslate:
        if characterNotHandled:
            characterNotHandled = True
            if letter == '⠸':
                if textToTranslate[i+1] == '⠡':
                    translatedText = translatedText + '\\'
                    characterNotHandled = False
                elif textToTranslate[i+1] == '⠌':
                    translatedText = translatedText + '/'
                    characterNotHandled = False

            if letter == '⠄':
                if len(textToTranslate) > 1:
                    if textToTranslate[i + 1] == '⠶':
                        translatedText = translatedText + '"'
                        characterNotHandled = False
                    elif textToTranslate[i+1] == '⠦':
                        translatedText = translatedText + "'"
                        characterNotHandled = False
                    elif textToTranslate[i+1] == '⠴':
                        translatedText = translatedText + "'"
                        characterNotHandled = False
                    else:
                        translatedText = translatedText + letter.translate(dictionary)
                else:
                    translatedText = translatedText + letter.translate(dictionary)

            elif letter == '⠐':
                if textToTranslate[i+1] == '⠣':
                    translatedText = translatedText + '('
                    characterNotHandled = False
                elif letter(i+1) == '⠜':
                    translatedText = translatedText + ')'
                    characterNotHandled = False

            elif letter == '⠘':
                if textToTranslate[i+1] == '⠴':
                    translatedText = translatedText + '"'
                    characterNotHandled = False
                elif textToTranslate[i+1] == '⠦':
                    translatedText = translatedText + '"'
                    characterNotHandled = False

            elif letter == '⠠':
                letterCapital = True

            else:
                if numberCache != '':
                    print("Number cache full")
                else:
                    if letter == ' ':
                        translatedText = translatedText + ' '
                    else:
                        letter = letter.translate(dictionary)
                        if letterCapital == True:
                            letter = letter.upper()
                            letterCapital = False
                        translatedText = translatedText + letter
        else:
            characterNotHandled = True
        i = i + 1

    if numberCache != '':
        numberCache = '⠼' + numberCache.translate(dictionary)
        translatedText = translatedText + numberCache

    return translatedText


continueRunning = True
while continueRunning:
    userChoice = input(
        'Daħħal 1 sabiex tittraduċi mill-Malti għall-Braille, Daħħal 2 sabiex tittraduċi mill-Braille għall-Malti: ')
    if userChoice == '1':
        textToTranslate = input('Enter:')
        if textToTranslate == 'EXITPROJECT':
            userChoice = 3
        else:
            translatedText = translateTextToBraille(textToTranslate)
            print(translatedText)
    elif userChoice == '2':
        textToTranslate = input('Enter:')
        if textToTranslate == "EXITPROJECT":
            userChoice = 3
        else:
            translatedText = translateBrailleToText(textToTranslate)
            print(translatedText)
    else:
        print("Exit")
        continueRunning = False
