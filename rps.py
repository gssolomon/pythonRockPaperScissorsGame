# -*- coding: utf-8 -*-

#Created on Tue Dec  5 18:09:11 2017
#student number: 040908930
#@author: GLENN SOLOMON


#--------------------------------------------------------------------------
#--------------ROCK---PAPER---SCISSORS---GAME------------------------------
#--------------------------------------------------------------------------


import tkinter as tk
import random

class rps:
        
    #compint=0
    #var = StringVar()
    def __init__(self, top): 
        #top.geometry("250x250")
        self.win=0
        
        self.lose=0
        
        self.tie=0
        
        #self.set_rock=tk.IntVar(top)
        #self.set_rock.set(1)
        #self.set_paper=tk.IntVar(top)
        #self.set_paper.set(2)
        #self.set_scissors=tk.IntVar(top)
        #self.set_scissors.set(3)
    
        self.message = "Rock Paper Scossors Game"  #-------HEADER
        #self.var=tk.StringVar()
        #self.var.set(self.message)
        self.label=tk.Label(top, text=self.message).grid(row=0, column=0, columnspan=3, pady=5)
        
        #-----------ADDING ROCK BUTTON
        self.rock = tk.Button(top, text='Rock', command= lambda: self.call_rock()).grid(row=1, column=0, padx=7)
        #self.rock.pack()
        #-----------ADDING PAPER BUTTON
        self.paper = tk.Button(top, text='Paper', command= lambda: self.call_paper()).grid(row=1, column=1, padx=7)
        
        #self.paper.pack()
        #-----------ADDING SCISSORS BUTTON
        self.scissors = tk.Button(top, text='Scissors', command= lambda: self.call_scissors()).grid(row=1, column=2, padx=7)
        
        #-----------ADDING RESET BUTTON
        self.reset_button=tk.Button(top, text='Reset', command= lambda: self.reset_game(), state=tk.DISABLED)
        self.reset_button.grid(row=2, columnspan=3, pady=5)
        
        self.t=tk.Label(top, text='© COPYRIGHT 2017 Created By Glenn Solomon').grid(row=10, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5, padx=7)
        #self.scissors.pack()
        #self.rock.pack()
        #self.paper.pack()
        #self.scissors.pack()
        
    #-------Rock method called on-click Rock Button        
    def call_rock(self):
        self.set_rock=1
        self.compint=random.randint(1,3)
        
        self.reset_button.configure(state=tk.NORMAL)
        
        self.execute1(self.set_rock,self.compint)
        
    #-------Paper method called on-click Paper Button    
    def call_paper(self):
        self.set_paper=2
        self.compint=random.randint(1,3)
        
        self.reset_button.configure(state=tk.NORMAL)
        
        self.execute1(self.set_paper,self.compint)
        
    #-------Scissors method called on-click Scissors Button    
    def call_scissors(self):
        self.set_scissors=3
        self.compint=random.randint(1,3)
        
        self.reset_button.configure(state=tk.NORMAL)
        
        self.execute1(self.set_scissors, self.compint)
    #-------Reset methon called on-click Reset Button
    
    def reset_game(self):
        self.win=0
        self.lose=0
        self.tie=0
        self.scoreboard(self.win, self.lose, self.tie)
        self.t=tk.Label(top, text='GAME RESET').grid(row=4, column=0, rowspan=3, columnspan=3, sticky=tk.W+tk.E+tk.N+tk.S, pady=5)
        self.reset_button.configure(state=tk.DISABLED)
        
    #-------Execution of the rules to be performed for the Rock-Paper-Scissors Game
    def execute1(self, user_select,compint):
        
        #print("test")
        #self.compint=1
        
        if (user_select==1):
            if (compint==1):
                self.t=tk.Label(top, text='Its a Draw!').grid(row=4, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.tie+=1
                self.t=tk.Label(top, text='Computer Selected ROCK').grid(row=5, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.t=tk.Label(top, text='You Selected ROCK').grid(row=6, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.scoreboard(self.win, self.lose, self.tie)
            elif (compint==2):
                self.t=tk.Label(top, text='Computer Wins!').grid(row=4, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.lose+=1
                self.t=tk.Label(top, text='Computer Selected PAPER').grid(row=5, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.t=tk.Label(top, text='You Selected ROCK').grid(row=6, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.scoreboard(self.win, self.lose, self.tie)
            elif (compint==3):
                self.t=tk.Label(top, text='You WIN!').grid(row=4, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.win+=1
                self.t=tk.Label(top, text='Computer Selected SCISSORS').grid(row=5, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.t=tk.Label(top, text='You Selected ROCK').grid(row=6, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.scoreboard(self.win, self.lose, self.tie)
        elif (user_select==2):
            if (compint==1):
                self.t=tk.Label(top, text='You Win!').grid(row=4, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.win+=1
                self.t=tk.Label(top, text='Computer Selected ROCK').grid(row=5, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.t=tk.Label(top, text='You Selected PAPER').grid(row=6, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.scoreboard(self.win, self.lose, self.tie)
            elif (compint==2):
                self.t=tk.Label(top, text='Its a Draw!').grid(row=4, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.tie+=1
                self.t=tk.Label(top, text='Computer Selected PAPER').grid(row=5, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.t=tk.Label(top, text='You Selected PAPER').grid(row=6, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.scoreboard(self.win, self.lose, self.tie)
            elif (compint==3):
                self.t=tk.Label(top, text='Computer Wins!').grid(row=4, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.lose+=1
                self.t=tk.Label(top, text='Computer Selected SCISSORS').grid(row=5, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.t=tk.Label(top, text='You Selected PAPER').grid(row=6, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.scoreboard(self.win, self.lose, self.tie)
        elif (user_select==3):
            if (compint==1):
                self.t=tk.Label(top, text='Computer Wins!').grid(row=4, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.lose+=1
                self.t=tk.Label(top, text='Computer Selected ROCK').grid(row=5, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.t=tk.Label(top, text='You Selected SCISSORS').grid(row=6, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.scoreboard(self.win, self.lose, self.tie)
            elif (compint==2):
                self.t=tk.Label(top, text='You win!').grid(row=4, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.win+=1
                self.t=tk.Label(top, text='Computer Selected PAPER').grid(row=5, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.t=tk.Label(top, text='You Selected SCISSORS').grid(row=6, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.scoreboard(self.win, self.lose, self.tie)
            elif (compint==3):
                self.t=tk.Label(top, text='Its Draw!').grid(row=4, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.tie+=1
                self.t=tk.Label(top, text='Computer Selected SCISSORS').grid(row=5, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.t=tk.Label(top, text='You Selected SCISSORS').grid(row=6, column=0, columnspan=3, sticky=tk.W+tk.E, pady=5)
                self.scoreboard(self.win, self.lose, self.tie)
    
    #-------Display of Win Lose Tie scores            
    def scoreboard(self, cW, cL, cT):
        self.dispW="Your Score is:  "
        self.dispL="Computer's Score:  "
        self.dispT="Tie Score:  " 
        self.t=tk.Label(top, text=self.dispW+str(cW)).grid(row=7, column=0, columnspan=3, sticky=tk.W, pady=5)
        #self.t=tk.Label(top, textvariable=self.win).grid(row=5, column=2, columnspan=3, sticky=E, pady=5)
        self.t=tk.Label(top, text=self.dispL+str(cL)).grid(row=8, column=0, columnspan=3, sticky=tk.W, pady=5)
        #self.t=tk.Label(top, textvariable=self.lose).grid(row=6, column=2, columnspan=3, sticky=E, pady=5)
        self.t=tk.Label(top, text=self.dispT+str(cT)).grid(row=9, column=0, columnspan=3, sticky=tk.W, pady=5)
        #self.t=tk.Label(top, textvariable=self.tie).grid(row=7, column=2, columnspan=3, sticky=E, pady=5)
                

top = tk.Tk()
game = rps(top)
top.mainloop()