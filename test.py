import pandas as pd
import requests
import json
import traceback
import time
from gemini_api import llm_translate

# pip install openpyxl


def split_list(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]


def translate(content,language:str):
    print('翻译中...')
    try:
        translated_content = str(llm_translate(json.dumps(content),language))
        translated_content = translated_content.replace('```json','').replace('```','')
        return json.loads(translated_content)
    except Exception as e:
        print('异常: ',e,traceback.format_exc())
        time.sleep(2)
        translate(content)

def read_translate(source_file,target_file,language):
    df = pd.read_excel(source_file)
    texts_to_translate = df['A'].astype(str).tolist()

    splited_list = split_list(texts_to_translate,30)
    translated_list = []
    for item in splited_list:
        try:
            translated_texts = translate(item,language)
            translated_list.extend(translated_texts)
            print('append, list size: ',len(translated_list))
            time.sleep(5)
        except Exception as e:
            print('异常: ',traceback.format_exc())
            translate(item)
    df[language] = translated_list
    df.to_excel(target_file, index=False)
    print(f"翻译完成，结果已保存到 {target_file}")

    print(translated_list)
    


if __name__ == "__main__":
    input_file = 'new_file.xlsx'
    output_file = 'output.xlsx'
    read_translate(input_file,output_file,"菲律宾语")

