# -*- coding: utf-8 -*-
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scratch.generate_goi import words_data, ILLUSTRATED_WORDS

def list_missing(limit=20):
    missing = []
    for idx, item in enumerate(words_data, 1):
        word, group, meaning, jp_def, nuance, ex_jp, ex_vi, syn, ant = item
        if word not in ILLUSTRATED_WORDS:
            missing.append((idx, word, group, meaning, nuance))
            
    print(f"TỔNG SỐ TỪ CHƯA CÓ ẢNH: {len(missing)}")
    print(f"LIÊT KÊ {min(limit, len(missing))} TỪ TIẾP THEO:")
    print("=" * 60)
    for idx, word, group, meaning, nuance in missing[:limit]:
        print(f"STT: {idx} | Từ: {word} | Nhóm: {group}")
        print(f"  Ý nghĩa: {meaning}")
        print(f"  Sắc thái: {nuance}")
        print("-" * 60)

if __name__ == "__main__":
    list_missing()
