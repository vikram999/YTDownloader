import streamlit as st 
import yt_dlp
import os

# ---------- CSS + HTML Header with Logo and Navigation ----------
st.markdown(
    """
    <style>
    /* General styling */
    body {
        margin: 0;
        padding: 0;
    }
    .header {
        background-color: #2C3E50;
        color: white;
        padding: 20px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .logo {
        height: 50px;
    }

    .nav-links {
        display: flex;
        gap: 20px;
    }

    .nav-links a {
        color: white;
        text-decoration: none;
        font-weight: bold;
        font-size: 16px;
        transition: 0.3s;
    }

    .nav-links a:hover {
        color: #1abc9c;
    }

    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #2C3E50;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 16px;
    }

    .social-icons a {
        margin: 0 10px;
        color: white;
        text-decoration: none;
        font-size: 20px;
    }

    .social-icons a:hover {
        color: #1abc9c;
    }
    </style>

    <!-- Header Section -->
    <div class="header">
        <div style="display: flex; align-items: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg" class="logo" />
            <h2 style="margin-left: 15px;">Video Downloader</h2>
        </div>
        <div class="nav-links">
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#contact">Contact</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
st.header('download online videos fast & easy')

st.markdown(
    """
    <style>
    .stApp {
        background-color: #e5eaf5; /* light blue */
    }
    </style>
    """,
    unsafe_allow_html=True
)

m = st.markdown("""
<style>
div.stButton > button:first-child {
	box-shadow: 3px 4px 0px 0px #899599;
	background:linear-gradient(to bottom, #ededed 5%, #bab1ba 100%);
	background-color:#ededed;
	border-radius:15px;
	border:1px solid #d6bcd6;
	display:inline-block;
	cursor:pointer;
	color:#3a8a9e;
	font-family:Arial;
	font-size:17px;
	padding:7px 25px;
	text-decoration:none;
	text-shadow:0px 1px 0px #e1e2ed;
}

div.stButton > button:hover {
    background:linear-gradient(to bottom, #bc80ea 5%, #dfbdfa 100%);
	background-color:#bc80ea;
}

div.stButton > button:active {
	position:relative;
	top:3px;
}

</style>""", unsafe_allow_html=True)
 
st.markdown('<p></p>', unsafe_allow_html = True)
st.markdown('<p></p>', unsafe_allow_html = True)
st.markdown('<p></p>', unsafe_allow_html = True)
 
url = st.text_input('Enter Url Here ', "")
c1, c2, c3 = st.columns([1, 1, 1], gap="large")
with c2:
    if(st.button('Start Download')):
        if len(url.strip()) == 0:
            st.error("Enter URL")
            exit()
        URLS = [url]
        class MyLogger:
            def debug(self, msg):
                # For compatibility with youtube-dl, both debug and info are passed into debug
                # You can distinguish them by the prefix '[debug] '
                if msg.startswith('[debug] '):
                    pass
                else:
                    self.info(msg)

            def info(self, msg):
                pass

            def warning(self, msg):
                pass

            def error(self, msg):
                print(msg)

        # ℹ️ See "progress_hooks" in help(yt_dlp.YoutubeDL)
        def my_hook(d):
            if d['status'] == 'finished':
                print('Done downloading, now post-processing ...')
        ydl_opts = {
            'logger': MyLogger(),
            'progress_hooks': [my_hook],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                st.badge("downloading...", color="blue",icon="⏬")
                ydl.download(URLS)
                error_code = 0
            except Exception as err:
                error_code = -1
            if error_code == 0:
                 st.success("Downloaded Successfully")
            else:
                st.error("Error:Please check URL",icon="⚠️")
# ---------- Footer with Social Icons ----------
st.markdown(
    """
    <div class="footer">
        <div class="social-icons">
            <a href="https://twitter.com" target="_blank">🐦</a>
            <a href="https://github.com" target="_blank">💻</a>
            <a href="mailto:vikram.zenith999@gmail.com">✉️</a>
        </div>
        <div>
            © 2025 Vikram | Built with ❤️ and Streamlit
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
     