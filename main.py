from flask import Flask, render_template_string, session
from datetime import datetime
import os
import random
import string
import requests
app = Flask(__name__)
# 🧠 HTML TEMPLATE
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>🧟𝗕𝗔⃪𝗗⃪𝗠⃪𝗔⃪𝗦⃪𝗛⃪𝗢⃪ 𝗞⃪𝗔⃪ 𝗕⃪𝗔⃪𝗔⃪𝗣⃪ 𝗪⃪𝗔⃪𝗦⃪𝗨⃪ 𝗕⃪𝗛𝗔⃪𝗧⃪🧟</title>
  <style>
    body { font-family: sans-serif; background-color: #f4f4f4; text-align: center; padding: 20px; }
    h2 { color: #ff0000; }
    .timer { font-size: 20px; margin-bottom: 10px; }
    .date { font-weight: bold; margin-bottom: 20px; }
    .box { border: 2px solid #000; border-radius: 10px; padding: 15px; margin: 15px auto; width: 90%; max-width: 500px; background: #fff; }
    .btn { padding: 10px 20px; background: #000; color: white; border: none; border-radius: 6px; margin-top: 10px; display: inline-block; cursor: pointer; }
    .footer { margin-top: 40px; font-size: 14px; }
  </style>
</head>
<body>
  <h2>👿𝗪⃪𝗔⃪𝗦⃪𝗨⃪ 𝗕⃪𝗔⃪𝗗⃪𝗠⃪𝗔⃪𝗦⃪𝗛⃪👿</h2>
  <div class="timer" id="timer">Loading timer...</div>
  <div class="date">📆 LIVE DATE::⪼ {{ current_date }}</div>

  {% for box in boxes %}
  <div class="box">
    <img src="{{ box.image }}" alt="img" width="100%" style="border-radius: 10px;">
    {% if box.text %}<h3>{{ box.text }}</h3>{% endif %}
    {% if box.link %}
      {% if loop.index0 == 0 %}
        <button class="btn" onclick="checkPassword('{{ box.link }}')">{{ box.button }}</button>
      {% else %}
        <a href="{{ box.link }}" class="btn">{{ box.button }}</a>
      {% endif %}
    {% endif %}
  </div>
  {% endfor %}

  <div class="footer">
    <p>
      <a href="/terms">Terms</a> | <a href="/privacy">Privacy</a>
    </p>
    <p>
      <a href="https://www.facebook.com/profile.php?id=61574766223435">Facebook</a> |
      <a href="http://fi9.bot-hosting.net:20566/">WhatsApp</a> |
      <a href="https://github.com/devixayyat/">GitHub</a>
    </p>
    <p>© 2025 𝗕⃪𝗛⃪𝗔⃪𝗧⃪ 𝗪⃪𝗔⃪𝗦⃪𝗨⃪  All RIGHTS RESERVED.</p>
    <p>𝗠⃪𝗔⃪𝗗⃪𝗘⃪ 𝗕⃪𝗬⃪ 𝗕⃪𝗛⃪𝗔⃪𝗧⃪ 𝗪⃪𝗔⃪𝗦⃪𝗨⃪ <b>𝗫⃪ 𝗔⃪𝗭⃪𝗥⃪𝗔⃪</b></p>
  </div>

  <script>
    function updateTimer() {
      const now = new Date();
      const time = now.toLocaleTimeString();
      document.getElementById("timer").innerText = "⌛ LIVE TIMER::⪼ " + time;
    }
    setInterval(updateTimer, 1000);
    updateTimer();

    function checkPassword(link) {
      const pass = prompt("🎋🛡 ENTER PASSWORD TO ACCESS THIS SERVER 🎋🛡");
      if (pass === "WASU X AZRA") {
        window.location.href = link;
      } else {
        alert("❌ BHAT WASU NY TERE KO REJECT KAR DIYA..😞❤️");
      }
    }
  </script>
</body>
</html>
'''

# 🖼️ ROUTE
@app.route('/')
def home():
    boxes = [   
        {"image": "https://i.ibb.co/dw8bqDcx/20250829-121752.jpg", "text": "", "link": "http://fi1.bot-hosting.net:6350", "button": "⊲ 𝗖⃪𝗢⃪𝗡⃪𝗩⃪𝗢⃪ 𝗣⃪𝗔⃪𝗚⃪𝗘⃪ 1 ⊳"},
        {"image": "https://i.ibb.co/20TLs8tB/20250829-121917.jpg", "text": "", "link": "http://de3.bot-hosting.net:20064", "button": "⊲ 𝗖⃪𝗢⃪𝗡⃪𝗩⃪𝗢⃪ 𝗣⃪𝗔⃪𝗚⃪𝗘⃪ 2 ⊳"},
        {"image": "https://i.ibb.co/1G79WmBL/20250829-121834.jpg", "link": "http://fi7.bot-hosting.net:20594", "button": "⊲ 𝗣⃪𝗢⃪𝗦⃪𝗧⃪ 𝗣⃪𝗔⃪𝗚⃪𝗘⃪ 𝗦⃪𝗘⃪𝗥⃪𝗩⃪𝗘⃪𝗥⃪ ⊳"},
        {"image": "https://i.ibb.co/V0qG7gDQ/20250829-121640.jpg", "link": "http://de3.bot-hosting.net:20078", "button": "⊲ 𝗪⃪𝗛⃪𝗔⃪𝗧⃪𝗦⃪𝗔⃪𝗣⃪𝗣⃪ 𝗦⃪𝗘⃪𝗥⃪𝗩⃪𝗘⃪𝗥⃪ ⊳"},
        {"image": "https://i.ibb.co/20K1jtPZ/20250829-161910.jpg", "link": "https://token-checker-plum.vercel.app/", "button": "⊲ 𝗧⃪𝗢⃪𝗞⃪𝗘⃪𝗡⃪ 𝗖⃪𝗛⃪𝗘⃪𝗖⃪𝗞⃪𝗘⃪𝗥⃪ ⊳"},
        {"image": "https://i.ibb.co/Cs9GM32L/1749189275397.jpg", "link": None, "button": None}
    ]
    current_date = datetime.now().strftime("%d %B %Y").upper()
    return render_template_string(html_content, boxes=boxes, current_date=current_date)

# ▶️ RUN
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
