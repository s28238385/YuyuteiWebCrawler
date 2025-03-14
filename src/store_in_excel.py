from src import GetAllCard
import pandas as pd


def store_card_price_in_excel_by_series(series_name, link):
    get_all_card = GetAllCard(link)
    get_all_card.get_all_card_info()
    all_card_info_this_series = get_all_card.price_list
    df = pd.DataFrame(all_card_info_this_series)
    excel_filename = f"./result/{series_name}.xlsx"
    df.to_excel(excel_filename, index=False, engine='openpyxl')
    print(f"已成功將資料存入 {excel_filename}")
