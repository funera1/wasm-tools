#!/usr/bin/python3
import sys
from collections import defaultdict

"""
(cur_fidx, ir_pos): (8, 0)
(cur_fidx, ir_pos): (8, 16)
(cur_fidx, ir_pos): (8, 38)
...
の形式のテキストに対して

cur_func_idx: 0
(opcode, wasm_pos, ir_pos): (0xb, 1, 0)
cur_func_idx: 1
(opcode, wasm_pos, ir_pos): (0x28, 7, 0)
(opcode, wasm_pos, ir_pos): (0xd, 14, 16)
(opcode, wasm_pos, ir_pos): (0x36, 20, 38)


に変換する
"""
import re

def parse_input(text):
    # 行ごとに分割
    lines = text.strip().split('\n')
    
    # 現在の関数インデックスを保持する変数
    data = defaultdict(list)
    cur_fidx = None

    for line in lines:
        # 正規表現で値を抽出
        match = re.match(r'\(cur_fidx, ir_pos\): \((\d+), (\d+)\)', line)
        if match:
            fidx, ir_pos = map(int, match.groups())
            data[fidx].append(ir_pos)
            # result.append(f'ir_pos: {ir_pos}')

    # ソートした結果を構築
    result = []
    for fidx in sorted(data.keys()):
        result.append(f'cur_func_idx: {fidx}')
        not_duplicate_data = list(set(data[fidx]))
        for ir_pos in sorted(not_duplicate_data):
            result.append(f'ir_pos: {ir_pos}')
    
    
    return '\n'.join(result)

# テスト用の入力
input_text = """
(cur_fidx, ir_pos): (8, 0)
(cur_fidx, ir_pos): (8, 16)
(cur_fidx, ir_pos): (8, 38)
(cur_fidx, ir_pos): (9, 0)
(cur_fidx, ir_pos): (9, 22)
"""

# output_text = parse_input(input_text)
# print(output_text)


args = sys.argv
if len(args) != 2:
    print("ファイル名を入力してください")

input_file_path = args[1]

with open(input_file_path, 'r', encoding='utf-8') as file:
    data = file.read()
    # print(data)


    output_text = parse_input(data)
    print(output_text)
