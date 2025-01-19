# Smart UltraSound Detections

This is the rewrite of the Modeling Interface, which provides a system that helps detect the possible and sustaintial exceptions among the giving B UltraSound Images

Project currently is built using poetry and conda to manage the develop currently, see the documentations/build_from_raw_source.md if one would like to setup from blank for developemnt, or see setup.md to browse how to setup from source code.

Switch to the branch old to see the old version of Smart UltraSound Detections, which named Modeling Interface previously.

CAUTIONS: Poetry is recommanded! As the scripts is setup based the exsitance of peotry!

## Run in Windows

To run the project, you can use the devtools scripts in the root directory as followings

```powershell
devtools.ps1 --setup	# Setup the python dependencies
devtools.ps1 --all	# Setup the runtimes and execute the program
```

see further help with:

```powershell
devtools.ps1 --help
```

## Run in Linux with bash

To run the project, you can use the devtools scripts in the root directory as followings

```bash
devtools --setup	# Setup the python dependencies
devtools --all	# Setup the runtimes and execute the program
```

see further help with:

```bash
devtools.ps1 --help
```

## Functionalities

### Friendly imported

​	You can import images freely in

> 1. Folder way: auto collect the folder's images
> 2. Multi way: Imported by selecting images

​	Images are imported after selections

### Memorized Choices

​	Choices like model selections and reports summon settings are memorized. Once choiced, permenanted used!

### Management In Ui for images

​	manage the imported! you can delete single pictures by using right click to the items in the list, or clear it automatically!

### Report Analysis

​	For Those who owns report, you can download the analysis of the report by uploading the report! Programs will analysis the image and summon suggestions!

### Report generations

​	Main Functionalities! Summon report for each image!

### Audio Server

​	You can control the program in audio way! See the indictions as follows:

> The system allows users to perform various actions through voice commands. The system first checks the voice input to determine the user’s intent and provides corresponding feedback.
>
> 1. **清空操作**: If the voice input contains the word "清空," the system will execute the clear operation.
>
> 2. 导入操作
>
>    : If the input includes "导入," the system further distinguishes the type of import:
>
>    - **文件夹导入**: If the voice mentions "文件夹," the system will allow the user to select a folder for import.
>    - **图片导入**: If the voice mentions "图片," the user can select and import images.
>
> 3. 设置操作
>
>    : If the input contains "设置," the system will execute different actions based on the specific setting:
>
>    - **生成路径设置**: Configure the generate path.
>    - **模型设置**: Set the model for use.
>    - **解析路径设置**: Set the analysis path.
>
> 4. 识别操作
>
>    : If the voice input mentions "识别," the system will perform different actions based on the user's needs:
>
>    - **识别全部**: Execute recognition for all items.
>    - **识别当前**: Execute recognition for the current item.
>    - **识别多张**: Execute recognition for multiple images.
>
> 5. **查看操作**: If the voice mentions "查看," the system will perform view-related operations.
>
> 6. **解析操作**: If the input includes "解析," the system will perform the analysis operation.

