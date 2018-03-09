import pandas as pd
import urllib.request
import os

confs = ['2017', '2018']

# select top n papers by review
n = 30

for conf in confs:
    if not os.path.exists(conf):
        os.makedirs(conf)

    df = pd.read_json('data/iclr%s.json' % conf)
    top_n = df.sort_values('rating', ascending=False).head(n)

    for index, row in top_n.iterrows():
        print(row['title'])
        urllib.request.urlretrieve(
            row['url'].replace("forum", "pdf"),
            os.path.join(
                conf,
                '%s_%s_%s.pdf' % (
                    row['rating'], row['title'], ', '.join(row['authors'])
                )
            )
        )
