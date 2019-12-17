def replace_special_char(data):
  special_chars = ['$', ' ', '@' ,'#', '!', '%', '^', '&', '*', '(', ')', ':', ';', ',', '?']
  for k,v in data.dtypes:
    orgK = k
    for i in special_chars:
      if(i in k):
        k = k.replace(i, '')
    if(orgK != k):
      print('changed: {0}, {1}'.format(orgK, k))
      data = data.withColumn(k, col(orgK)).drop(orgK)
  return data
    
def rec_flatten(data, k='', v='', array_ops=''):
  for k,v in data.dtypes:
      if('struct' in v):
        for i in data.select(k+'.*').columns:
          data = data.withColumn(k + "_" + i, col(k+'.'+i)).drop(k)
      if(array_ops == 'array_to_string'):
        if('array' in v and array_ops == 'array_to_string'):
          data = data.withColumn(k+'_array', concat_ws(",", col(k))).drop(k)
  return data

def flatterned_check(dataFrame):
  print("data frame with datatype other than string and double")
  for k,v in dataFrame.dtypes:
    if(v != 'string' and v != 'double'):
      print(k, v)

new_data = rec_flatten(data)
flatterned_check(new_data)
new_data = replace_special_char(new_data)