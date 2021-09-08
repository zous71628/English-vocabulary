import urllib.request as req
import bs4

win_Numbers_Sort_lotto = ['SuperLotto638Control_history1_dlQuery_No1_',
                          'SuperLotto638Control_history1_dlQuery_No2_',
                          'SuperLotto638Control_history1_dlQuery_No3_',
                          'SuperLotto638Control_history1_dlQuery_No4_',
                          'SuperLotto638Control_history1_dlQuery_No5_',
                          'SuperLotto638Control_history1_dlQuery_No6_',
                          'SuperLotto638Control_history1_dlQuery_No7_']


def search_winning_numbers(css_class):
    global win_Numbers_Sort_lotto
    if (css_class != None):
        for i in range(len(win_Numbers_Sort_lotto)):
            if win_Numbers_Sort_lotto[i] in css_class:
                return css_class


def parse_tw_lotto_html(data_Info, number_count):
    data_Info_List = []
    data_Info_Dict = {}
    tmp_index = 0
    for index in range(len(data_Info)):
        if (index == 0):
            data_Info_List.append(data_Info[index].text)
        else:
            if (index % number_count != 0):
                data_Info_List.append(data_Info[index].text)
            else:
                data_Info_Dict[str(tmp_index)] = list(data_Info_List)
                data_Info_List = []
                data_Info_List.append(data_Info[index].text)
                tmp_index = tmp_index + 1
        data_Info_Dict[str(tmp_index)] = list(data_Info_List)
    return data_Info_List, data_Info_Dict

class main():
    url = "https://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx"
    request = req.Request(url, headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    header_Info = root.find_all(id=search_winning_numbers)
    data_Info_List, data_Info_Dict = parse_tw_lotto_html(header_Info, 7)
    print(data_Info_Dict)
