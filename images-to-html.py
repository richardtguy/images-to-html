import csv
from jinja2 import Environment, FileSystemLoader

def generate_html(assets_file, images_file, output_html):

    # Read list of Assets from CSV file 
    assets = []
    with open(assets_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            assets.append(row)

    # Read list of Images from CSV file 
    images = []
    with open(images_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            images.append(row)

    for asset in assets:
        asset['images'] = [image for image in images if image['Related Asset']==asset['Row ID']]

    # Configure Jinja2 environment
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')

    # Render the template with image data
    rendered_html = template.render(assets=assets)

    # Write the HTML content to the output HTML file
    with open(output_html, 'w') as html_file:
        html_file.write(rendered_html)

if __name__ == "__main__":
    assets_file = "Assets - Assets.csv"
    images_file = "Images - Images.csv"
    output_html = "output.html"

    generate_html(assets_file, images_file, output_html)
    print(f"HTML file '{output_html}' has been generated.")
