from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():

    return """
    <h1>Vulnerable Test App</h1>

    <ul>
        <li><a href='/login'>SQL Injection Page</a></li>
        <li><a href='/search'>XSS Page</a></li>
    </ul>
    """


# =========================
# SQLi Vulnerable Page
# =========================

@app.route('/login')
def login():

    user_id = request.args.get("id", "")

    query = f"SELECT * FROM users WHERE id = '{user_id}'"

    sql_keywords = [

        "'",

        "\"",

        "--",

        "OR",

        "or"

    ]

    for keyword in sql_keywords:

        if keyword in user_id:

            return f"""
            SQL syntax error near:
            {query}
            """

    return """
    <h2>Login Page</h2>

    <form>

        <input type='text' name='id' placeholder='Enter ID'>

        <button type='submit'>
            Login
        </button>

    </form>
    """


# =========================
# XSS Vulnerable Page
# =========================

@app.route('/search')
def search():

    user_input = request.args.get("input", "")

    return f"""
    <h2>Search Page</h2>

    <form>

        <input type='text'
        name='input'
        placeholder='Search here'>

        <button type='submit'>
            Search
        </button>

    </form>

    <p>
        You searched for:
        {user_input}
    </p>
    """


if __name__ == '__main__':

    app.run(port=5001, debug=True)