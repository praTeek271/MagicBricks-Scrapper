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
<div class="mb-srp__list" id="cardid69812357"><div class="mb-srp__card"><div class="mb-srp__card__container "><div class="mb-srp__card__photo"><div class="mb-srp__card__photo__fig"><div class="mb-srp__no-image"><div class="mb-srp__no-image__body"><span class="mb-srp__no-image--ico"></span><div class="mb-srp__no-image--text">No Image Available</div></div><div class="mb-srp__card__photo__fig--post">Posted:   Oct 30, '23 </div></div></div><div class="mb-srp__card__ads"><div class="mb-srp__card__ads--name">Owner: Meenakshi Iyer</div></div></div><div class="mb-srp__card__info mb-srp__card__info-withoutburger"><div class="mb-srp__card__tags"><span class="mb-srp__card__tags--tick  no-tick">Only on Magicbricks</span></div><h2 class="mb-srp__card--title" title="1 BHK Flat  for Sale in   Pune">1 BHK Flat  for Sale in   Pune</h2><span class="mb-srp__card__share--icon" data-ico="ico-share"></span><span class="mb-srp__card__sort--icon"></span><span></span><div class="mb-srp__card__summary " id="propertiesAction69812357"><div class="mb-srp__card__summary__list"><div class="mb-srp__card__summary__list--item" data-summary="super-area"><div class="mb-srp__card__summary--label">Super Area</div><div class="mb-srp__card__summary--value">208 sqft</div></div><div class="mb-srp__card__summary__list--item" data-summary="status"><div class="mb-srp__card__summary--label">Status</div><div class="mb-srp__card__summary--value">Ready to Move</div></div><div class="mb-srp__card__summary__list--item" data-summary="floor"><div class="mb-srp__card__summary--label">Floor</div><div class="mb-srp__card__summary--value">2 out of 3</div></div><div class="mb-srp__card__summary__list--item" data-summary="transaction"><div class="mb-srp__card__summary--label">Transaction</div><div class="mb-srp__card__summary--value">Resale</div></div><div class="mb-srp__card__summary__list--item" data-summary="bathroom"><div class="mb-srp__card__summary--label">Bathroom</div><div class="mb-srp__card__summary--value">1</div></div></div><div class="mb-srp__card__summary__action"></div></div><div class="mb-srp__card__usp-wrap has-offer"></div><div class="mb-srp__card--desc remove-truncated"><div class="mb-srp__card--desc--text"><p class="">1 BHK, Multistorey Apartment is available for Sale in , Pune for 8.0 Lac(s)</p><span class="mb-srp__card--desc--readmore">Read more</span></div></div></div></div><div class="mb-srp__card__estimate "><div class="mb-srp__card__price"><div class="mb-srp__card__price--amount"><span class="rupees">₹</span>8 Lac </div><div class="mb-srp__card__price--size"><span class="rupees">₹</span>3,846 per sqft </div></div><div class="mb-srp__action action--single mb-srp__card__action"><span class="mb-srp__action--btn medium btn-red">Contact Owner</span><span class="mb-srp__action--btn medium btn-white">Get Phone No.</span><div class="mb-srp__action--link mb-srp__action--link--nowrap">Get Home Loan</div></div></div><script type="application/ld+json">{"@context":"https://schema.org","@type":"Apartment","@id":"https://www.magicbricks.com/propertyDetails/1-BHK-208-Sq-ft-Multistorey-Apartment-FOR-Sale-in-Pune&id=4d423639383132333537","url":"https://www.magicbricks.com/propertyDetails/1-BHK-208-Sq-ft-Multistorey-Apartment-FOR-Sale-in-Pune&id=4d423639383132333537","numberOfRooms":"1","name":"1 BHK Flat  for Sale in   Pune","potentialAction":{"@type":"BuyAction","seller":{"@type":"Person","name":"Meenakshi Iyer"}},"address":{"@type":"PostalAddress","addressRegion":"Pune","addressCountry":"IN"}}</script></div></div>
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
