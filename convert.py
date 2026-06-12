import json
import re

TONE_MARKS = {
    'a': ['a', 'ā', 'á', 'ǎ', 'à'],
    'e': ['e', 'ē', 'é', 'ě', 'è'],
    'i': ['i', 'ī', 'í', 'ǐ', 'ì'],
    'o': ['o', 'ō', 'ó', 'ǒ', 'ò'],
    'u': ['u', 'ū', 'ú', 'ǔ', 'ù'],
    'ü': ['ü', 'ǖ', 'ǘ', 'ǚ', 'ǜ']
}


def convert_syllable(syllable):
    """chuyển ni3 -> nǐ, hao3 -> hǎo"""
    match = re.match(r'^([a-züv:]+)([1-5])$', syllable.lower())

    if not match:
        return syllable

    base = match.group(1).replace('u:', 'ü').replace('v', 'ü')
    tone = int(match.group(2))

    if tone == 5:
        return base

    # Quy tắc đặt dấu của pinyin
    vowels = "aeiouü"

    if 'a' in base:
        target = 'a'
    elif 'e' in base:
        target = 'e'
    elif 'ou' in base:
        target = 'o'
    else:
        target = None
        for c in reversed(base):
            if c in vowels:
                target = c
                break

    if target:
        marked = TONE_MARKS[target][tone]
        base = base.replace(target, marked, 1)

    return base


def pinyin_to_tone(pinyin):
    return " ".join(convert_syllable(s) for s in pinyin.split())


def convert():
    input_file = "cedict_ts.u8"
    output_file = "dictionary.json"

    output_dict = {}
    total_lines = 0
    saved_words = 0

    print("Đang xử lý CC-CEDICT...")

    pattern = re.compile(
        r'^(\S+)\s+(\S+)\s+\[(.*?)\]\s+/(.*)/$'
    )

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                total_lines += 1

                match = pattern.match(line)

                if not match:
                    continue

                traditional = match.group(1)
                simplified = match.group(2)
                raw_pinyin = match.group(3)
                meaning = match.group(4).replace("/", "; ")

                formatted_pinyin = pinyin_to_tone(raw_pinyin)

                data = {
                    "traditional": traditional,
                    "simplified": simplified,
                    "pinyin": formatted_pinyin,
                    "meaning": meaning
                }

                # Lưu theo cả chữ phồn và chữ giản
                for key in {traditional, simplified}:
                    if key not in output_dict:
                        output_dict[key] = data
                        saved_words += 1

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(
                output_dict,
                f,
                ensure_ascii=False,
                indent=2
            )

        print(f"Tổng dòng đọc: {total_lines}")
        print(f"Số từ lưu: {saved_words}")
        print(f"Đã lưu vào: {output_file}")

    except FileNotFoundError:
        print(f"Không tìm thấy file: {input_file}")

    except Exception as e:
        print(f"Lỗi: {e}")


if __name__ == "__main__":
    convert()