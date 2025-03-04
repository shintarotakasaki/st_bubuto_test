# -*- coding: utf-8 -*-
"""st_bubuto_test

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16lo2PVmG3UF7I9XPjBHhr0qVBl7igbgG
"""

import streamlit as st

# 初期化
if 'delivery_product' not in st.session_state:
    st.session_state.delivery_product = []

# 製品情報と出荷数の入力
product_info = st.text_input("製品情報")
product_quantity = st.number_input("出荷数", min_value=0, step=1)

# ボタンの処理
if st.button("次の製品を入力"):
    if product_info and product_quantity:
        st.session_state.delivery_product.append([product_info, product_quantity])
        st.rerun()

if st.button("伝票作成"):
    if product_info and product_quantity:
        st.session_state.delivery_product.append([product_info, product_quantity])
    st.write("伝票内容:")
    for product in st.session_state.delivery_product:
        st.write(f"製品情報: {product[0]}, 出荷数: {product[1]}")

# 現在の入力内容を表示
st.write("現在の入力内容:")
for product in st.session_state.delivery_product:
    st.write(f"製品情報: {product[0]}, 出荷数: {product[1]}")
