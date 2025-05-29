from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from datetime import datetime
import sqlite3
import os

app = Flask(__name__, template_folder='template')
app.secret_key = 'your-secret-key-here'

# Database setup
def init_db():
    conn = sqlite3.connect('real_estate_crm.db')
    c = conn.cursor()
    
    # Clients table
    c.execute('''CREATE TABLE IF NOT EXISTS clients
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  email TEXT,
                  phone TEXT,
                  address TEXT,
                  budget_min REAL,
                  budget_max REAL,
                  property_type TEXT,
                  status TEXT DEFAULT 'Active',
                  notes TEXT,
                  created_date TEXT)''')
    
    # Properties table
    c.execute('''CREATE TABLE IF NOT EXISTS properties
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  address TEXT NOT NULL,
                  price REAL NOT NULL,
                  property_type TEXT,
                  bedrooms INTEGER,
                  bathrooms INTEGER,
                  square_feet INTEGER,
                  status TEXT DEFAULT 'Available',
                  description TEXT,
                  created_date TEXT)''')
    
    # Leads table
    c.execute('''CREATE TABLE IF NOT EXISTS leads
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  email TEXT,
                  phone TEXT,
                  interest TEXT,
                  source TEXT,
                  status TEXT DEFAULT 'New',
                  priority TEXT DEFAULT 'Medium',
                  notes TEXT,
                  created_date TEXT)''')
    
    # Activities table
    c.execute('''CREATE TABLE IF NOT EXISTS activities
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  client_id INTEGER,
                  activity_type TEXT,
                  description TEXT,
                  date TEXT,
                  created_date TEXT)''')
    
    conn.commit()
    conn.close()

# Database helper functions
def get_db_connection():
    conn = sqlite3.connect('real_estate_crm.db')
    conn.row_factory = sqlite3.Row
    return conn

# Routes
@app.route('/')
def dashboard():
    conn = get_db_connection()
    
    # Get dashboard statistics
    total_clients = conn.execute('SELECT COUNT(*) FROM clients').fetchone()[0]
    total_properties = conn.execute('SELECT COUNT(*) FROM properties').fetchone()[0]
    total_leads = conn.execute('SELECT COUNT(*) FROM leads').fetchone()[0]
    active_clients = conn.execute('SELECT COUNT(*) FROM clients WHERE status = "Active"').fetchone()[0]
    
    # Recent activities
    recent_leads = conn.execute('SELECT * FROM leads ORDER BY created_date DESC LIMIT 5').fetchall()
    recent_clients = conn.execute('SELECT * FROM clients ORDER BY created_date DESC LIMIT 5').fetchall()
    
    conn.close()
    
    stats = {
        'total_clients': total_clients,
        'total_properties': total_properties,
        'total_leads': total_leads,
        'active_clients': active_clients
    }
    
    return render_template('dashboard.html', stats=stats, recent_leads=recent_leads, recent_clients=recent_clients)

@app.route('/clients')
def clients():
    conn = get_db_connection()
    clients = conn.execute('SELECT * FROM clients ORDER BY created_date DESC').fetchall()
    conn.close()
    return render_template('clients.html', clients=clients)

@app.route('/clients/add', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        conn = get_db_connection()
        conn.execute('''INSERT INTO clients (name, email, phone, address, budget_min, budget_max, 
                        property_type, notes, created_date)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                     (request.form['name'], request.form['email'], request.form['phone'],
                      request.form['address'], request.form['budget_min'], request.form['budget_max'],
                      request.form['property_type'], request.form['notes'], datetime.now().isoformat()))
        conn.commit()
        conn.close()
        flash('Client added successfully!', 'success')
        return redirect(url_for('clients'))
    
    return render_template('add_client.html')

@app.route('/properties')
def properties():
    conn = get_db_connection()
    properties = conn.execute('SELECT * FROM properties ORDER BY created_date DESC').fetchall()
    conn.close()
    return render_template('properties.html', properties=properties)

@app.route('/properties/add', methods=['GET', 'POST'])
def add_property():
    if request.method == 'POST':
        conn = get_db_connection()
        conn.execute('''INSERT INTO properties (title, address, price, property_type, bedrooms, 
                        bathrooms, square_feet, description, created_date)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                     (request.form['title'], request.form['address'], request.form['price'],
                      request.form['property_type'], request.form['bedrooms'], request.form['bathrooms'],
                      request.form['square_feet'], request.form['description'], datetime.now().isoformat()))
        conn.commit()
        conn.close()
        flash('Property added successfully!', 'success')
        return redirect(url_for('properties'))
    
    return render_template('add_property.html')

@app.route('/leads')
def leads():
    conn = get_db_connection()
    leads = conn.execute('SELECT * FROM leads ORDER BY created_date DESC').fetchall()
    conn.close()
    return render_template('leads.html', leads=leads)

@app.route('/leads/add', methods=['GET', 'POST'])
def add_lead():
    if request.method == 'POST':
        conn = get_db_connection()
        conn.execute('''INSERT INTO leads (name, email, phone, interest, source, priority, notes, created_date)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                     (request.form['name'], request.form['email'], request.form['phone'],
                      request.form['interest'], request.form['source'], request.form['priority'],
                      request.form['notes'], datetime.now().isoformat()))
        conn.commit()
        conn.close()
        flash('Lead added successfully!', 'success')
        return redirect(url_for('leads'))
    
    return render_template('add_lead.html')

@app.route('/client/<int:client_id>')
def client_detail(client_id):
    conn = get_db_connection()
    client = conn.execute('SELECT * FROM clients WHERE id = ?', (client_id,)).fetchone()
    activities = conn.execute('SELECT * FROM activities WHERE client_id = ? ORDER BY date DESC', 
                             (client_id,)).fetchall()
    conn.close()
    
    if client is None:
        flash('Client not found!', 'error')
        return redirect(url_for('clients'))
    
    return render_template('client_detail.html', client=client, activities=activities)

@app.route('/update_lead_status', methods=['POST'])
def update_lead_status():
    lead_id = request.form['lead_id']
    new_status = request.form['status']
    
    conn = get_db_connection()
    conn.execute('UPDATE leads SET status = ? WHERE id = ?', (new_status, lead_id))
    conn.commit()
    conn.close()
    
    return jsonify({'success': True})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)