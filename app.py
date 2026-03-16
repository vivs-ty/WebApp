import os
import re
import secrets

from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', secrets.token_hex(32))

# Sample data - in a real app, this would typically come from a database
items = [
    {
        'id': 1,
        'title': 'Project Alpha',
        'description': 'Revolutionizing AI-driven automation.',
        'date': '2025-03-13',
        'category': 'Technology'
    },
    {
        'id': 2,
        'title': 'Project Beta',
        'description': 'Advancing next-gen medical research.',
        'date': '2025-03-13',
        'category': 'Research'
    },
    {
        'id': 3,
        'title': 'Project Gamma',
        'description': 'Exploring quantum computing applications.',
        'date': '2025-03-13',
        'category': 'Technology'
    },
    {
        'id': 4,
        'title': 'Project Delta',
        'description': 'Developing sustainable energy solutions.',
        'date': '2025-03-13',
        'category': 'Research'
    },
    {
        'id': 5,
        'title': 'Project Epsilon',
        'description': 'Enhancing cybersecurity with AI.',
        'date': '2025-03-13',
        'category': 'Technology'
    },
    {
        'id': 6,
        'title': 'Project Zeta',
        'description': 'Pioneering advancements in biotechnology.',
        'date': '2025-03-13',
        'category': 'Research'
    },
    {
        'id': 7,
        'title': 'Project Eta',
        'description': 'Creating immersive AR experiences.',
        'date': '2025-03-13',
        'category': 'Technology'
    },
    {
        'id': 8,
        'title': 'Project Theta',
        'description': 'Analyzing climate change patterns.',
        'date': '2025-03-13',
        'category': 'Research'
    },
    {
        'id': 9,
        'title': 'Project Iota',
        'description': 'Building next-gen IoT devices.',
        'date': '2025-03-13',
        'category': 'Technology'
    },
    {
        'id': 10,
        'title': 'Project Kappa',
        'description': 'Investigating human genome sequencing.',
        'date': '2025-03-13',
        'category': 'Research'
    },
    {
        'id': 11,
        'title': 'Project Lambda',
        'description': 'Developing blockchain-based solutions.',
        'date': '2025-03-13',
        'category': 'Technology'
    },
    {
        'id': 12,
        'title': 'Project Mu',
        'description': 'Studying deep-sea ecosystems.',
        'date': '2025-03-13',
        'category': 'Research'
    },
    {
        'id': 13,
        'title': 'Project Nu',
        'description': 'Enhancing cloud computing infrastructure.',
        'date': '2025-03-13',
        'category': 'Technology'
    },
    {
        'id': 14,
        'title': 'Project Xi',
        'description': 'Exploring the effects of space travel.',
        'date': '2025-03-13',
        'category': 'Research'
    },
    {
        'id': 15,
        'title': 'Project Omicron',
        'description': 'Integrating AI into smart homes.',
        'date': '2025-03-13',
        'category': 'Technology'
    },
    {
        'id': 16,
        'title': 'Project Pi',
        'description': 'Advancing neuroscience studies.',
        'date': '2025-03-13',
        'category': 'Research'
    },
    {
        'id': 17,
        'title': 'Project Rho',
        'description': 'Improving autonomous vehicle technology.',
        'date': '2025-03-13',
        'category': 'Technology'
    },
    {
        'id': 18,
        'title': 'Project Sigma',
        'description': 'Developing next-gen cancer treatments.',
        'date': '2025-03-13',
        'category': 'Research'
    },
    {
        'id': 19,
        'title': 'Project Tau',
        'description': 'Innovating AI-driven healthcare.',
        'date': '2025-03-13',
        'category': 'Technology'
    },
    {
        'id': 20,
        'title': 'Project Upsilon',
        'description': 'Investigating renewable energy sources.',
        'date': '2025-03-13',
        'category': 'Research'
    }
]

EMAIL_REGEX = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')
VALID_THEMES = {'light', 'dark'}


def get_categories():
    return sorted({item['category'] for item in items})


def is_valid_email(email):
    return bool(EMAIL_REGEX.match(email))

@app.route('/')
def home():
    search_query = request.args.get('search', '').strip().lower()
    category_filter = request.args.get('category', '').strip()

    filtered_items = items
    if search_query:
        filtered_items = [
            item for item in filtered_items
            if search_query in item['title'].lower() or search_query in item['description'].lower()
        ]

    categories = get_categories()
    if category_filter in categories:
        filtered_items = [item for item in filtered_items if item['category'] == category_filter]

    return render_template(
        'index.html',
        items=filtered_items,
        categories=categories,
        current_theme=session.get('theme', 'light')
    )

@app.route('/item/<int:item_id>')
def item_details(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

@app.route('/about')
def about():
    return render_template('about.html', current_theme=session.get('theme', 'light'))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        if not all([name, email, message]):
            flash('Please fill in all fields.', 'error')
        elif not is_valid_email(email):
            flash('Please enter a valid email address.', 'error')
        elif len(message) < 10:
            flash('Message should be at least 10 characters long.', 'error')
        else:
            # In a real application, you would process the form data here
            flash('Thank you for your message! We will get back to you soon.', 'success')
            return redirect(url_for('contact'))

    return render_template('contact.html', current_theme=session.get('theme', 'light'))

@app.route('/toggle-theme', methods=['POST'])
def toggle_theme():
    payload = request.get_json(silent=True) or {}
    theme = payload.get('theme')

    if theme not in VALID_THEMES:
        return jsonify({'status': 'error', 'message': 'Invalid theme'}), 400

    session['theme'] = theme
    return jsonify({'status': 'success', 'theme': theme})

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', '0') == '1'
    app.run(debug=debug_mode)
