import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.font_manager as fm
import os
import time
from pykrx import stock
from PIL import Image
# 오늘 날짜


def img_gen(today):
    # 주식 데이터 받아오기 (종목 코드: 082270, ETF, ETN, ELW 포함)
    # if there is no data, it will return None

    try:
        df = stock.get_market_trading_volume_by_date(
            today, today, "082270", etf=True, etn=True, elw=True, detail=True)
    except Exception as e:
        print(
            f"Error occurred while retrieving stock market trading volume data: {e}")
        return None

    # Transpose the DataFrame
    transposed_df = df.transpose()

    # 한글 폰트 설정
    font_path = 'NanumGothic-Bold.ttf'
    if not os.path.exists(font_path):
        raise FileNotFoundError(f"Font file not found: {font_path}")
    fontprop = fm.FontProperties(fname=font_path)

    # 주식 데이터를 기반으로 DataFrame 생성
    df_for_plot = pd.DataFrame({
        '항목': transposed_df.index,  # 주식 데이터의 인덱스를 항목으로 설정
        '값': transposed_df.iloc[:, 0]  # 첫 번째 열을 값으로 설정 (예: 거래량 데이터)
    })

    # 색상 설정 함수

    def set_color(value):
        if value > 0:
            return 'red'
        elif value < 0:
            return 'blue'
        else:
            return 'black'

    # 그래프 크기 설정
    fig, ax = plt.subplots(figsize=(2, 3))

    # 테이블 출력
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=df_for_plot.values, colLabels=[
        '항목', '값'], cellLoc='center', loc='center')

    # 색상 및 폰트 설정
    for i, key in enumerate(df_for_plot['값']):
        table[(i + 1, 1)].set_text_props(color=set_color(key),
                                         fontsize=12, fontproperties=fontprop)
        table[(i + 1, 0)].set_text_props(fontproperties=fontprop)

    # 여백 설정
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

    # 그래프를 파일로 저장
    plt.savefig('output.png', bbox_inches='tight', dpi=300, format='png')

    # 그래프를 화면에 표시하고 닫기

    # Pillow로 이미지 열고 자르기
    try:
        img = Image.open('output.png')
        # 위에서 50 픽셀 자르기
        cropped_img = img.crop((0, 120, img.width, img.height))

        # 하얀색 빈 공간 추가
        white_space_height = 50  # 추가할 하얀색 공간의 높이
        new_img = Image.new("RGBA", (cropped_img.width,
                            cropped_img.height + white_space_height), (255, 255, 255, 255))
        # 자른 이미지를 하얀색 이미지 아래에 붙여넣기
        new_img.paste(cropped_img, (0, white_space_height))

        # 잘라낸 이미지 저장
        new_img.save(today + '_output.png')
        # output.png 파일 삭제
        os.remove('output.png')

        print("이미지가 성공적으로 저장되었습니다!")
    except Exception as e:
        print(f"이미지를 처리하는 도중 오류가 발생했습니다: {e}")
