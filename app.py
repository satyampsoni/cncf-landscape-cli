from flask import Flask, jsonify
import yaml


app = Flask(__name__)


def load_project_details():
    with open('projects.yml') as f:
        projects_data = yaml.safe_load(f)
    return projects_data

@app.route('/projects/<project_name>')
def get_project_info(project_name):
    projects_data = load_project_details()
    # Find the project details based on the project name
    for category in projects_data.get('landscape', []):
        subcategories = category.get('subcategories', [])
        for subcategory in subcategories:
            items = subcategory.get('items', [])
            for item in items:
                if item.get('name') == project_name:
                    category_name = category.get('name')
                    subcategory_name = subcategory.get('name')
                    item_details = {
                        key.capitalize(): value for key, value in item.items()
                    }
                    return jsonify({
                        "category_name": category_name,
                        "subcategory_name": subcategory_name,
                        "item_details": item_details
                    })
    # Return a 404 response if the project is not found
    return jsonify({"error": "Project not found"}), 404

if __name__ == '__main__':
    app.run()
