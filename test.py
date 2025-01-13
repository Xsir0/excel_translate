import pandas as pd
import requests
import json
import traceback
import time
from gemini_api import llm_translate

# pip install openpyxl


def split_list(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]


def translate(content, language: str):
    print('翻译中...')
    try:
        translated_content = str(llm_translate(json.dumps(content), language))
        # translated_content = translated_content.replace(
        #     '```json', '').replace('```', '')
        # result = json.loads(translated_content)
        # if len(result) != len(content):
        #     print('length different: ', len(result), len(content))
        #     return translate(content, language)
        # return result
        return translated_content
    except Exception as e:
        print('异常: ', e, traceback.format_exc())
        time.sleep(2)
        translate(content, language)


def read_translate(source_file, target_file, language):
    df = pd.read_excel(source_file)
    texts_to_translate = df['中文'].astype(str).tolist()

    try:
        # splited_list = split_list(texts_to_translate, 50)
        translated_list = []
        # for item in splited_list:
        for item in texts_to_translate:
            try:
                translated_texts = translate(item, language)
                with open('result1.txt', 'a', encoding='utf-8') as file:
                    # file.writelines(line + '\n' for line in translated_texts)
                    file.write(f"{item} <<>> {translated_texts}")
                # translated_list.extend(translated_texts)
                translated_list.append(
                    translated_texts)
                print('append, list size: ', len(translated_list))
                time.sleep(4)
            except Exception as e:
                print('异常: ', traceback.format_exc())
                translate(item, language)
    except Exception as e:
        print('global error,', traceback.format_exc())
    finally:
        df['泰文'] = translated_list
        df.to_excel(target_file, index=False)
        print(f"翻译完成，结果已保存到 {target_file}")
    print(translated_list)


if __name__ == "__main__":
    input_file = '2.xlsx'
    output_file = '4.xlsx'
    read_translate(input_file, output_file, "泰文")
