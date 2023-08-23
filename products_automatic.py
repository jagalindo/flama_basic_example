from flamapy.core.discover import DiscoverMetamodels # This loads the tool in the python execution environment
dm = DiscoverMetamodels()
#result = dm.use_operation_from_file("Products", "./tutorial-splc22/models/pizzas/pizzas.fide")
#result = dm.use_operation_from_file("ValidProduct", "./tutorial-main/models/pizzas/pizzas.fide",configuration_file="./tutorial-main/models/pizzas_nonvalid.csvconf")
print(dm.get_plugins())
#result = dm.use_operation_from_file("Valid", "./pizzas.uvl")
#result = dm.use_operation_from_file("Glucose3Diagnosis", "./pizzas.uvl" ,configuration_file="./pizzas_nonvalid.csvconf")

#result = dm.use_operation_from_file("Glucose3Conflict", "./pizzas.uvl" ,configuration_file="./pizzas_nonvalid.csvconf")
result = dm.use_operation_from_file("Metrics", "./pizzas.uvl")

print(result)