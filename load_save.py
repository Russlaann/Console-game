import pickle

# СОХРАНЕНИЕ
data_to_save = {'name': 'test', 'value': 42}

with open('save.dat', 'wb') as f:  # 'wb' - write binary
    pickle.dump(data_to_save, f)
print("Данные сохранены")

# ЗАГРУЗКА
with open('save.dat', 'rb') as f:  # 'rb' - read binary
    loaded_data = pickle.load(f)
print("Загруженные данные:", loaded_data)