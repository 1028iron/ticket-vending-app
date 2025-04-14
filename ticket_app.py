import streamlit as st

st.title("🎫 自動券売機の操作案内")

# ステップ1: 切符の種類を選ぶ
st.header("① 切符の種類を選んでください")
ticket_type = st.radio(
    "選択肢を選んでください：",
    ("指定席", "自由席", "おトクなきっぷ")
)

# 選択に応じた画像を表示
if ticket_type == "指定席":
    st.image("images/shiteiseki.png", caption="指定席の選択画面")
elif ticket_type == "自由席":
    st.image("images/jiyuuseki.png", caption="自由席の選択画面")
elif ticket_type == "おトクなきっぷ":
    st.image("images/otoku.png", caption="おトクなきっぷの選択画面")

# 「次へ」ボタン
if st.button("▶ 次へ"):
    st.header("② 乗車方法を選んでください")
    train_type = st.radio(
        "どのタイプの列車をご利用ですか？",
        ("新幹線の指定席", "在来線の指定席", "しらさぎから新幹線の乗り継ぎ")
    )

    # 選択に応じた画像を表示
    if train_type == "新幹線の指定席":
        st.image("images/shinkansen.png", caption="新幹線の指定席 選択画面")
    elif train_type == "在来線の指定席":
        st.image("images/zairaisen.png", caption="在来線の指定席 選択画面")
    elif train_type == "しらさぎから新幹線の乗り継ぎ":
        st.image("images/noritsugi.png", caption="乗り継ぎ案内画面")
