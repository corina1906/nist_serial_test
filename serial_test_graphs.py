from scipy.stats import chi2
import numpy as np
import matplotlib.pyplot as plt
def second_type_error(p1,n,m):
    p0=0.5
    alfa=0.01
    g_lib=2**m-1
    v=p0**m/p1**m
    x=(v*chi2.ppf(1-alfa,g_lib))+((n/m) *(pow((p0**m-p1**m),2)/p0**m*p1**m))
    beta_p_1=chi2.cdf(x,g_lib)
    return beta_p_1
def plot_values(n,m):
    #values = np.arange(0.3, 0.7, 0.001)
    values = np.arange(0.49, 0.51, 0.001)
    # values = np.arange(0.48, 0.52, 0.001)
    beta_values = []
    for p1 in values:
        beta_values.append(second_type_error(p1, n,m))
    beta_values = np.array(beta_values)
    plt.plot(values, beta_values, label=f'm={m}')
    plt.title('Variation of β with respect to H1: p=p1')
    plt.legend(loc='upper right')
    plt.xlabel('p1')
    plt.ylabel('β(p1)')
plot_values(200,2)
plot_values(200,3)
plot_values(200,4)
# plot_values(150,2)
# plot_values(5300,8)

def f(x,y):
    return second_type_error(x,y,m=8)
yline = [n for n in range(5200,7700,100)]
xline = [p1 for p1 in np.arange(0.48, 0.52, 0.001)]
X, Y = np.meshgrid(xline, yline)
Z = f(X,Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('Variation of β with respect to H1: p=p1')
ax.set_xlabel('p1')
ax.set_ylabel('n')
ax.set_zlabel('z')
plt.show()