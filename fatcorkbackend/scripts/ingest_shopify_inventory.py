import os
import csv
import sys
import json

from inventory.models import Cuvee, Vendor, Product, ProductType, ProductStatus

# file = sys.argv[1]
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'products_export_1.csv')

product_attrs = {

}

product_types = {
    'Standard': ProductType.STANDARD,
    'Large Format': ProductType.LARGE_FORMAT,
    'Half bottles': ProductType.HALF_BOTTLES,
}

product_status = {
    'Archived': ProductStatus.ARCHIVED,
    'Draft': ProductStatus.DRAFT,
    'Active': ProductStatus.ACTIVE,
}

col_attrs = {}
with open(filename, encoding="utf8", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    cols = next(reader)
    for i, item in enumerate(cols):
        col_attrs[item] = i
    for row in reader:
        handle = row[0]
        title = row[1]
        vendor = row[3]
        product_category = row[4]
        product_type = row[5]
        tags = row[6]
        published = row[7]
        variant_sku = row[14]
        variant_price = row[19]
        variant_compare_at_price = row[20]
        image_src = row[24]
        status = row[49]

        quit()

        # if (product_type not in product_types):
        #     continue

        # vender_obj = Vendor.objects.get_or_create(name=vendor)
        # status_obj = product_status[status]

        # try:
        #     cuvee = Cuvee.objects.get(handle=handle)
        # except Cuvee.DoesNotExist:
        #     cuvee = Cuvee.objects.create(
        #         handle=handle,
        #         title=title,
        #         vendor=vender_obj,
        #         product_category=product_category,
        #         type=product_type,
        #         published=published,
        #         variant_sku=variant_sku,
        #         variant_price=variant_price,
        #         variant_compare_at_price=variant_compare_at_price,
        #         image_src=image_src,
        #         status=status_obj,
        #     )


print(json.dumps(col_attrs, indent=2))
