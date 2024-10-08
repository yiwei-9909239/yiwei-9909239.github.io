import json

# 讀取原始檔案內容
with open('395b3007-7f9d-4569-9e7b-e18839af7b24', 'r', encoding='utf-8') as file:
    content = file.read()

# 將內容轉換為 JSON 格式
# 假設內容是可以直接轉換的字典格式
try:
    data = json.loads(content)
except json.JSONDecodeError:
    # 如果內容不是 JSON 格式，則將其包裝在一個字典中
    data = {"content": content}

# 將 JSON 格式的內容寫入新檔案
with open('output.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print("轉換完成，已將內容寫入 output.json")