


from flask import Flask, render_template, url_for
app = Flask(__name__)

# Safe URL helper: use in templates as `safe_url('endpoint')` to avoid BuildError when endpoint missing.
def safe_url(endpoint, **values):
    try:
        return url_for(endpoint, **values)
    except Exception:
        return '#'

# Register helper in Jinja globals so templates can call `safe_url`.
app.jinja_env.globals.update(safe_url=safe_url)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/single')
def single():
    return render_template('single.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
