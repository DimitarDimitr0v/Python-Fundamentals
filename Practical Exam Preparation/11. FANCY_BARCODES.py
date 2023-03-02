import re

pattern = r"(\@{1}\#{1,})(?P<barcode>[A-Z]{1}[A-Za-z0-9]{4,}[A-Z]{1})(\@{1,}\#{1,})"
counter = 0

n = int(input())
text = input()


for rot in range(1, n + 1):
    valid = False
    valid_matches = re.finditer(pattern, text)

    # iterate trough valid barcodes
    for match in valid_matches:
        current_barcode = match.group('barcode')

        # extracting the product code
        temp_product_code = [
            "".join([current_barcode[i] for i in range(len(current_barcode)) if current_barcode[i].isnumeric()])]


        # printing code and confirm its validity
        if temp_product_code == ['']:
            print(f"Product group: 00")
            valid = True

        elif temp_product_code != ['']:
            print(f"Product group: {''.join(temp_product_code)}")
            valid = True

    if not valid:
        print(f"Invalid barcode")

    if rot == n:
        break

    text = input()









