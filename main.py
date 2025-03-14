from src import GetAllSeries, store_card_price_in_excel_by_series

if __name__ == '__main__':
    link = 'https://yuyu-tei.jp/top/ua'
    get_all_series = GetAllSeries(link)
    all_series_info = get_all_series.get_all_sereies_links()
    
    for i in all_series_info:
        store_card_price_in_excel_by_series(i['name'], i['link'])
