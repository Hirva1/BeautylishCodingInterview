import requests


class Products:
    """
    class to return desire output
    """

    def __init__(self):
        self.deleted_hidden_products = []
        response = requests.get(url='https://www.beautylish.com/rest/interview-product/list')
        self.product_data = response.json()
        print(self.product_data)
        self.data = self.initial_dict(data=self.product_data)

    @staticmethod
    def initial_dict(data):
        """
        :param data: data which contains initial data from the api https://www.beautylish.com/rest/interview-product/list
        :return: data_list which returns with brand_name,product_name and price
        """

        data_list = {'products': [
            {'brand_name': products.get('brand_name'), 'product_name': products.get('product_name'),
             'price': products.get('price')} for products in data.get('products')]}
        print("List of products including only the brand name, product name, and price:" + str(data_list))
        return data_list

    def hidden_deleted_products(self):
        """
        function to display hidden or deleted products
        :return: hidden or deleted items
        """
        for product in self.product_data.get('products'):
            self.deleted_hidden_products.append(
                {'brand_name': product.get('brand_name'), 'product_name': product.get('product_name'),
                 'price': product.get('price')}) if product.get('deleted') == True or product.get(
                'hidden') == True else ''

        print("Hidden or deleted products list:" + str({'products': self.deleted_hidden_products}))

    def lowest_highest_price(self):
        """
        products list which is sorted by lowest to highest by price and if price is same then product name wise.
        :return: final sorted list of products
        """
        sorted_list = sorted(self.data.get('products'), key=lambda x: float(x['price'].lstrip("$")))

        first_list, second_list, final_list, final_product_list = list(), list(), list(), list()
        new_sorted_list, new_sorted_second_list, new_sorted_third_list = list(), list(), list()
        for i in sorted_list:
            if i.get('price') == '$10.00':
                first_list.append(i)
                new_sorted_list = sorted(first_list, key=lambda x: x['product_name'])
            elif i.get('price') == '$99.99':
                second_list.append(i)
                new_sorted_second_list = sorted(second_list, key=lambda x: x['product_name'])
            else:
                final_list.append(i)
                new_sorted_third_list = sorted(final_list, key=lambda x: x['product_name'])
        final_product_list.extend(new_sorted_list + new_sorted_second_list + new_sorted_third_list)
        print("Sorted list with lowest to highest price:" + str(final_product_list))

    def display_unique_product(self):
        """
        function to return final list of unique products
        :return:
        """
        unique_product = [dict(t) for t in {tuple(d.items()) for d in self.data.get('products')}]
        print("Unique product:" + str(unique_product))

    def unique_products_summary(self):
        """
        function to return product summary
        :return: The total number of unique products,The total number of unique brands, The average price
        """
        unique_product_name = {product_name.get('product_name') for product_name in self.data.get('products')}
        unique_brands = {brands.get('brand_name') for brands in self.data.get('products')}
        average_price = list(float(product.get('price').lstrip("$")) for product in self.data.get('products'))
        average = sum(average_price) / len(average_price)
        print("The total number of unique products is:" + str(len(unique_product_name)))
        print("The total number of unique brands is:" + str(len(unique_brands)))
        print("The average price is $" + str(round(average, 2)))


product_obj = Products()
product_obj.hidden_deleted_products()
product_obj.lowest_highest_price()
product_obj.display_unique_product()
product_obj.unique_products_summary()
