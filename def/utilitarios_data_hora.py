from datetime import datetime

def data_hora_atual():
    return datetime.now()
def formatar_data(data,formato = '%Y-%m-%d'):
    return data.strftime(formato)