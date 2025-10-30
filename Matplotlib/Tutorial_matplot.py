try:
    import matplotlib.pyplot as plt
except ImportError:
    plt - None
z = 3
dias = [1, 2, z, 4, 5, 6, 7]
estoque = [100, 95, 110, 105, 120, 115, 130]

plt.plot(dias, estoque)
plt.title("Exemplo de Gráfico de Linha")
plt.xlabel("Tempo (dias)")
plt.ylabel("Valor (R$)")
plt.legend(labels=['Evolução'])
plt.grid(True)
plt.show()