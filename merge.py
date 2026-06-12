import json

def main():
    print("Đang tải dữ liệu...")
    
    # 1. Đọc từ điển tiếng Anh hiện tại của bạn
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

    # 3. Tạo một bộ từ điển map nhanh: Ký tự -> [Âm Hán] Nghĩa
    tc_map = {}
    data_list = thieu_chuu.get('data', [])
    
    for item in data_list:
        if len(item) >= 10:
            ky_tu = str(item[9]).strip()
            am_han = str(item[4]).strip().capitalize()
            nghia_goc = str(item[6]).strip().replace('\n', ' ').replace('\r', '')
            
            # Lấy câu nghĩa ngắn gọn (tới dấu chấm đầu tiên) để in vở không bị tràn dòng
            nghia_ngan = nghia_goc.split('.')[0] if '.' in nghia_goc else nghia_goc
            
            tc_map[ky_tu] = f"[{am_han}] {nghia_ngan}"

    print("Bắt đầu đối chiếu và dịch nghĩa...")

    # 4. Gộp nghĩa tiếng Việt vào từ điển của bạn
    count = 0
    for word in my_dict.keys():
        # Nếu là chữ đơn (1 ký tự)
        if len(word) == 1 and word in tc_map:
            my_dict[word]['meaning'] = tc_map[word]
            count += 1
            
        # Nếu là từ ghép (ví dụ: 電路)
        elif len(word) > 1:
            combined_meaning = []
            for char in word:
                if char in tc_map:
                    combined_meaning.append(tc_map[char])
            
            # Nối nghĩa các chữ đơn lại với nhau
            if combined_meaning:
                my_dict[word]['meaning'] = " | ".join(combined_meaning)
                count += 1

    # 5. Lưu thành file JSON mới
    output_file = 'dictionary_vi.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(my_dict, f, ensure_ascii=False, indent=4)

    print(f"Xong! Đã cập nhật thành công {count} từ vựng sang tiếng Việt.")
    print(f"File mới đã được lưu thành '{output_file}'.")

if __name__ == "__main__":
    main()