try:
    import matplotlib.pyplot as plt
except ImportError:
    plt - None

precos = [50, 120, 300, 80, 20] 
estoque = [80, 25, 10, 70, 150]

plt.scatter(precos, estoque)
plt.title("Exemplo de Gráfico de Dispersão")
plt.xlabel("Tempo (dias)")
plt.ylabel("Valor (R$)")
plt.legend(labels=['Evolução'])
plt.grid(True)
plt.show()