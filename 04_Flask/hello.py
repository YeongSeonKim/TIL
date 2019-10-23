from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    # return 'Hello World'
    return render_template('index.html')

@app.route('/dohyeon')
def dohyeon():
    return '저는 무술가입니다.'   
    
@app.route('/html')
def html():
    return '<h1>태그 사용할 수 있어용!</h1>'

@app.route('/html_multiline')
def html_multiline():
    return '<h1>안녕안녕</h1>'

# 동적 라우팅(Variable Routing)
@app.route('/greeting/<string:name>')
def greeting(name):
    # return f'안녕, {name}?'
    return render_template('greeting.html', html_name=name)

# 세제곱을 돌려주는 cube 페이지 작성!

# end of file!!!
# debug 모드를 활성화해서 서버 새로고침을 생략한다.
if __name__ == '__main__':
    app.run(debug=True)