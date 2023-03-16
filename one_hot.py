import pandas as pd

# Создаем исходный DataFrame
df = pd.DataFrame({
    'color': ['red', 'blue', 'green', 'red', 'green', 'green']
})

# Создаем новый DataFrame, применяя метод pivot_table()
one_hot_df = pd.pivot_table(
    df,
    index=df.index,
    columns=['color'],
    aggfunc=lambda x: 1,
    fill_value=0
)

# Выводим результат
print(one_hot_df)