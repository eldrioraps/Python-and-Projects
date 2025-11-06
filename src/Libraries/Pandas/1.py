import pandas as pd
from matplotlib import pyplot as plt
path=r'C:\Users\Ravi\OneDrive\Desktop\edtech\Module-9(Python)\Projects\Batch\src\Libraries\Pandas\youtube_video.csv'
df=pd.read_csv(path)
pd.set_option("display.max_columns",1000)

columns=['video_id', 'title', 'channel_name', 'channel_id', 'view_count',
       'like_count', 'comment_count', 'published_date', 'thumbnail']
df=df[['title', 'channel_name',  'view_count','like_count', 'comment_count', 'published_date']]
df['Serial_Number']=df.index+1
# print(df.head())
# print(df.head())
# print(df.tail())
# print(df.describe())
# print(df.columns)
# print(df.info())
# print(df.shape)
# print(df.dtypes)
# print(df.isna())
# print(df.index)

max_like_count=df["like_count"].mean()
df["Like_Count_%"] = ((df["like_count"] / max_like_count) * 100).round(4).astype(str) + "%"
max_view_count=df["view_count"].mean()
df["View_Count_%"] = ((df["view_count"] / max_view_count) * 100).round(4).astype(str) + "%"
# print(df[["title","View_Count_%"]].head())

df["Like_Count_%_num"] = df["Like_Count_%"].str.rstrip('%').astype(float)
df["View_Count_%_num"] = df["View_Count_%"].str.rstrip('%').astype(float)
df_final = df[(df["Like_Count_%_num"] > 10) & (df["View_Count_%_num"] > 10)]

# df_final.to_csv('clean_csv.csv', index=False)
df_plot = df_final.sort_values("View_Count_%_num", ascending=False).head(10)

df_plot.plot(
    kind='bar',
    x='Serial_Number',
    y='View_Count_%_num',
    title='Top 10 by View Count %',
    ylabel='View Count (%)',
    xlabel='Serial Number',
    legend=False,
    figsize=(8,5)
)
plt.show()