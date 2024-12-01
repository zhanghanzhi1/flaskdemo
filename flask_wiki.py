from flask import Flask, render_template, request, redirect, url_for, session
import wikipedia

app = Flask(__name__)
app.secret_key = 'IT@JCUA0Zr98j/3yXa R~XHH!jmN]LWX/,?RT'

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        session['search_term'] = request.form['search']
        return redirect(url_for('results'))
    return render_template("search.html")

@app.route('/results')
def results():
    search_term = session['search_term']
    page, error = get_page(search_term)
    if page:
        return render_template("results.html", page=page, title=page.title)
    else:
        return render_template("error.html", error=error)

def get_page(search_term):
    try:
        return wikipedia.page(search_term), None
    except wikipedia.exceptions.DisambiguationError as e:
        # This is a disambiguation page, provide options to the user
        return None, f"Disambiguation page found. Please be more specific. Possible options: {e.options[:5]}"
    except wikipedia.exceptions.PageError:
        # No such page, inform the user
        return None, "No page found for this term. Please try another search."

if __name__ == '__main__':
    app.run(debug=True)
