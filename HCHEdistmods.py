# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 08:47:49 2017

@author: MatthewLazenby
"""
import tkinter as tk
import numpy as np
import pandas as pd
from tkinter import messagebox
dist = tk.Tk()
dist.title("R744 Distributors")

lbl_evap_t = tk.Label(dist, text = "Evap Temperature(°C):", width = 20)
lbl_cap = tk.Label(dist, text = "Capacity(kW):", width = 20)
lbl_liq_t = tk. Label(dist, text = "Liquid Temperature(°C):", width = 20)
lbl_circ = tk.Label(dist, text = "Number of Circuits:", width = 20)
lbl_tail_len = tk.Label(dist, text = "Tail Length(mm):", width = 20)
txtbx_cap = tk.Entry(dist, width = 20)
txtbx_evap_t = tk.Entry(dist, width = 20)
Liqs = ['-20°C','-15°C','-10°C','-5°C','0°C','5°C']
liq_temps = tk.StringVar(dist)
liq_temps.set(Liqs[5])
txtbx_liq_t = tk.OptionMenu(dist, liq_temps, *Liqs)
Tubes = [300, 450, 600, 760, 900, 1050, 1200, 1350, 1500, 1650, 1800]
tube_lens = tk.StringVar(dist)
tube_lens.set(Tubes[0])
txtbx_circ = tk.Entry(dist, width = 20)
txtbx_tail_len = tk.OptionMenu(dist, tube_lens,*Tubes)

lbl_evap_t.grid(row = 0, column = 0, sticky = tk.E)
txtbx_evap_t.grid(row = 0, column = 1)
lbl_cap.grid(row = 1, column = 0, sticky = tk.E)
txtbx_cap.grid(row = 1, column = 1)
lbl_liq_t.grid(row = 2, column = 0, sticky = tk.E)
txtbx_liq_t.grid(row = 2, column = 1)
lbl_circ.grid(row = 3, column = 0, sticky = tk.E)
txtbx_circ.grid(row = 3, column = 1)
lbl_tail_len.grid(row = 4, column = 0, sticky = tk.E)
txtbx_tail_len.grid(row = 4, column = 1)


def dist_nozz_caps():
    count = 0
    test_4 = "!@#$%^&*()_+=<>,?/':;{}[]\|`~-"
    for i in np.arange(0, len(txtbx_evap_t.get()), 1):
        for j in np.arange(0, len(test_4), 1):
            if txtbx_evap_t.get()[i] == test_4[j]:
                count = count + 1
    if count > 0:
        messagebox.showerror("Error","Be sure to enter the values in correctly.")
    else:
        noz_cap = pd.read_excel('Distributor table.xlsx', sheet_name = 'Distributor Nozzle Capacities')
        test_1 = txtbx_evap_t.get()
        if any(c.isalpha() for c in test_1):
            messagebox.showerror("Error","Enter in a valid value for Evap Temperature.")
        else:
            evap_t = float(txtbx_evap_t.get())
            if evap_t >= -25:
                return np.array(noz_cap[['Nozzle number:','-20°C']])
            elif evap_t < -25 and evap_t >= -35:
                return np.array(noz_cap[['Nozzle number:','-30°C']])
            elif evap_t < -35:
                return np.array(noz_cap[['Nozzle number:','-40°C']])
            
def dist_tube_caps():
    count = 0
    test_4 = "!@#$%^&*()_+=<>,?/':;{}[]\|`~"
    for i in np.arange(0, len(txtbx_evap_t.get()), 1):
        for j in np.arange(0, len(test_4), 1):
            if txtbx_evap_t.get()[i] == test_4[j]:
                count = count + 1
    if count > 0:
        messagebox.showerror("Error","Be sure to enter the values in correctly.")
    else:
        test_1 = txtbx_evap_t.get()
        if any(c.isalpha() for c in test_1):
            messagebox.showerror("Error","Enter in a valid value for Evap Temperature.")
        else:
            evap_t = float(txtbx_evap_t.get())
            tube_cap = pd.read_excel('Distributor table.xlsx', sheet_name = 'Distributor Capacity per tube')
            if evap_t >= -25:
                return np.array(tube_cap[['Tube Diameter:','-20°C']])
            elif evap_t < -25 and evap_t >= -35:
                return np.array(tube_cap[['Tube Diameter:','-30°C']])
            elif evap_t < -35:
                return np.array(tube_cap[['Tube Diameter:','-40°C']])
            
            
def calc_dist():
    test_1 = txtbx_evap_t.get()
    test_2 = txtbx_cap.get()
    test_3 = txtbx_circ.get()
    test_4 = "!@#$%^&*()_+=<>,?/':;{}[]\|`~"
    count = 0
    for i in np.arange(0, len(txtbx_evap_t.get()), 1):
        for j in np.arange(0, len(test_4), 1):
            if txtbx_evap_t.get()[i] == test_4[j]:
                count = count + 1
    for i in np.arange(0, len(txtbx_cap.get()), 1):
        for j in np.arange(0, len(test_4), 1):
            if txtbx_cap.get()[i] == test_4[j]:
                count = count + 1
    for i in np.arange(0, len(txtbx_circ.get()), 1):
        for j in np.arange(0, len(test_4), 1):
            if txtbx_circ.get()[i] == test_4[j]:
                count = count + 1
    if any(c.isalpha() for c in test_1) or any(c.isalpha() for c in test_2) or any(c.isalpha() for c in test_3) or count>0 or txtbx_evap_t.get() == "" or txtbx_circ.get() == "" or txtbx_cap.get() == "":
        messagebox.showerror("Error","Be sure to enter the values in correctly.")
    else:
        capacity = float(txtbx_cap.get())
        liq_t = str(liq_temps.get())
        circ = int(txtbx_circ.get())
        tail_len = float(tube_lens.get())

        liq_temp = pd.read_excel('Distributor table.xlsx', sheet_name = 'Liquid Temperature')
        liq_cf = np.array(liq_temp[liq_t])[0]
        nozzy = capacity/liq_cf
        for i in np.arange(0,len(dist_nozz_caps())-1,1):
            compare = dist_nozz_caps()[i]
            compare_1 = dist_nozz_caps()[i+1]
            if compare[1] < nozzy and compare_1[1] > nozzy:
                noz_capacity = compare_1[0]
            elif compare[1] == nozzy:
                noz_capacity = compare[0]
            elif compare_1[1] == nozzy:
                noz_capacity = compare_1[0]

        if nozzy >= float(dist_nozz_caps()[0][1]) and nozzy <= float(dist_nozz_caps()[len(dist_nozz_caps())-1][1]):       
            tail_table = pd.read_excel('Distributor table.xlsx', sheet_name = 'Tubelength') 
            tail_cf = np.array(tail_table[tail_len])[0]
            tube_cap = ((capacity/circ)/tail_cf)/liq_cf
            if tube_cap >= float(dist_tube_caps()[0][1]) and tube_cap <= float(dist_tube_caps()[len(dist_tube_caps())-1][1]):
                for k in np.arange(0,len(dist_tube_caps())-1,1):
                    tube = dist_tube_caps()[k]
                    tube_1 = dist_tube_caps()[k+1]
                    if tube[1] < tube_cap and tube_1[1] > tube_cap:
                        tube_di = tube_1[0]
                    elif tube[1] == tube_cap:
                        tube_di = tube_1[0]
                    elif tube_1[1] == tube_cap:
                        tube_di = tube_1[0]
            elif tube_cap < float(dist_tube_caps()[0][1]):
                tube_di = dist_tube_caps()[0][0]
            elif tube_cap > float(dist_tube_caps()[len(dist_tube_caps())-1][1]):
                messagebox.showerror("Error", "The tube diameter could not be calculated based on the values in the Sporlan tables.")

            hche = pd.read_excel('Distributor table.xlsx', sheet_name = 'HCHE') 
            if tube_di == "3/16":
                mod = np.array(hche[['Model:','3/16','Nozzle size:','Conn. Size OD:','Body size ']])
                dist_mod = []
            elif tube_di == "1/4":
                mod = np.array(hche[['Model:','1/4','Nozzle size:','Conn. Size OD:','Body size ']])
                dist_mod = []
            elif tube_di == "5/16":
                mod = np.array(hche[['Model:','5/16','Nozzle size:','Conn. Size OD:','Body size ']])
                dist_mod = []
            elif tube_di == "3/8":
                mod = np.array(hche[['Model:','3/8','Nozzle size:','Conn. Size OD:','Body size ']])
                dist_mod = []

            for i in np.arange(0,(len(mod)),1):
                chk = mod[i]
                chk_1 = chk[1]
                if str(chk_1) != 'nan':
                    chk_1 = chk[1]
                    for k in np.arange(0,len(chk_1),1):
                        if chk_1[k] == "-":
                            last = chk_1[k+1:len(chk_1)]
                            first = chk_1[0:k]
                            if int(first) <= int(circ) and int(last) >= int(circ):
                                dist_mod.append(chk[0])
            if dist_mod == []:
                messagebox.showerror("Error","No distributor was calculted.")
            else:
                display = dist_mod, circ, tube_di, noz_capacity
                msg = "Possible distributor models:\n%a -%a -%a -%a"%display
                messagebox.showinfo("Suggested Distributors", msg)
            
                return dist_mod,noz_capacity,tube_di,int(circ)
        else:
            messagebox.showerror("Error", "The nozzle size could not be calculated based on the values in the Sporlan tables.")

button_dist = tk.Button(dist, text = "Calculate Distributor",command = calc_dist)
button_dist.grid(row = 5, column = 0, columnspan = 6)
button_dist.focus_set()
dist.mainloop()