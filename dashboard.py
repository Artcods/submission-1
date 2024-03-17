from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


import streamlit as st 
import pandas as pd
     

# Muat data produk
products_data = pd.read_csv('products_dataset.csv')

# Muat data pembayaran
order_payments_data = pd.read_csv('order_payments_dataset.csv')

# Fungsi untuk menampilkan rata-rata berat produk dalam rentang 500-1200 gram untuk setiap kategori
def tampilkan_rata_rata_panjang_produk():
    rata_rata_panjang_produk = products_data.groupby('product_category_name')['product_weight_g'].mean().sort_values(ascending=False)
    rata_rata_panjang_produk_filtered = rata_rata_panjang_produk[(rata_rata_panjang_produk >= 500) & (rata_rata_panjang_produk <= 1200)]
    st.title('Rata-Rata Berat Product dalam Rentang 500-1200 Gram Setiap Kategori')
    st.bar_chart(rata_rata_panjang_produk_filtered)

    st.write("""
    **Conclusion:**
    Rata-rata panjang produk disetiap kategori yang berada dalam rentang 500 hingga 1200 gram 
    dapat dilihat dari visualisasi dengan menggunakan bar plot. Kategori produk yang memiliki 
    rata-rata panjang produk dalam rentang tersebut akan terlihat pada sumbu x, sedangkan nilai berat rata-rata produk (dalam gram) akan ditampilkan pada sumbu y..
    """)

# Fungsi untuk menampilkan jumlah penggunaan setiap jenis metode pembayaran
def tampilkan_jumlah_metode_pembayaran():
    jumlah_metode_pembayaran = order_payments_data.groupby('payment_type')['order_id'].count()
    st.title('Jumlah Penggunaan Metode Pembayaran')
    st.bar_chart(jumlah_metode_pembayaran)

    st.write("""
    **Conclusion:**
    Jumlah penggunaan metode pembayaran dapat dilihat dari visualisasi dengan menggunakan bar plot. 
    Metode pembayaran yang digunakan akan terlihat pada sumbu x, sedangkan jumlah order yang menggunakan 
    metode tersebut akan ditampilkan pada sumbu y.
    """)

# Buat dashboard Streamlit
st.sidebar.title('Menu')
button_selection = st.sidebar.button("Rata-Rata Berat Product Setiap Kategori")
if button_selection:
    tampilkan_rata_rata_panjang_produk()

button_selection2 = st.sidebar.button("Jumlah Penggunaan Metode Pembayaran")
if button_selection2:
    tampilkan_jumlah_metode_pembayaran()