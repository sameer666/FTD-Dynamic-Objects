This script will provide an interactive CLI to create and update Dynamic Objects on FMC

User needs to provide the address and credentials required to make API calls to the FMC

![1](https://user-images.githubusercontent.com/55170586/116532353-c4fc6680-a8fd-11eb-910a-d15a4dbb2541.png)


The user is given four options to choose from
	1. Create a new dynamic objects with or without any mappings
	2. Edit an existing dynamic object to add or remove mappings
	3. Delete an existing dynamic object from FMC
	4. Get a list of current mappings for a dynamic object 

![2](https://user-images.githubusercontent.com/55170586/116532364-c75ec080-a8fd-11eb-8516-ffb7c48be7e9.png)


When creating a new Dynamic Object, user needs to provide a name for the object and has 2 options to provide the mappings. Either directly on the CLI in the form of comma separated values  or as a file path containing the mappings in the form of comma separated values.
User will also have a choice to not provide any mappings at the time of creating a new dynamic object.

![3](https://user-images.githubusercontent.com/55170586/116532367-c9288400-a8fd-11eb-81fc-b5c84cb4b81a.png)


When editing an existing dynamic object, user gets a list of dynamic objects  configured on FMC and needs to select the object to be edited. User will select whether they want to add or remove mappings from the selected object and provide the mappings directly on the CLI in the form of comma separated values. 


![4](https://user-images.githubusercontent.com/55170586/116532375-caf24780-a8fd-11eb-8ccb-ac2c0ec67891.png)

When deleting a dynamic object, user gets a list of dynamic objects configured on FMC and needs to select the object to be deleted. The object selected from the list will get deleted.


![5](https://user-images.githubusercontent.com/55170586/116532379-cb8ade00-a8fd-11eb-9cfd-0c4bac329ea9.png)


When listing the current mappings for a dynamic object, user gets a list of dynamic objects configured on FMC and needs to select the object whose mapping is required. The list of mappings for the selected object is displayed on the cli.

![6](https://user-images.githubusercontent.com/55170586/116532382-cc237480-a8fd-11eb-95e2-f6dc47d79879.png)



To run the application follow the steps below:
	1. pip install -r requirements.txt
	2. python main.py
