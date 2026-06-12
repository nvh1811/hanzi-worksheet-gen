import json

def main():
    print("Đang tải dữ liệu...")
    
    # 1. Đọc file dictionary.json GỐC (File này phải chứa nghĩa tiếng Việt ban đầu)
    try:
        with open('dictionary.json', 'r', encoding='utf-8') as f:
            my_dict = json.load(f)
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file 'dictionary.json'.")
        return

    # 2. Đọc file data2.json của Thiều Chửu
    try:
        with open('data2.json', 'r', encoding='utf-8') as f:
            thieu_chuu = json.load(f)
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file 'data2.json'.")
        return

    tc_map = {}
    data_list = thieu_chuu.get('data', [])
    
    for item in data_list:
        if len(item) >= 10:
            ky_tu = str(item[9]).strip()
            am_han_raw = str(item[4]).strip().lower()
            
            am_han_list = [x.strip() for x in am_han_raw.split(',')]
            am_han_chinh = am_han_list[0]
            if 'đài' in am_han_list: 
                am_han_chinh = 'đài'

            nghia_goc = str(item[6]).strip().replace('\n', ' ').replace('\r', '')
            nghia_ngan = nghia_goc.split('.')[0] if '.' in nghia_goc else nghia_goc
            
            tc_map[ky_tu] = {
                "am_han_full": am_han_raw,
                "am_han_ngan": am_han_chinh,
                "nghia": nghia_ngan
            }

    print("Bắt đầu đối chiếu và khôi phục Nghĩa Tiếng Việt...")

    count = 0
    for word, data in my_dict.items():
        
        # ĐÂY LÀ BƯỚC QUAN TRỌNG NHẤT: Cứu lại nghĩa gốc!
        # Lưu nghĩa tiếng Việt tổng thể vào thuộc tính mới tên là "word_meaning"
        nghia_goc_cua_tu = data.get('meaning', '')
        data['word_meaning'] = nghia_goc_cua_tu
        
        # Bắt đầu xử lý Chữ đơn
        if len(word) == 1 and word in tc_map:
            data['hanviet'] = tc_map[word]['am_han_ngan'].capitalize()
            data['meaning'] = f"[{tc_map[word]['am_han_full'].capitalize()}] {tc_map[word]['nghia']}"
            count += 1
            
        # Xử lý Từ ghép
        elif len(word) > 1:
            hanviet_list = []
            meaning_list = []
            
            for char in word:
                if char in tc_map:
                    hanviet_list.append(tc_map[char]['am_han_ngan'])
                    meaning_list.append(f"[{tc_map[char]['am_han_full'].capitalize()}] {tc_map[char]['nghia']}")
                else:
                    hanviet_list.append("...")
            
            data['hanviet'] = " ".join(hanviet_list).title()
            
            if meaning_list:
                data['meaning'] = " | ".join(meaning_list)
                count += 1

    # 5. Xuất ra file dictionary_vi.json
    output_file = 'dictionary_vi.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(my_dict, f, ensure_ascii=False, indent=4)

    print(f"Hoàn tất! Đã thêm thành công 'word_meaning' cho {count} từ vựng.")

if __name__ == "__main__":
    main()