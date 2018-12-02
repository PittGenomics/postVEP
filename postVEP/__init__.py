import pandas as pd


class VEPresult():
    def __init__(self, file_name):
        with open(file_name) as f:
            while True:
                line = f.readline().rstrip('\n')
                if line.startswith('## Column descriptions:'):
                    break
                else:
                    continue
            self.col_desc = {}
            col_names = []
            while True:
                line = f.readline().rstrip('\n')
                if line.startswith('##') and ':' in line:
                    temp = line.lstrip('## ')
                    temp = temp.split(':')
                    col_name = temp[0].rstrip(' ')
                    col_description = ':'.join(temp[1:])
                    self.col_desc[col_name] = col_description
                    col_names.append(col_name)
                else:
                    break
            del self.col_desc['Extra column keys']
            col_names.remove('Extra column keys')
            predifined_columns = line.lstrip('#').split('\t')
            assert predifined_columns[13] == 'Extra'
            predifined_columns = predifined_columns[:-1]
            data = []
            for line in f:
                temp = line.rstrip('\n').split('\t')
                row = dict(zip(predifined_columns, temp[:13]))
                extras = temp[13].split(';')
                for t in extras:
                    name, value = t.split('=')
                    row[name] = value
                data.append(row)
            self.data = pd.DataFrame.from_dict(data, dtype=str)

    def get_all_col_names(self):
        return self.col_desc.keys()

    def get_col_info(self, key):
        return self.col_desc.get(key)
