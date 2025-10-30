try:
    import matplotlib.pyplot as plt
except ImportError:
    plt - None

categorias = ['Eletrônicos', 'Vestuário', 'Alimentos']
valores = [15000, 8000, 5000]

plt.pie(valores, labels=categorias)
plt.title("Exemplo de Gráfico de Pizza")
plt.legend(labels=['Evolução'])
plt.show()