import pandas as pd
from scipy.io import arff
import matplotlib.pyplot as plt


data, meta = arff.loadarff('data/BME_TRAIN.arff')
df = pd.DataFrame(data)
df['target'] = df['target'].apply(lambda x: x.decode('utf-8') if isinstance(x, bytes) else x)

begin_class = df[df['target'] == "1"].drop(columns='target')
middle_class = df[df['target'] == "2"].drop(columns='target')
end_class = df[df['target'] == "3"].drop(columns='target')

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
for i in range(len(begin_class)):
    plt.plot(range(1, 129), begin_class.iloc[i], alpha=0.5)
plt.title('Class: Begin')
plt.xlabel('Time step')
plt.ylabel('Amplitude')

plt.subplot(1, 3, 2)
for i in range(len(middle_class)):
    plt.plot(range(1, 129), middle_class.iloc[i], alpha=0.5)
plt.title('Class: Middle')
plt.xlabel('Time step')


plt.subplot(1, 3, 3)
for i in range(len(end_class)):
    plt.plot(range(1, 129), end_class.iloc[i], alpha=0.5)
plt.title('Class: End')
plt.xlabel('Time step')

plt.tight_layout()
plt.show()