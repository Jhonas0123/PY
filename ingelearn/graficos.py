import matplotlib.pyplot as plt
valores = [5,4,3,2,1,0,2,4,4,5]
valores2 = [1,1,1,1,1,1,1,1,1,1]
plt.plot(valores,label="plot1")
plt.plot(valores2,label="plot2")
plt.legend()
plt.style.use("ggplot")
plt.title("grafico")
