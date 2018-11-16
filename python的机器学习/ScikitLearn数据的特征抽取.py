from sklearn.feature_extraction import DictVectorizer

onehot = DictVectorizer()  # 如果结果不用toarray，请开启sparse=False
instances = [{'city': '北京', 'temperature': 100}, {'city': '上海', 'temperature': 60}, {'city': '深圳', 'temperature': 30}]
X = onehot.fit_transform(instances).toarray()
print(onehot.inverse_transform(X))
