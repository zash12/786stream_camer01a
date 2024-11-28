import streamlit as st

st.title("Camera Access Using WebRTC")
st.markdown("""
This demo uses WebRTC to access your camera. Click the button below to start.
""")

camera_html = """
<video id="video" width="300" height="200" autoplay></video>
<script>
navigator.mediaDevices.getUserMedia({ video: true })
  .then((stream) => {
    document.getElementById('video').srcObject = stream;
  })
  .catch((err) => {
    alert('Error accessing camera: ' + err);
  });
</script>
"""

st.components.v1.html(camera_html, height=250)
