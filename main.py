import pandas as pd


df = pd.read_csv('dataset.csv')
entry = pd.read_csv('entry.csv')
# rows, columns = df.shape
columns = df.columns


if __name__ == '__main__':
	count_x = {i: None for i in columns[1:]}
	for i in columns[1:]:
		count_x[i] = df[i].value_counts().to_dict()

	# class probability
	probabilities_y = df[columns[0]].value_counts(normalize=True).to_dict()

	# xij probability
	probabilities_x = {i: {} for i in columns[1:]}
	for i in columns[1:]:
		for j in count_x[i].keys():
			probabilities_x[i].update({j: {}})
			for y in probabilities_y.keys():
				xij = df.loc[(df[columns[0]] == y) & (df[i] == j)]
				prop = len(xij) / count_x[i][j]
				probabilities_x[i][j].update({y: prop})

	# classify entries
	for row in entry.iloc:
		# result_entry = row[columns[0]]
		result = {}
		for y in probabilities_y.keys():
			result.update({y: None})
			calc = probabilities_y[y]
			for i in columns[1:]:
				calc *= probabilities_x[i][row[i]][y]
			result[y] = calc
		print(result)

	# for row in entry.itertuples(index=True):
	# 	print(type(row['age']))

	## just a remider
	# querys
	# data = df.loc[(df['Contact-lenses']=='soft') & (df['age']=='young')]
	# print(data)
