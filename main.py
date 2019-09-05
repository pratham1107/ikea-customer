from flask import Flask, render_template
from google.cloud import datastore
app = Flask(__name__)

client = datastore.Client()
key = client.key('customer', 9876)
entity = datastore.Entity(key=key)
entity.update({
    'name': u'ABC',
    'id': 1,
})
client.put(entity)


@app.route('/getCustomers/<p_id>')
def get_customer_by_id(p_id):
    customer = client.query(kind='customer')
    customer_list = list(customer.fetch())
    for customer_entity in customer_list:
        id = customer_entity.id
        if p_id == id:
            print("customer information is {} and name is {}".format(customer_entity.id,customer_entity.name))
    return ""

@app.route('/getCustomers')
def get_customers():
    customer = client.query(kind='customer')
    customer_list = list(customer.fetch())
    for customer_entity in customer_list:
        id = customer_entity["id"]
        name = customer_entity["name"]
        print("customer information is {} and name is {}".format(id,name))
    return ""

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
