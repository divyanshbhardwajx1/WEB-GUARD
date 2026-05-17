from flask import Flask, render_template, request, jsonify

from scanner.crawler import crawl
from scanner.sqli_scanner import scan_sqli
from scanner.xss_scanner import scan_xss

app = Flask(__name__)


@app.route('/')
def dashboard():

    from database import get_db_connection

    db = get_db_connection()

    cursor = db.cursor(dictionary=True)

    query = """

    SELECT *
    FROM scan_reports
    ORDER BY scan_time DESC

    """

    cursor.execute(query)

    history = cursor.fetchall()

    cursor.close()

    db.close()

    return render_template(

        'dashboard.html',

        history=history

    )


@app.route('/scan', methods=['POST'])
def scan():

    data = request.get_json()

    target = data.get('target')

    print("\n[SCANNING]", target)

    urls = crawl(target)

    findings = []

    from database import get_db_connection

    db = get_db_connection()

    cursor = db.cursor()

    for url in urls:

        # =========================
        # SQL Injection Scan
        # =========================

        sqli_results = scan_sqli(url)

        for result in sqli_results:

            result["type"] = "SQL Injection"

            findings.append(result)

        # =========================
        # XSS Scan
        # =========================

        xss_results = scan_xss(url)

        for result in xss_results:

            result["type"] = "XSS"

            findings.append(result)

    # =========================
    # SAVE TO DATABASE
    # =========================

    for finding in findings:

        query = """

        INSERT INTO scan_reports
        (target_url, vulnerability_type, severity, status)

        VALUES (%s, %s, %s, %s)

        """

        values = (

            finding["url"],
            finding["type"],
            finding["severity"],
            "Detected"

        )

        cursor.execute(query, values)

    db.commit()

    cursor.close()

    db.close()

    return jsonify({

        "urls": urls,
        "findings": findings

    })


if __name__ == '__main__':

    app.run(debug=True)