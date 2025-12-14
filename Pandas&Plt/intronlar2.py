import pandas as pd
import matplotlib.pyplot as plt

introns_df = pd.read_table('introns (1).tsv')
introns_df['Position_3to5'] = introns_df.groupby('mRNA').cumcount(ascending=False)+1
introns_df.head()

print(introns_df[introns_df['Position']==1]['Size'].median())
print(introns_df[introns_df['Position']==2]['Size'].median())
print(introns_df[introns_df['Position']==3]['Size'].median())
print(introns_df[introns_df['Position']==4]['Size'].median())
print('...')
print(introns_df[introns_df['Position_3to5']==1]['Size'].median())
print(introns_df[introns_df['Position_3to5']==2]['Size'].median())
print(introns_df[introns_df['Position_3to5']==3]['Size'].median())
print(introns_df[introns_df['Position_3to5']==4]['Size'].median())
print('...')

size_5to3_list = []
size_3to5_list = []

for position in range(1, 11):
  median_5to3 = introns_df[introns_df['Position']==position]['Size'].median()
  median_3to5 = introns_df[introns_df['Position_3to5']==position]['Size'].median()
  size_5to3_list.append(median_5to3)
  size_3to5_list.append(median_3to5)

print(size_5to3_list)
print(size_3to5_list)

size_figure = plt.figure(figsize=[10, 15])
size_subplot1 = size_figure.add_subplot(3, 1, 1)
size_subplot2 = size_figure.add_subplot(3, 1, 2)
size_subplot3 = size_figure.add_subplot(3, 1, 3)
position_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

size_subplot1.plot(position_list, size_5to3_list)
size_subplot1.set_ylabel('Median of Size (bp)\n', fontsize='large')
size_subplot1.set_title('Median Size of Introns Per Position (5 to 3)',
                        fontsize=12, color='blue')

size_subplot2.plot(position_list, size_3to5_list)
size_subplot2.set_ylabel('Median of Size (bp)\n', fontsize='large'),
size_subplot2.set_title('Median Size of Introns Per Position (3 to 5)',fontsize=12, color='purple')

size_subplot3.plot(position_list, size_3to5_list, label = '5 to 3')
size_subplot3.plot(position_list, size_3to5_list, label = '3 to 5')
size_subplot3.set_ylabel('Median of Size (bp)\n', fontsize='large')
size_subplot3.set_title('Median Size of Introns Per Position (3 to 5)',fontsize=12, color='darkgreen')

plt.tight_layout(pad=5.0)

plt.show()