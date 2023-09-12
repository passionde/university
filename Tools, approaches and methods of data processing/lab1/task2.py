from keras.datasets import boston_housing
from sklearn.linear_model import Ridge
from sklearn import metrics

# Получение данных
(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()

# Нормализация данных
mean = train_data.mean(axis=0)
train_data -= mean

std = train_data.std(axis=0)

train_data /= std
test_data -= mean
test_data /= std

# Создание и обучение модели
clf = Ridge()
clf.fit(train_data, train_targets)

Y_pred = clf.predict(test_data)

mae = metrics.mean_absolute_error(test_targets, Y_pred)
print(f"Средняя абсолютная ошибка (MAE): {mae}")
