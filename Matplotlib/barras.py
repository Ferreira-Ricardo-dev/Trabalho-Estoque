try:
    import matplotlib.pyplot as plt
except ImportError:
    plt - None
z = 3
produtos = ['Mouse', 'Teclado', 'Monitor', 'Webcam']
quantidades = [50, 75, 30, 60]

plt.bar(produtos, quantidades)
plt.title("Exemplo de Gráfico de Barras")
plt.xlabel("Tempo (dias)")
plt.ylabel("Valor (R$)")
plt.legend(labels=['Evolução'])
plt.show()