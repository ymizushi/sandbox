#!/usr/bin/env python
# -*- coding: utf-8 -*-

TENJI_MAP = {
    u'あ':u'⠁',
    u'い':u'⠃',
    u'う':u'⠉',
    u'え':u'⠋',
    u'お':u'⠊',
    u'か':u'⠡',
    u'き':u'⠣',
    u'く':u'⠩',
    u'け':u'⠫',
    u'こ':u'⠪',
    u'さ':u'⠱',
    u'し':u'⠳',
    u'す':u'⠹',
    u'せ':u'⠻',
    u'そ':u'⠺',
    u'た':u'⠕',
    u'ち':u'⠗',
    u'つ':u'⠝',
    u'て':u'⠟',
    u'と':u'⠞',
    u'な':u'⠅',
    u'に':u'⠇',
    u'ぬ':u'⠍',
    u'ね':u'⠏',
    u'の':u'⠎',
    u'は':u'⠥',
    u'ひ':u'⠧',
    u'ふ':u'⠭',
    u'へ':u'⠯',
    u'ほ':u'⠮',
    u'ま':u'⠵',
    u'み':u'⠷',
    u'む':u'⠽',
    u'め':u'⠿',
    u'も':u'⠾',
    u'や':u'⠌',
    u'ゆ':u'⠬',
    u'よ':u'⠜',
    u'ら':u'⠑',
    u'り':u'⠓',
    u'る':u'⠙',
    u'れ':u'⠛',
    u'ろ':u'⠚',
    u'わ':u'⠄',
    u'お':u'⠔',
    u'ん':u'⠴',
    u'っ':u'⠂',
    u'ー':u'⠒',

    u'”':u'⠐',
    u'＠':u'⠠',
    u'＃' :u'⠈', # 拗音
    u'！' :u'⠘', # 拗濁音 ⠘ 
    u'＄' :u'⠨', # 拗半濁音 ⠨ 
}

while True:
    raw_input_str = raw_input(u'日本語かなを入力してください> '.encode('utf-8'))
    if raw_input_str == 'q':
        break
    input_str = raw_input_str.decode('utf-8')
    output_str = ''
    for i in input_str:
        output_str += TENJI_MAP[i]
    output_str += '\n'
    print output_str
