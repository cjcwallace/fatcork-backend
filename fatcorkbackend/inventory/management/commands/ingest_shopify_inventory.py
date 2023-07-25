import os
import csv
import sys
import json

from django.core.management.base import BaseCommand, CommandError
from inventory.models import Cuvee, Vendor, Product, ProductType, ProductStatus


class Command(BaseCommand):
    """
        Make sure the shopify csv file is in this directory:
            ../../inventory/management/commands
        Run:
            `./manage.py ingest_shopify_inventory products_export_1.csv`
    """
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        # parser.add_argument("poll_ids", nargs="+", type=int)
        parser.add_argument("shopify_csv", nargs="+", type=str)

    def handle(self, *args, **options):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, options['shopify_csv'][0])

        product_types = {
            'Standard': ProductType.STANDARD,
            'Large Format': ProductType.LARGE_FORMAT,
            'Half bottles': ProductType.HALF_BOTTLES,
        }

        product_status = {
            'active': ProductStatus.ACTIVE,
            'archived': ProductStatus.ARCHIVED,
            'draft': ProductStatus.DRAFT,
            '': ProductStatus.NONE,
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
                variant_price = float(row[19] or 0.0)
                variant_compare_at_price = float(row[20] or 0.0)
                image_src = row[24]
                status = product_status[row[49]]
                print('================ NEW BOTTLE =================')
                print(f'{handle=}')
                print(f'{title=}')
                print(f'{vendor=}')
                print(f'{product_category=}')
                print(f'{product_type=}')
                print(f'{tags=}')
                print(f'{published=}')
                print(f'{variant_sku=}')
                print(f'{variant_price=}')
                print(f'{variant_compare_at_price=}')
                print(f'{image_src=}')
                print(f'{status=}')
                # quit()
                if (product_type not in product_types):
                    print(f'Skipping product {product_type}')
                    continue

                product_type = product_types[row[5]]
                vender_obj = Vendor.objects.get_or_create(name=vendor)

                try:
                    cuvee = Cuvee.objects.get(handle=handle)
                    print(f'{cuvee.handle} already created')
                except Cuvee.DoesNotExist:
                    if published == 'true':
                        published_val = True
                    else:
                        published_val = False
                    Cuvee.objects.create(
                        handle=handle,
                        title=title,
                        vendor=vender_obj[0],
                        product_category=product_category,
                        type=product_type,
                        published=published_val,
                        variant_sku=variant_sku,
                        variant_price=variant_price,
                        variant_compare_at_price=variant_compare_at_price,
                        image_src=image_src,
                        status=status,
                    )

        print(json.dumps(col_attrs, indent=2))
