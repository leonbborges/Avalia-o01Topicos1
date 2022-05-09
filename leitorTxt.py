from csv import (DictWriter)

def ler_arquivo(nome_arquivo):
    headers = ['x1', 'x2', 'x3', 'd']
    with open(f'{nome_arquivo.split(".")[0]}.csv', 'w') as arquivo:
        escritor = DictWriter(arquivo, fieldnames=headers)
        with open(nome_arquivo, 'r') as data:
            for dado in data.readlines():
                dado = dado.replace('\n', '').split()
                escritor.writerow({headers[0]: dado[0],headers[1]: dado[1], headers[2]:dado[2], headers[3]:dado[3]}) if not dado[0] == 'x1' else None
            
            

if __name__ == '__main__':
    ler_arquivo('./content/dataset.txt')
    print('completo!')