from CodeLibrary import Simulation
print("\nThe Library ran without any Syntax Error \n")
#1. instanciate the class and set the aspen name, file path and visibilty
sim = Simulation(AspenFileName= "Simulation 1.apw", WorkingDirectoryPath= r"E:\Programming\Cloned-AspenPlus-Repo\AspenPlus-Python-Interface\test" ,VISIBILITY=True)
input("Press any key to test old command")
sim.BlockPlace("B6","DSTWU")
input("Press any key to test new command")
try:
    sim.BlockPlace("TEST1","RGIBBS")
except:
    print("error thrown")
input("Press any key to test new command")
sim.BLK_RGIBBS_Set_Pressure("TEST1","20")
input("Press any key to test new command")
sim.BLK_RGIBBS_Set_Temperature("TEST1","57")
input("Press any key to test new command")
sim.BLK.Elements("TEST1").Elements("Input").Elements("TEMP").Value = 70
input("Press any key to close aspen")
sim.CloseAspen()