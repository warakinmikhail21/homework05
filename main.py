import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder(sparse=false)
one_hot_encoder == encoder.fit_transform(data[['whoAmI']])
one_hot_df = pd.DataFrame(one_hot_encoder, columns= encoder.get_feature_names_out(['whoAmI']))
data_one_hot = data.join(one_hot_df)