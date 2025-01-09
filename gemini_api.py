import requests
import json

headers = {
    "Content-Type": "application/json",
}

baseURL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash"
api_key = "AIzaSyARPtL2sWusm9UjsWSUel0HtHIL5j6CjyM"




def llm_translate(text,language:str):
    image_parse_prompt = f"""
给出的内容是一个列表，列表中是待翻译成{language}的中文，请将翻译后的结果按照顺序返回，只需返回翻译后的列表即可,列表里的内容请使用双引号，不要使用单引号，不需要其他任何额外的内容。
需要翻译的内容如下：
{text}
"""
    url = f'{baseURL}:generateContent?key={api_key}'
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": image_parse_prompt
                    }
                ]
            }
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            ret = response.json()
            if "candidates" in ret and len(ret['candidates']) > 0:
                content = ret['candidates'][0]['content']
                print('content: ',content['parts'][0]['text'])
                return content['parts'][0]['text']
            else:
                print('error: ', ret)
                return None
        else:
            print("request fail ", response.status_code,
                  response.content, end="\n\n")
            return None
    except Exception as e:
        print(f'text_generation exception, {text}', e,response.status_code)
        return None


if __name__ == "__main__":
#     text_generation(json.dumps(contents))
    import pandas as pd
    contents = ["今天天气怎么样？", "你能帮我查一下明天的航班吗？", "附近有没有好吃的餐厅？", "北京时间现在几点？", "你能给我讲个笑话吗？", "最近的电影院在哪里？", "明天的日出时间是什么时候？", "你能帮我写一首小诗吗？", "附近有没有公园可以散步？", "苹果公司最新发布的产品是什么？", "你能帮我推荐一本好看的书吗？", "最近的图书馆在哪里？", "世界杯冠军是谁？", "你能帮我设计一个简单的logo吗？", "最近的博物馆在哪里？", "中国最长的河流是哪一条？", "你能帮我解释一下量子力学吗？", "最近的邮局在哪里？", "最近有什么热门的电视剧？", "你能帮我做一份PPT演示文稿吗？", "最近的健身房在哪里？", "最近有什么新的游戏发布？", "你能帮我写一封求职信吗？", "最近的酒店在哪里？", "最近的演唱会是什么？", "你能帮我翻译一篇英文文章吗？", "最近的咖啡馆在哪里？", "最近的画展是什么？", "你能帮我写一篇关于人工智能的论文吗？", "最近的银行在哪里？", "明天的天气预报是什么？", "你能帮我查一下火车时刻表吗？", "附近有没有商场可以购物？", "最近的股市行情怎么样？", "你能帮我设计一个简单的网页吗？", "最近的超市在哪里？", "最近有什么新的科技产品发布？", "你能帮我写一篇产品说明书吗？", "最近的加油站在哪里？", "最近有什么新的手机发布？", "你能帮我写一篇新闻报道吗？", "最近的药店在哪里？", "最近有什么新的汽车发布？", "你能帮我写一篇市场调研报告吗？", "最近的医院在哪里？", "最近有什么新的电影上映？", "你能帮我写一篇商业计划书吗？", "最近的学校在哪里？", "最近有什么新的综艺节目？", "你能帮我写一篇演讲稿吗？", "最近的图书馆分馆在哪里？", "最近有什么新的音乐专辑发布？", "你能帮我写一篇学术论文吗？", "最近的公园入口在哪里？", "最近有什么新的艺术展览？", "你能帮我写一篇文学评论吗？", "最近的博物馆纪念品商店在哪里？", "最近有什么新的体育赛事？", "你能帮我写一篇影评吗？", "最近的健身房器械区在哪里？", "最近有什么新的科技突破？", "你能帮我写一篇书评吗？", "最近的酒店游泳池在哪里？", "最近有什么新的环保技术？", "你能帮我写一篇博客文章吗？", "最近的咖啡馆户外座位在哪里？", "最近有什么新的能源政策？", "你能帮我写一篇社交媒体帖子吗？", "最近的银行ATM机在哪里？", "最近有什么新的教育改革？", "你能帮我写一封电子邮件吗？", "最近的超市停车场在哪里？", "最近有什么新的医疗进展？", "你能帮我写一条短信吗？", "最近的加油站卫生间在哪里？", "最近有什么新的社会问题？", "你能帮我写一个问卷调查吗？", "最近的药店急救室在哪里？", "最近有什么新的政治事件？", "你能帮我写一份报告吗？", "最近的医院急诊科在哪里？", "最近有什么新的经济形势？", "你能帮我写一份总结吗？", "最近的学校图书馆在哪里？", "最近有什么新的文化现象？", "你能帮我写一份计划书吗？", "最近的图书馆自习室在哪里？", "最近有什么新的艺术潮流？", "你能帮我写一份预算表吗？", "最近的公园儿童游乐区在哪里？"]
    df = pd.DataFrame({'A': contents})
    # df = pd.read_excel("translate.xlsx")
    # df['中文']=contents
    df.to_excel("new_file.xlsx", index=False)
    