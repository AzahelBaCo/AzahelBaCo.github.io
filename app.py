from flask import Flask, request, render_template
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form.get('name')
    return f"Hola, {name}!"

def load_services():
    tree = ET.parse('services.xml')
    root = tree.getroot()
    services = {}
    for service in root.findall('service'):
        name = service.get('name')
        endpoint = service.find('endpoint').text
        method = service.find('method').text
        services[name] = {'endpoint': endpoint, 'method': method}
    return services

if __name__ == '__main__':
    services = load_services()
    app.run(debug=True)
