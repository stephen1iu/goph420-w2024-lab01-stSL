import numpy as np
import matplotlib.pyplot as plt

from goph420_lab01.integration import integrate_gauss

def main():
    def prob1(z):
        z=(z-seis_mean)/seis_stddev
        return (1/np.sqrt(2*np.pi))*np.exp(-0.5*z**2)
    seis_mean=1.5
    seis_stddev=0.5
    lims=[1, 5]
    npts=[1, 2, 3, 4, 5]
    integral_arr1=[]
    eps_a1=[]

    for i in (npts):
        integral_arr1.append(integrate_gauss(prob1, lims, npts=i))
        
    for j in range (0, len(npts)-1):
        eps_a1.append(np.abs((integral_arr1[j+1]-integral_arr1[j])/integral_arr1[j+1]))

    def prob2(z):
        z=(z-L_mean)/L_stdev
        return (1/np.sqrt(2*np.pi))*np.exp(-0.5*z**2)
    L_mean=10.28
    L_stdev=0.05
    lims1=[10.25, 10.35]
    integral_arr2=[]
    eps_a2=[]

    for i in (npts):
        integral_arr2.append(integrate_gauss(prob2, lims1, npts=i))
    
    for j in range (0, len(npts)-1):
        eps_a2.append(np.abs((integral_arr2[j+1]-integral_arr2[j])/integral_arr2[j+1]))
    
    plt.loglog(npts[:-1], eps_a1, label="seismic")
    plt.loglog(npts[:-1], eps_a2, label="length")
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()
    plt.xlabel("Number of Points")
    plt.ylabel("Approximate Relative Error")
    plt.title("Log Graph of Number of Points Against Approximate Relative Error")
    plt.savefig("../figures/epsa_vs_npts.png")
    plt.close("all")


if __name__=="__main__":
    main()