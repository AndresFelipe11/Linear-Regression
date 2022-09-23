import tkinter as tk
from tkinter.filedialog import askopenfile
from src.JsonReader import Json
from src.regression import Regression

class GUI:

    def __init__(self):
        self.root = tk.Tk()
        self.frameBtn = tk.Frame(self.root, bg="white")
        self.frameGraph = tk.Frame(self.root, bg="white")
        
        self.frameBtn.pack(side=tk.LEFT, expand=True, padx=20)
        self.frameGraph.pack(side=tk.RIGHT, expand=True)
    
    def start(self):
        self.root.title("Linear Regression")
        self.root.geometry("750x450")
        self.root.configure(bg="white")

        loadLabel = tk.Label(self.frameBtn, text="Select a JSON file with the data to operate", bg="white", font="Arial 10")
        loadLabel.pack()

        loadFileBtn = tk.Button(self.frameBtn, text="Load File", command=self.readFile)
        loadFileBtn.pack()

        graphLabel = tk.Label(self.frameGraph, text="Linear Regression Graph", font="Arial 15 bold", bg="white")
        graphLabel.pack(pady=0)

        self.root.mainloop()

    def readFile(self):
        path = askopenfile(mode='r', filetypes=[('JSON Files', '*.json')])
        
        if path is not None:
            xName, yName, xData, yData, dataToPredict = Json(path.name).read()
            self.executeRegression(xName, yName, xData, yData, dataToPredict)

    def executeRegression(self, xName, yName, xData, yData, dataToPredict):
        regression = Regression(xData, yData)
        regression.start()
        predictedData = regression.predict(dataToPredict)
        
        print("For {} = {} the predicted {} is {}".format(xName, dataToPredict, yName, predictedData))