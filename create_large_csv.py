import csv
import os

def create_large_csv(file_path, size_gb):
    row = ['Example'] * 100  # 100カラムのサンプルデータ
    file_size = 0
    size_limit = size_gb * (1024 ** 3)  # サイズ制限をバイト単位に変換

    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Column'] * 100)  # ヘッダー行を書き込む

        while file_size < size_limit:
            writer.writerow(row)
            f.flush()
            file_size = os.path.getsize(file_path)

if __name__ == '__main__':
    create_large_csv('large_file.csv', 1)  # 6GBのCSVファイルを作成
