import streamlit as st
import requests as r
import re
import time


def download_file(url, save_as=None, block_size=1024):
    req = r.get(url, stream=True)
    total_size = int(req.headers.get('content-length', 0))

    if save_as is None:
        save_as = re.sub(r"[?!&].*", "", url.split("/")[-1])
    with open(save_as, 'wb') as f:
        downloaded_size = 0
        for data in req.iter_content(block_size):
            downloaded_size += len(data)
            percent = int((downloaded_size/total_size)*100)
            bar.progress(percent)
            desc_text.text(f"{percent}% done")
            f.write(data)

    desc_text.text("Completed!")


st.title("mini-progress-app")

large_file_button = st.button("Download large file")
image_button = st.button("Download image")
iterate_button = st.button("Simply iterate")

bar = st.progress(0)
desc_text = st.empty()

if large_file_button:
    download_file("http://www.ovh.net/files/10Mb.dat")
elif image_button:
    download_file(
        "https://i.ytimg.com/vi/Yw6u6YkTgQ4/maxresdefault.jpg",
        block_size=1024
        )
elif iterate_button:
    for i in range(101):
        bar.progress(i)
        desc_text.text(f"{i}% done")
        time.sleep(0.1)
