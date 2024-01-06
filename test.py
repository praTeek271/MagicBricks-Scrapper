# import re

# def extract_bhk(description):
#     # Regular expression to find Bhk information
#     bhk_pattern = re.compile(r'(\d+)\s*BHK', re.IGNORECASE)

#     # Search for Bhk information in the description
#     match = bhk_pattern.search(description)

#     if match:
#         return int(match.group(1))
#     else:
#         return None

# # Example usage
# property_description = "Studio Apartment is available for Sale in Ambegaon BK, Pune for 1.0 Lac(s)"

# # Extract Bhk information
# bhk_info = extract_bhk(property_description)

# if bhk_info is not None:
#     print(f"Bhk information found: {bhk_info} BHK")
# else:
#     print("Bhk information not found.")


from bs4 import BeautifulSoup

html_content = """
<div class="mb-srp__card__summary__list">
    <div class="mb-srp__card__summary__list--item" data-summary="super-area">
        <div class="mb-srp__card__summary--label">Super Area</div>
        <div class="mb-srp__card__summary--value">340 sqft</div>
    </div>
    <div class="mb-srp__card__summary__list--item" data-summary="floor">
        <div class="mb-srp__card__summary--label">Floor</div>
        <div class="mb-srp__card__summary--value">Ground out of 3</div>
    </div>
    <div class="mb-srp__card__summary__list--item" data-summary="bathroom">
        <div class="mb-srp__card__summary--label">Bathroom</div>
        <div class="mb-srp__card__summary--value">1</div>
    </div>
</div>
"""

soup = BeautifulSoup(html_content, 'html.parser')

def extract_values_from_html(soup):
    super_area = None
    floor = None
    total_floors = None
    bathrooms = None

    # Find all items with the specified class
    summary_items = soup.find_all('div', class_='mb-srp__card__summary__list--item')

    for item in summary_items:
        label = item.find('div', class_='mb-srp__card__summary--label')
        value = item.find('div', class_='mb-srp__card__summary--value')

        if label and value:
            label_text = label.text.strip().lower()
            value_text = value.text.strip()

            if 'super area' in label_text:
                super_area = int(value_text.split(' ')[0])
            elif 'floor' in label_text:
                floor_data = value_text.split(' out of ')
                floor = floor_data[0].strip()
                total_floors = int(floor_data[1].strip())
            elif 'bathroom' in label_text:
                bathrooms = int(value_text)

    return super_area, floor, total_floors, bathrooms

# Example usage
super_area, floor, total_floors, bathrooms = extract_values_from_html(soup)

print(f"Super Area: {super_area} sqft")
print(f"Floor: {floor}")
print(f"Total Floors: {total_floors}")
print(f"No. of Bathrooms: {bathrooms}")
