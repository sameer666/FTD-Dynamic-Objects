This script will provide an interactive CLI to create and update Dynamic Objects on FMC

User needs to provide the address and credentials required to make API calls to the FMC

The user is given four options to choose from
	1. Create a new dynamic objects with or without any mappings
	2. Edit an existing dynamic object to add or remove mappings
	3. Delete an existing dynamic object from FMC
	4. Get a list of current mappings for a dynamic object 


When creating a new Dynamic Object, user needs to provide a name for the object and has 2 options to provide the mappings. Either directly on the CLI in the form of comma separated values  or as a file path containing the mappings in the form of comma separated values.
User will also have a choice to not provide any mappings at the time of creating a new dynamic object.

When editing an existing dynamic object, user gets a list of dynamic objects  configured on FMC and needs to select the object to be edited. User will select whether they want to add or remove mappings from the selected object and provide the mappings directly on the CLI in the form of comma separated values. 

When deleting a dynamic object, user gets a list of dynamic objects configured on FMC and needs to select the object to be deleted. The object selected from the list will get deleted.

When listing the current mappings for a dynamic object, user gets a list of dynamic objects configured on FMC and needs to select the object whose mapping is required. The list of mappings for the selected object is displayed on the cli.

