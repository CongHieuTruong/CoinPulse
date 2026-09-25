# File: app.py
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Giao diện HTML cực kỳ cơ bản có ô nhập liệu
HTML_TEMPLATE = '''
    <h1>CryptoScope MVP - Echo Test</h1>
    <form method="POST">
        <label>Nhập thử một từ khóa (vd: Bitcoin):</label><br>
        <input type="text" name="user_input" required>
        <button type="submit">Submit!</button>
    </form>
    {% if result %}
        <h2 style="color: green;">Hệ thống trả lời: Bạn vừa nhập "{{ result }}"</h2>
    {% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    user_input = None
    if request.method == 'POST':
        user_input = request.form.get('user_input') # Nhận dữ liệu
    return render_template_string(HTML_TEMPLATE, result=user_input) # Echo ra màn hình

if __name__ == '__main__':
    app.run(debug=True)