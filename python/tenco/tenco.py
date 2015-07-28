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
    u'を':u'⠔',
    u'ん':u'⠴',
    u'っ':u'⠂',
    u'ー':u'⠒',

    u'が':u'⠐⠡',
    u'ぎ':u'⠐⠣',
    u'ぐ':u'⠐⠩',
    u'げ':u'⠐⠫',
    u'ご':u'⠐⠪',

    u'ざ':u'⠐⠱',
    u'じ':u'⠐⠳',
    u'ず':u'⠐⠹',
    u'ぜ':u'⠐⠻',
    u'ぞ':u'⠐⠺',

    u'だ':u'⠐⠕',
    u'ぢ':u'⠐⠗',
    u'づ':u'⠐⠝',
    u'で':u'⠐⠟',
    u'ど':u'⠐⠞',

    u'ば':u'⠐⠥',
    u'び':u'⠐⠧',
    u'ぶ':u'⠐⠭',
    u'べ':u'⠐⠯',
    u'ぼ':u'⠐⠮',

    u'ば':u'⠐⠥',
    u'び':u'⠐⠧',
    u'ぶ':u'⠐⠭',
    u'べ':u'⠐⠯',
    u'ぼ':u'⠐⠮',

    u'ぱ':u'⠠⠥',
    u'ぴ':u'⠠⠧',
    u'ぷ':u'⠠⠭',
    u'ぺ':u'⠠⠯',
    u'ぽ':u'⠠⠮',

    u'きゃ':u'⠈⠡',
    u'きゅ':u'⠈⠩',
    u'きょ':u'⠈⠪',

    u'しゃ':u'⠈⠱',
    u'しゅ':u'⠈⠹',
    u'しょ':u'⠈⠺',

    u'ちゃ':u'⠈⠕',
    u'ちゅ':u'⠈⠝',
    u'ちょ':u'⠈⠞',

    u'にゃ':u'⠈⠅',
    u'にゅ':u'⠈⠍',
    u'にょ':u'⠈⠎',

    u'ひゃ':u'⠈⠥',
    u'ひゅ':u'⠈⠭',
    u'ひょ':u'⠈⠮',

    u'みゃ':u'⠈⠵',
    u'みゅ':u'⠈⠽',
    u'みょ':u'⠈⠾',

    u'りゃ':u'⠈⠑',
    u'りゅ':u'⠈⠙',
    u'りょ':u'⠈⠚',

    u'ぎゃ':u'⠘⠡',
    u'ぎゅ':u'⠘⠩',
    u'ぎょ':u'⠘⠪',

    u'じゃ':u'⠘⠱',
    u'じゅ':u'⠘⠹',
    u'じょ':u'⠘⠺',

    u'ぢゃ':u'⠘⠕',
    u'ぢゅ':u'⠘⠝',
    u'ぢょ':u'⠘⠞',

    u'びゃ':u'⠘⠥',
    u'びゅ':u'⠘⠭',
    u'びょ':u'⠘⠮',

    u'ぴゃ':u'⠨⠥',
    u'ぴゅ':u'⠨⠭',
    u'ぴょ':u'⠨⠮',

    u'いぇ':u'⠈⠋',
    u'きぇ':u'⠈⠫',
    u'しぇ':u'⠢⠻',
    u'ちぇ':u'⠢⠟',

    u'にぇ':u'⠈⠏',
    u'ひぇ':u'⠈⠯',
    u'みぇ':u'⠈⠿',
    u'りぇ':u'⠈⠛',

    u'ぎぇ':u'⠘⠫',
    u'じぇ':u'⠘⠻',
    u'びぇ':u'⠘⠯',
    u'ぢぇ':u'⠘⠟',

    u'ぴぇ':u'⠨⠯',

    u'うぃ':u'⠢⠃',
    u'うぇ':u'⠢⠋',
    u'うぉ':u'⠢⠊',

    u'すぃ':u'⠈⠳',
    u'ずぃ':u'⠘⠳',

    u'てぃ':u'⠢⠗',
    u'でぃ':u'⠘⠗',

    u'くぁ':u'⠢⠡',
    u'くぃ':u'⠢⠣',
    u'くぇ':u'⠢⠫',
    u'くぉ':u'⠢⠪',

    u'ぐぁ':u'⠲⠡',
    u'ぐぃ':u'⠲⠣',
    u'ぐぇ':u'⠲⠫',
    u'ぐぉ':u'⠲⠪',

    u'とぅ':u'⠢⠝',
    u'どぅ':u'⠘⠝',

    u'つぁ':u'⠢⠕',
    u'つぃ':u'⠢⠗',
    u'つぇ':u'⠢⠟',
    u'つぉ':u'⠢⠞',


    u'ふぁ':u'⠥',
    u'ふぃ':u'⠧',
    u'ふぇ':u'⠯',
    u'ふぉ':u'⠮',

    u'てゅ':u'⠨⠝',
    u'ふゅ':u'⠨⠬',
    u'ふょ':u'⠨⠜',

    u'でゅ':u'⠸⠝',
    u'ゔゅ':u'⠸⠬',
    u'ゔょ':u'⠸⠜',

    u'ゔぁ':u'⠲⠥',
    u'ゔぃ':u'⠲⠧',
    u'ゔぇ':u'⠲⠯',
    u'ゔぉ':u'⠲⠮',

    u'ゔ':u'⠐⠉',

    u'”':u'⠐', # 濁音
    u'＠':u'⠠', # 半濁音
    u'＃' :u'⠈', # 拗音
    u'！' :u'⠘', # 拗濁音 ⠘ 
    u'＄' :u'⠨', # 拗半濁音 ⠨ 

    u'、' :u'⠰ ', # 読点
    u'。' :u'⠲  ', # 読点
    u'？' :u'⠢', # 疑問符
    u'！' :u'⠲', # 感嘆符
    u'・' :u'⠐', # 中点

    u'　' :u' ', # 半角空白
    u' ' :u' ', # 全角空白
}

while True:
    raw_input_str = raw_input(u'日本語かなを入力してください> '.encode('utf-8'))
    if raw_input_str == 'q':
        break
    input_str = raw_input_str.decode('utf-8')
    output_str = ''
    i = 0
    while i < len(input_str):
        if TENJI_MAP.get(input_str[i:i+2]):
            output_str += TENJI_MAP.get(input_str[i:i+2])
            i += 1
        else:
            output_str += TENJI_MAP[input_str[i]]
        i += 1
    output_str += '\n'
    print output_str
