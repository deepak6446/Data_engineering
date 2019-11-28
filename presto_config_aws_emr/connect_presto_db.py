from pyhive import presto
cursor = presto.connect(host='public_ip_address_master_node_on_emr', port=8889).cursor()
cursor.execute("SELECT * from hive.default.table_name limit 10")
my_results = cursor.fetchall()
print(my_results)
