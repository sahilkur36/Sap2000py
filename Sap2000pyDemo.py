from Sap2000py.Saproject import Saproject
import os

#full path to the model
ModelPath = 'F:\python\Sap2000\Models'+os.sep+'Test_Continuous_Bridge.sdb'

# Create a Sap2000py obj (default: attatch to instance and create if not exist)
Sap = Saproject()

# Change Sap api settings if you want
# Sap.createSap(AttachToInstance = True,SpecifyPath = False,ProgramPath = "your sap2000 path")

# Open Sap2000program
Sap.openSap()

# Open Sap2000 sdb file (create if not exist, default: CurrentPath\\NewSapProj.sdb)
Sap.File.Open(ModelPath)

# Can also creat a new blank model (or )
# Sap.File.New_Blank()

# Check your units and set them correctly
Sap.getUnits()
Sap.setUnits(Sap.Units["kN-m-C"])


# Build your Model Here


# run analysis
Sap.Analyze.RunAnalysis()

# Save your file with a Filename(default: your ModelPath)
Sap.File.Save()

# Don't forget to close the program
Sap.closeSap()