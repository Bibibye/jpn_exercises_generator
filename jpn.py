#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import random as rand
import math

DEBUG = True

def debug(str):
    if debug:
        print(str)

hiragana_table = [
    ('#',"あいうえお"),
    ('k',"かきくけこ"),
    ('s',"さしすせそ"),
    ('t',"たちつてと"),
    ('n',"なにぬねの"),
    ('h',"はひふへほ"),
    ('m',"まみむめも"),
    ('y',"やーゆーよ"),
    ('r',"らりるれろ"),
    ('w',"わーーーを"),
    ("n", "んーーーー"),
    ('g',"がぎぐげご"),
    ('z',"ざじずぜぞ"),
    ('d',"だぢづでど"),
    ('b',"ばびぶべぼ"),
    ('p', "ぱぴぷぺぽ"),
    ('ky',["きゃ", "", "きゅ", "", "きょ"]),
    ('gy',["ぎゃ", "", "ぎゅ", "", "ぎょ"]),
    ('sh',["しゃ", "", "しゅ", "", "しょ"]),
    ('j', ["じゃ", "", "じゅ", "", "じょ"]),
    ('ch',["ちゃ", "", "ちゅ", "", "ちょ"]),
    ('ny',["にゃ", "", "にゅ", "", "にょ"]),
    ('hy',["ひゃ", "", "ひゅ", "", "ひょ"]),
    ('by',["びゃ", "", "びゅ", "", "びょ"]),
    ('py',["ぴゃ", "", "ぴゅ", "", "ぴょ"]),
    ('my',["みゃ", "", "みゅ", "", "みょ"]),
    ('ry',["りゃ", "", "りゅ", "", "りょ"])
]

katakana_table = [
    ('#',"アイウエオ"),
    ('k',"カキクケコ"),
    ('s',"サシスセソ"),
    ('t',"タチツテト"),
    ('n',"ナニヌネノ"),
    ('h',"ハヒフヘホ"),
    ('m',"マミムメモ"),
    ('y',"ヤーユーヨ"),
    ('r',"ラリルレロ"),
    ('w',"ワーーーヲ"),
    ('n', "ンーーーー"),
    ('g',"ガギグゲゴ"),
    ('z',"ザジズゼゾ"),
    ('d',"ダヂヅデド"),
    ('b',"バビブベボ"),
    ('p', "パピプペポ"),
    ('ky',["キャ", "", "キュ", "", "キョ"]),
    ('gy',["ギャ", "", "ギュ", "", "ギョ"]),
    ('sh',["シャ", "", "シュ", "", "ショ"]),
    ('j', ["ジャ", "", "ジュ", "", "ジョ"]),
    ('ch',["チャ", "", "チュ", "", "チョ"]),
    ('ny',["ニャ", "", "ニュ", "", "ニョ"]),
    ('hy',["ヒャ", "", "ヒュ", "", "ヒョ"]),
    ('by',["ビャ", "", "ビュ", "", "ビョ"]),
    ('py',["ピャ", "", "ピュ", "", "ピョ"]),
    ('my',["ミャ", "", "ミュ", "", "ミョ"]),
    ('ry',["リャ", "", "リュ", "", "リョ"])
]

romaji_to_int = {
    "a" : 0,
    "i" : 1,
    "u" : 2,
    "e" : 3,
    "o" : 4
}

int_to_romaji = ["a","i","u","e","o"]
    
exceptions = {
    "し" : "shi",
    "じ" : "ji",
    "ち" : "chi",
    "ぢ" : "ji",
    "つ" : "tsu",
    "づ" : "zu",
    "ふ" : "fu",
    "ん" : "n",

    "シ" : "shi",
    "ジ" : "ji",
    "チ" : "chi",
    "ヂ" : "ji",
    "ツ" : "tsu",
    "ヅ" : "zu",
    "フ" : "fu",
    "ン" : "n"
}

kana_tables = {"hiragana" : hiragana_table, 
               "katakana" : katakana_table}
    
hiragana_list = [c for l in hiragana_table for c in l[1] if c != "ー" and c != ""]
katakana_list = [c for l in katakana_table for c in l[1] if c != "ー" and c != ""]

def is_romaji(romaji, kana):
    if kana in exceptions.keys():
        return romaji == exceptions[kana]

    l = len(romaji)

    if l == 1:
        return (katakana_table[0][1][romaji_to_int[romaji]] == kana or
                hiragana_table[0][1][romaji_to_int[romaji]] == kana)
    
    elif l == 2 or l == 3:
        for table in kana_tables.values():
            for i in range(len(table)):
                if table[i][0] == romaji[:l-1]:
                    if table[i][1][romaji_to_int[romaji[l-1]]] == kana:
                        return True
    return False

def get_romaji(kana):
    if kana in exceptions.keys():
        return exceptions[kana]
    for table in kana_tables.values():
        for i in range(len(table)):
            for j in range(len(table[i][1])):
                if table[i][1][j] == kana:                    
                    return table[i][0]+int_to_romaji[j]

def print_table(table):
    size = len(table)
    offset = size % 2
    for i in range(size//2+offset):
        print(''.join(table[i][0]) + "\t" + ''.join(table[i][1]) +
              ("\t| "+ ''.join(table[i+size//2+offset][0]) + 
               "\t" + ''.join(table[i+size//2+offset][1])
               if i+size//2+offset < size  else ""))

def exercise_generator(chars):
    while True:
        yield chars[rand.randrange(len(chars))]

def reading_exercise(tables, exercise_size = 10, line_size = 10):
    exercise = exercise_generator(tables)
    for _ in range(math.ceil(exercise_size/line_size)):
        for _ in range(line_size):
            print(next(exercise), end="")
        print("")

def quizz_exercice(tables, exercise_size = 10):
    good_answers = 0
    for i in range(exercise_size):
        random = rand.randrange(len(tables))
        kana = tables[random]
        answer = input(kana+"\n? ")
        if is_romaji(answer, kana):
            good_answers += 1
            print("Right.\n")
        else:
            print("False. Answer was \""+get_romaji(kana)+"\".\n")
    print("Result : "+str(good_answers)+"/"+str(exercise_size))

def print_help():
    for i in range(len(cmd)):
        print(cmd[i][0]+" : "+cmd[i][1])

cmd = [
    ("h", "print help", print_help),
    ("ph", "print hiragana table", lambda : print_table(hiragana_table)),
    ("pk", "print katakana table", lambda : print_table(katakana_table)),
    ("re", "print random kana (reading exercise)", lambda : reading_exercise(hiragana_list+katakana_list, 100)),
    ("qe", "begin quizz (quizz exercise)", lambda : quizz_exercice(hiragana_list+katakana_list)),
    ("q", "quit", lambda : print(''))
    ]
     
if __name__ == "__main__":
    print_help()
    quit = False
    while not quit:
        try:
            user_cmd = input("> ")
            if user_cmd == "q":
                quit = True
            else:
                for i in range(len(cmd)):
                    if cmd[i][0] == user_cmd:
                        cmd[i][2]()
        except EOFError:
            quit = True
            print('')
        
