from goph420_lab01.integration import integrate_newton

import numpy as np
import matplotlib.pyplot as plt

def main():

    s_wave_data=np.loadtxt(fname="s_wave_data.txt")
    t_raw=s_wave_data[:,0]
    v_raw=s_wave_data[:,1]

    max_v=max(np.abs(v_raw))
    v_last=max_v*0.005

    for i in range (0,1001):
        if v_raw[i] > v_last:
            index_max=i

    plot_t=[t_raw[0], t_raw[index_max]]
    plot_v=[v_raw[0], v_raw[index_max]]

    T=t_raw[index_max]
    t=t_raw[:index_max]
    v=v_raw[:index_max]

    print(plot_t, plot_v)

    plt.plot(t_raw, v_raw, label="velocity vs time")
    plt.plot(plot_t, plot_v, "ro", label="bounds of integration")
    plt.xlabel("Time(s)")
    plt.ylabel("Velocity(mm/s)")
    plt.title("Raw Velocity Time Data")
    plt.legend()
    plt.savefig("../figures/raw_data.png")
    plt.close("all")

    int_trap_arr=[[], [], [], [], []]
    int_simp_arr=[[], [], [], [], []]
    eps_trap=[]
    eps_simp=[]

    delt=[1, 2, 4, 8, 16]
    delta=[0.01, 0.02, 0.04, 0.08, 0.16]

    for i in range (0, len(delt)):
        t2=[]
        v2=[]
        for k in range (0, index_max, delt[i]): #creating sampling interval values of different spacings
            t2.append(t[k])
            v2.append(v[k])
        integral_simp=integrate_newton(t2, v2, alg="simp")
        integral_trap=integrate_newton(t2, v2, alg="trap")
        int_trap_arr[i].append(integral_trap)
        int_simp_arr[i].append(integral_simp)

    for j in range (len(delt)-1):
        eps_trap.append(np.abs((int_trap_arr[j+1][0]-int_trap_arr[j][0])/int_trap_arr[j+1][0]))
        eps_simp.append(np.abs((int_simp_arr[j+1][0]-int_simp_arr[j][0])/int_simp_arr[j+1][0]))

    plt.loglog(delta[:-1], eps_trap, label="trapezoid")
    plt.loglog(delta[:-1], eps_simp, label="simpson")
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()
    plt.xlabel("Sampling Intervals")
    plt.ylabel("Approximate Relative Error")
    plt.title("Log Graph of Sampling Intervals Against Approximate Relative Error")
    plt.savefig("../figures/epsa_vs_delta.png")
    plt.close("all")

if __name__=="__main__":
    main()