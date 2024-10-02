from maedong import img_gen
from datetime import datetime, timedelta
from pykrx import stock
import streamlit as st
from maedong import img_gen
# 오늘의 젬백스 주가 가져오기
import os
# 젬백스의 종목 코드
ticker = "082270"  # 젬백스의 KRX 종목 코드
today = datetime.today().strftime('%Y%m%d')
# today like 09/30
today_a = datetime.today().strftime('%m/%d')
# 오늘 날짜의 주가 가져오기
today_price_data = stock.get_market_ohlcv(today, today, ticker)
# 어제 날짜의 주가 가져오기
yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y%m%d')
yesterday_price_data = stock.get_market_ohlcv(yesterday, yesterday, ticker)
# 어제와 오늘의 변동폭 계산

st.title(today_a+' 젬백스 매매동향')
st.write(today_price_data)
d = st.date_input("매매동향 불러오기", datetime.today(), format='YYYY/MM/DD')

generate_button = st.button("매매동향 불러오기")
if generate_button:
    process_message = st.info("매매동향을 불러오는 중입니다.")
    d = d.strftime('%Y%m%d')
    try:
        df = stock.get_market_trading_volume_by_date(
            d, d, "082270", etf=True, etn=True, elw=True, detail=True)
        img_gen(d)
        process_message.empty()
        st.success("매매동향을 성공적으로 불러왔습니다.")
        st.image(str(d)+'_output.png',
                 use_column_width=True)

    except Exception as e:
        st.error(e)
        st.error(d+"의 매매동향 데이터가 없습니다")
